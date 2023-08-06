"""@Author: Rayane AMROUCHE

DataFrame Pipeline class.
"""

import collections

from typing import Any, Generator

import pandas as pd  # type: ignore

from dsmanager.controller.logger import Logger


Logger.update_logger(name="data_pipeline")


class Step:
    """Step class."""

    def __init__(
        self,
        __is_leaf: bool,
        __output_name: Any,
        __func: Any,
        *args,
        **kwargs,
    ) -> None:
        """Init a step with a pipeline instance, a func and its args/kwargs.

        Args:
            __is_leaf (bool): Check whether step is a leaf.
            __output_name (Any): Name of the output in env.
            __func (Any): Function of the step.
            __name (Any): Name of the step.
        """
        self.is_leaf = __is_leaf
        self.output_name = __output_name
        self.func = __func
        self.args = args
        self.kwargs = kwargs
        self.name = "default"

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return (self.func, self.args, self.kwargs)

    def __str__(self) -> str:
        func_name = self.func if isinstance(self.func, str) else self.func.__name__
        return f"<{str(self.name)}> [{func_name}]"


class DataPipeline:
    """DataFrame Pipeline class."""

    def __init__(self, **kwargs) -> None:
        """Init a pipeline with a list of steps and env vars as kwargs."""
        Logger.update_logger(name="data_pipeline")
        self.steps: collections.OrderedDict = collections.OrderedDict({})
        self.env = kwargs

    def add_vars(self, **kwargs) -> Any:
        """Add a var to the pipeline env.

        Returns:
            Any: Returns the updated pipeline.
        """
        self.env.update(**kwargs)
        return self

    def set_name(self, name: str) -> Any:
        """Change name of a step.

        Args:
            name (str): Name to give to a step.

        Returns:
            Any: Returns the updated pipeline.
        """
        last_step = next(reversed(self.steps))
        old_name = self.steps[last_step].name
        for _ in range(len(self.steps)):
            key_, value_ = self.steps.popitem(False)
            self.steps[name if old_name == key_ else key_] = value_
        self.steps[name].name = name
        return self

    def use_env(self, var_aliases: dict) -> Any:
        """Add DataPipeline env variables in kwargs as given names.

        Args:
            var_aliases (dict): Dict with the key being the name of the var in the
                DataPipeline and value the name to put in kwargs.

        Returns:
            Any: Returns the updated pipeline.
        """
        last_step = next(reversed(self.steps))
        func = self.steps[last_step].func

        def enved_func(__df, *args_, **kwargs_):
            kwargs_.update(**{v: self.env[k] for k, v in var_aliases.items()})
            return func(__df, *args_, **kwargs_)

        enved_func.__qualname__ = func.__qualname__
        self.steps[last_step].func = enved_func
        return self

    def add_step(self, __func: Any, *args, **kwargs) -> Any:
        """Add a step to a DataPipeline.

        Args:
            func (Any): Step function.

        Returns:
            Any: return the pipeline updated with the new step.
        """
        name = f"step_{len(self.steps)}"
        step = Step(False, None, __func, *args, **kwargs)
        setattr(step, "name", name)
        self.steps[name] = step
        return self

    def add_steps(self, steps: list) -> Any:
        """Add a list of steps to a DataPipeline.

        Args:
            steps (Any): List of step written a tuple. The first element is a function,
                the second is a list of args and the third is a dict of kwargs.

        Returns:
            Any: return the pipeline updated with the new step.
        """
        for step in steps:
            __func, args, kwargs = step
            name = f"step_{len(self.steps)}"
            step = Step(False, None, __func, *args, **kwargs)
            setattr(step, "name", name)
            self.steps[name] = step
        return self

    def add_leaf(self, __output_name: Any, __func: Any, *args, **kwargs) -> Any:
        """Add a step that does not return a dataframe to a DataPipeline.

        Args:
            func (Any): Step function.

        Returns:
            Any: return the pipeline updated with the new step.
        """
        name = f"step_{len(self.steps)}"
        step = Step(True, __output_name, __func, *args, **kwargs)
        setattr(step, "name", name)
        self.steps[name] = step
        return self

    def __call__(self, __df) -> Any:
        steps = [v for _, v in self.steps.items()]
        return self._loop_pipe(__df, (element for element in reversed(steps)))

    def __repr__(self) -> str:
        res = "DataPipeline:\n"
        res += "Steps order: [\n\t"
        res += "\n\t-> ".join(str(v) for _, v in self.steps.items())
        res += "\n]\n"
        res += "Env vars: {\n\t"
        res += ",\n\t".join(f"{str(k)}: {str(v)}" for k, v in self.env.items())
        res += "\n}"
        return res

    def _loop_pipe(
        self, __df: pd.DataFrame, generator: Generator[Any, None, None]
    ) -> pd.DataFrame:
        try:
            cur = next(generator)
        except StopIteration:
            return __df

        tmp_func = cur.func
        jump_val = self._loop_pipe(__df, generator)
        if isinstance(tmp_func, str):
            tmp_func = getattr(jump_val, tmp_func)
            tmp_func = Logger.log_func("data_pipeline")(tmp_func)
            res = tmp_func(*cur.args, **cur.kwargs)
        else:
            tmp_func = Logger.log_func("data_pipeline")(tmp_func)
            res = tmp_func(jump_val, *cur.args, **cur.kwargs)
        if cur.is_leaf:
            if cur.output_name:
                self.env[cur.output_name] = res
            return jump_val
        return res

    @staticmethod
    def pipeline(__df: pd.DataFrame, pipeline: Any) -> pd.DataFrame:
        """Wrap chain function to a DataFrame using a generator to apply multiple
        functions and theirs arguments in chain.

        Args:
            __df (pd.DataFrame): DataFrame that will be piped.
            pipeline (Any): DataPipeline instance.

        Returns:
            pd.DataFrame: Returns original DataFrame to keep chaining.
        """
        return pipeline(__df)
