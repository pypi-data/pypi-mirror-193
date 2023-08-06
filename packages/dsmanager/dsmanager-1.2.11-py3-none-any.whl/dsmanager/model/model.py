"""@Author Rayane AMROUCHE

Model Class.
"""

import inspect

from typing import Any, Optional

from sklearn.base import BaseEstimator  # type: ignore

from dsmanager.model.utils import Utils


class Model(BaseEstimator):
    """Estimor Class to parametrize model in a pipeline."""

    def __init__(
        self,
        name: str,
        estimator: Any,
        params: Optional[dict] = None,
        **kwargs: Any,
    ) -> None:
        """Init class Model with an estimator.

        Args:
            name (str): Name of the model.
            estimator (Any): Estimator associated.
            params (Dict): Dict of params for grid search. Defaults to None.
        """
        self.name = name
        if callable(estimator):
            self.estimator = estimator()
        else:
            self.estimator = estimator
        self.params = params
        self.set_params(**kwargs)

    def set_params(self, **params):
        """Set params."""
        if "name" in params:
            setattr(self, "name", params["name"])
        if "estimator" in params:
            setattr(self, "estimator", params["estimator"])

        if callable(self.estimator):
            init_signature = inspect.signature(self.estimator)
        else:
            init_signature = inspect.signature(self.estimator.__class__)

        parameters = [
            p.name
            for p in init_signature.parameters.values()
            if p.name != "self" and p.kind != p.VAR_KEYWORD
        ]

        for key_, value_ in params.items():
            try:
                cur_name, cur_key = key_.split("__")
                if "name" in params and cur_name != params["name"]:
                    continue
                if "name" not in params and cur_name != self.name:
                    continue
            except ValueError as _:
                cur_key = key_
            if cur_key in parameters:
                setattr(self, cur_key, value_)
                setattr(self.estimator, cur_key, value_)

    def fit(
        self,
        X: Any,  # pylint: disable=invalid-name
        y: Any = None,  # pylint: disable=invalid-name
        **kwargs: Any,
    ) -> None:
        """Fit the model according to the given training data.

        Args:
            X (Any): Training data matrix.
            y (Any, optional): Target vector. Defaults to None.
        """
        self.estimator.fit(X, y, **kwargs)

    def predict(
        self,
        X: Any,  # pylint: disable=invalid-name
    ) -> None:
        """Predict class labels for samples in X.

        Args:
            X (Any): The data matrix for which we want to get the predictions.

        Raises:
            Exception: Raised if model is not fitted.

        Returns:
            Any: Vector containing the class labels for each sample.
        """
        return self.estimator.predict(X)

    def predict_proba(
        self,
        X: Any,  # pylint: disable=invalid-name
    ) -> None:
        """Probability estimates.

        Args:
            X (Any): The data matrix for which we want to get the predictions.

        Raises:
            Exception: Raised if model is not fitted.

        Returns:
            Any: Returns the probability of the sample for each class in the model.
        """
        return self.estimator.predict_proba(X)

    def score(
        self, X: Any, y: Any = None  # pylint: disable=invalid-name
    ) -> Any:  # pylint: disable=invalid-name
        """Score using the `scoring` option on the given test data and labels.

        Args:
            X (Any): The data matrix for which we want to get the predictions.
            y (Any, optional): True labels for X. Defaults to None.

        Raises:
            Exception: Raised if model is not fitted.

        Returns:
            Any: Score of self.predict(X) wrt. y.
        """
        return self.estimator.score(X, y)

    def get_optuna_params(self) -> dict:
        """Get params for a gridsearch.

        Returns:
            dict: Returns params dict by transforming params to optuna distributions.
        """
        params = {}  # type: dict
        if self.params is None:
            return params
        for key_, value_ in self.params.items():
            params[key_] = Utils.to_distribution(value_)
        return params

    def __str__(self) -> str:
        return (
            f"Model(name={self.name}, "
            f"estimator={repr(self.estimator)}, "
            f"params={self.params}"
        )

    def __repr__(self, N_CHAR_MAX=700):
        return (
            f"Model(name={self.name}, "
            f"estimator={repr(self.estimator)}, "
            f"params={self.params}"
        )
