"""@Author Rayane AMROUCHE

Utils for ModelManager.
"""

import os
import datetime
import itertools

from concurrent.futures import FIRST_COMPLETED
from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
from typing import Any, Set, Optional

import optuna  # type: ignore

from sklearn.model_selection import cross_val_score  # type: ignore

from dsmanager.controller.utils import fill_kwargs
from dsmanager.controller.logger import Logger


class Utils:
    """Utils class brings utils tools for the model manager."""

    @staticmethod
    def generic_scorer(
        model: Any, X: Any, y: Any = None, **kwargs  # pylint: disable=invalid-name
    ) -> float:
        """Generate a generic scorer and return score.

        Args:
            model (Any): Model class or instance used for the cross val scorer.
            X (Any): The data matrix.
            y (Any, optional): The labels for X. Defaults to None.

        Returns:
            Any: Score of cross_val_score of X wrt. y.
        """
        cv_kwargs = fill_kwargs(cross_val_score, **kwargs)
        if callable(model):
            model = model(**kwargs)
        model.set_params(**kwargs)
        cv_kwargs["estimator"] = model
        return cross_val_score(X=X, y=y, **cv_kwargs).mean()

    @staticmethod
    def _one_study(  # pylint: disable=too-many-arguments
        study: Any,
        scorer: Any,
        n_trials: Any,
        timeout: Any,
        distributions_params: dict,
        fixed_params: dict,
    ):
        i_trial = 0
        time_start = datetime.datetime.now()
        while True:
            if n_trials is not None:
                if i_trial >= n_trials:
                    break
                i_trial += 1

            if timeout is not None:
                elapsed_seconds = (datetime.datetime.now() - time_start).total_seconds()
                if elapsed_seconds >= timeout:
                    break

            trial = study.ask(distributions_params)
            fixed_params.update(trial.params)
            score = scorer(**fixed_params)
            if "model" in fixed_params:
                trial.set_user_attr(key="model", value=fixed_params["model"])
            study.tell(trial, score)
            Utils._log_completed_trial(study)

        return study

    @staticmethod
    def _many_study(  # pylint: disable=too-many-arguments
        study: Any,
        scorer: Any,
        n_jobs: int,
        n_trials: Any,
        timeout: Any,
        distributions_params: dict,
        fixed_params: dict,
    ):
        time_start = datetime.datetime.now()

        def to_exec(study_, scorer_, distributions_params_, fixed_params_):
            trial = study_.ask(distributions_params_)
            fixed_params_.update(trial.params)
            score = scorer_(**fixed_params_)
            if "model" in fixed_params_:
                trial.set_user_attr(key="model", value=fixed_params_["model"])
            study_.tell(trial, score)
            Utils._log_completed_trial(study)

        futures: Set[Future] = set()
        with ThreadPoolExecutor(max_workers=n_jobs) as executor:
            for i_trial in itertools.count():
                if n_trials is not None and i_trial >= n_trials:
                    break

                if timeout is not None:
                    elapsed = (datetime.datetime.now() - time_start).total_seconds()
                    if elapsed >= timeout:
                        break

                if len(futures) >= n_jobs:
                    completed, futures = wait(futures, return_when=FIRST_COMPLETED)
                    for _f in completed:
                        _f.result()

                futures.add(
                    executor.submit(
                        to_exec, study, scorer, distributions_params, fixed_params
                    )
                )

    @staticmethod
    def launch_study(  # pylint: disable=too-many-arguments
        study: Any,
        scorer: Any,
        distributions_params: dict,
        n_jobs: int = 1,
        n_trials: Any = None,
        timeout: Any = None,
        **fixed_params: Any,
    ) -> Any:
        """Generate a study and launch a certain number of optimization trials.

        Args:
            study (Any): Optuna study.
            scorer (Any): Function that returns a score and take both distributions
                parameters and fixed parameters.
            distributions_params (dict): Dict of params as optuna distributions.
            n_trials (int): Number of trials to run. Defaults to 5.

        Returns:
            Any: Study trained.
        """
        if study is None:
            study = optuna.create_study()
        elif isinstance(study, str):
            study = optuna.create_study(study_name=study)
        elif isinstance(study, dict):
            study = optuna.create_study(**study)

        if study._thread_local.in_optimize_loop:  # pylint: disable=protected-access
            raise RuntimeError("Nested invocation of launch_study isn't allowed.")

        try:
            if n_jobs == 1:
                Utils._one_study(
                    study, scorer, n_trials, timeout, distributions_params, fixed_params
                )
            else:
                if n_jobs == -1:
                    n_jobs = os.cpu_count() or 1
                Utils._many_study(
                    study,
                    scorer,
                    n_jobs,
                    n_trials,
                    timeout,
                    distributions_params,
                    fixed_params,
                )
        finally:
            study._thread_local.in_optimize_loop = (  # pylint: disable=protected-access
                False
            )

        return study

    @staticmethod
    def to_distribution(*args: Any) -> Any:
        """Transform argument to distribution.

        Returns:
            Any: Arguments as an optuna distribution.
        """
        res: Optional[optuna.distributions.BaseDistribution] = None
        if len(args) == 1:
            _l = args[0]
            if isinstance(_l, optuna.distributions.BaseDistribution):
                return _l
            if isinstance(_l, range):
                res = optuna.distributions.IntDistribution(
                    _l.start, _l.stop, step=_l.step
                )
            elif isinstance(_l, (list, tuple)):
                if all(isinstance(x, int) for x in _l):
                    res = optuna.distributions.IntDistribution(min(_l), max(_l))
                elif all(isinstance(x, (float, int)) for x in _l):
                    res = optuna.distributions.FloatDistribution(min(_l), max(_l))
                else:
                    res = optuna.distributions.CategoricalDistribution(_l)
        elif len(args) == 2 and all(isinstance(x, (int, float)) for x in args):
            if any(isinstance(x, float) for x in args):
                res = optuna.distributions.FloatDistribution(*args)
            elif all(isinstance(x, int) for x in args):
                res = optuna.distributions.IntDistribution(*args)
        if res is None:
            res = optuna.distributions.CategoricalDistribution(args)
        return res

    @staticmethod
    def _log_completed_trial(study: Any) -> None:
        trial = study.trials[-1]
        if len(trial.values) > 1:
            Logger.get_logger("modelmanager").info(
                "Trial %s finished with values: %s and parameters: %s.",
                trial.number,
                trial.values,
                trial.params,
            )
        elif len(trial.values) == 1:
            best_trial = study.best_trial
            Logger.get_logger("modelmanager").info(
                "Trial %s finished with value: %s and parameters: %s. "
                "Best is trial %s with value: %s.",
                trial.number,
                trial.values[0],
                trial.params,
                best_trial.number,
                best_trial.value,
            )
        else:
            assert False, "Should not reach."
