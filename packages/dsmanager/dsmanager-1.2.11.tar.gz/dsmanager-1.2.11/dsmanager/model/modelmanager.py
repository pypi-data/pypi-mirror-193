"""@Author Rayane AMROUCHE

ModelManager Class.
"""

import pickle

from typing import Any, List, Union

import optuna  # type: ignore

from dsmanager.model.model import Model
from dsmanager.model.utils import Utils
from dsmanager.controller.utils import pickle_to_ds
from dsmanager.controller.logger import Logger


class ModelManager:
    """ModelManager class handle all the Model work."""

    def __init__(
        self,
        save_path: str = "data/models.save",
    ) -> None:
        """Init Modelmanager.

        Args:
            save_path (str, optional): Path of the models save for the ModelManager.
                Defaults to "data/models.save".
        """
        Logger.update_logger(
            name="modelmanager",
            logger=optuna.logging._get_library_root_logger(),
        )
        if save_path:
            self.models = pickle_to_ds(save_path)
        else:
            raise TypeError("No model's path given")

        self.utils = Utils()
        self.__save_path = save_path

    def __repr__(self) -> str:
        res = "ModelManager:\n"
        res += f"Models: {list(self.models.keys())}\n"
        models_params = {
            name: list(model.params.keys()) for name, model in self.models.items()
        }
        models_estimators = {
            name: model.estimator for name, model in self.models.items()
        }
        res += "Models' params: {\n"
        for name, param_list in models_params.items():
            res += f"\t'{name}': {param_list},\n"
        res += "}\n"
        res += "Models' estimator: {\n"
        for name, estimator_list in models_estimators.items():
            res += f"\t'{name}': {estimator_list},\n"
        res += "}\n"
        return res

    def _save_mm(self):
        with open(self.__save_path, mode="wb") as outfile:
            pickle.dump(self.models, outfile)

    def add_model(
        self,
        name: str,
        estimator: Any,
        params: dict,
        **kwargs: Any,
    ) -> None:
        """Generate and add a model to the model manager models dict.

        Args:
            name (str): Name of the model to add.
            estimator (Any): Model class.
            params (dict): Dict of params for grid search.
        """
        self.models[name] = Model(name, estimator, params, **kwargs)
        self._save_mm()

    def update_model(
        self,
        name: str,
        **kwargs: Any,
    ) -> None:
        """Generate and add a model to the model manager models dict.

        Args:
            name (str): Name of the model to add.
            estimator (Any): Model class.
        """
        self.models[name].set_params(**kwargs)
        self._save_mm()

    def get_model(self, name: str, **kwargs: Any) -> Any:
        """Get a model from the model manager models dict.

        Args:
            name (str): Name of the model.

        Returns:
            Any: Model instance.
        """
        model = self.models[name]
        model.estimator.set_params(**kwargs)
        return model

    def get_optuna_params(self, names: List[str]) -> dict:
        """Get params for optuna grid search.

        Args:
            names (List[str]): Names of the models to use.

        Returns:
            dict: Params for the optuna grid search.
        """

        all_params = {}
        models = []
        for name in names:
            temp_params = self.models[name].get_optuna_params()
            for param in temp_params:
                all_params[f"{name}__{param}"] = temp_params[param]
            models.append(self.models[name])
        all_params["model"] = Utils.to_distribution(models)
        return all_params

    def study(  # pylint: disable=too-many-arguments
        self,
        study: Any,
        names: Union[List[str], str],
        X: Any,  # pylint: disable=invalid-name
        y: Any,  # pylint: disable=invalid-name
        custom_scorer: Any = None,
        **kwargs: Any,
    ) -> Any:
        """Study a list of models with a given dataset.

        Args:
            names (Union[List[str],str]): List of name of the models to tune.
            X (Any): The data matrix.
            y (Any): The labels for X. Defaults to None.
            custom_scorer (Any, optional): Function that takes 3 mains arguments:
                "model", "X" and "y" as well some keyword arguments given through models
                params or additional kwargs. Defaults to None.

        Returns:
            Any: Study instance.
        """
        if len(names) == 1:
            names = names[0]
        if isinstance(names, str):
            params = self.models[names].get_optuna_params()
            params["model"] = self.models[names]
        else:
            params = self.get_optuna_params(names)

        kwargs["X"] = X
        kwargs["y"] = y

        if custom_scorer is None:
            custom_scorer = Utils.generic_scorer

        trial_params = {}
        for param_name, param_value in params.items():
            if not isinstance(param_value, optuna.distributions.BaseDistribution):
                kwargs[param_name] = param_value
            else:
                trial_params[param_name] = param_value

        study = Utils.launch_study(study, custom_scorer, trial_params, **kwargs)
        return study

    def study_to_model(self, study: Any, name: Any = None, trial_id: int = -1) -> Any:
        """Extract best model from a study.

        Args:
            study (Any, optional): Study from which the model is to be extracted.
            name (Any, optional): Name of the model to save.
            trial_id (int, optional): Exact trial number to select. Defaults to -1.

        Returns:
            Any: Model extracted from the trial.
        """
        if trial_id < 0:
            trial_id = study.best_trial.number
        model = study.trials[trial_id].user_attrs.pop("model")
        model.set_params(**study.trials[trial_id].params)

        if name is None:
            name = study.study_name
        self.models[name] = model
        self.models[name].name = name
        self._save_mm()
        return model

    def get_model_cv(  # pylint: disable=too-many-arguments
        self,
        study: Any,
        names: Union[List[str], str],
        X: Any,  # pylint: disable=invalid-name
        y: Any,  # pylint: disable=invalid-name
        custom_scorer: Any = None,
        **kwargs: Any,
    ) -> Any:
        """Get Optuna CV model.

        Args:
            names (Union[List[str],str]): List of name of the models to tune.
            X (Any): The data matrix.
            y (Any): The labels for X. Defaults to None.
            custom_scorer (Any, optional): Function that takes 3 mains arguments:
                "model", "X" and "y" as well some keyword arguments given through models
                params or additional kwargs. Defaults to None.

        Returns:
            Any: Best model among the ones given for the given X and y.
        """
        study = self.study(study, names, X, y, custom_scorer, **kwargs)
        model = self.study_to_model(study, study.study_name)
        return model
