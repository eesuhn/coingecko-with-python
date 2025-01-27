import inspect

from typing import Any, Callable
from functools import wraps

from ..utils import print_json, log_json


class Playground:
    console_print: bool
    console_log: bool
    func_list: list[str]

    def __init__(
        self,
        **kwargs: Any
    ):
        for k, v in kwargs.items():
            setattr(self, k, v)
        self._register_run_methods()

    def _register_run_methods(self) -> None:
        """
        Register all methods with `@Playground.run_wrapper`
        """

        self.func_list = []
        for name, method in inspect.getmembers(self, inspect.ismethod):

            # Run only methods with `@Playground.run_wrapper`
            if hasattr(method, 'is_run_wrapper'):
                self.func_list.append(name)

    @staticmethod
    def run_wrapper(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self: 'Playground', *args: Any, **kwargs: Any) -> Any:
            return func(self, *args, **kwargs)

        # Mark the method as `run_wrapper`
        setattr(wrapper, 'is_run_wrapper', True)
        return wrapper

    def handle_run(
        self,
        response: dict,
        func_name: str
    ) -> None:
        """
        Handle response from `_run` methods
        """

        if self.console_print:
            print_json(response)
        if self.console_log:
            log_json(
                d=response,
                filename=func_name,
                prod_filename=True
            )

    def get_run_methods(self) -> list[str]:
        return self.func_list

    def gui_callback(self) -> None:
        pass
