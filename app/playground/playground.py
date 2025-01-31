import inspect

from PyQt5.QtWidgets import QCheckBox
from typing import Any, Callable, Dict
from functools import wraps

from ..utils import print_json, log_json


class Playground:
    console_print: bool
    console_log: bool
    func_list: list[str]
    run_method_checkboxes: Dict[str, QCheckBox]
    print_checkbox: QCheckBox
    log_checkbox: QCheckBox

    def __init__(
        self,
        **kwargs: Any
    ):
        for k, v in kwargs.items():
            setattr(self, k, v)
        self._register_run_methods()
        self.run_method_checkboxes = {}

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
        """
        - Methods marked as `run_wrapper` will be registered
        - If `console_print` or `console_log` is True, the method will be executed
        """

        @wraps(func)
        def wrapper(self: 'Playground', *args: Any, **kwargs: Any) -> Any:
            if not (self.console_print or self.console_log):
                return None
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

        TODO: Handle error response
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
        """
        - Link console options
        - Register all method checkboxes for `func_list`

        Override this method to handle GUI submit button
        """
        self.console_print = self.print_checkbox.isChecked()
        self.console_log = self.log_checkbox.isChecked()

        for func_name in self.get_run_methods():
            if self.run_method_checkboxes[func_name].isChecked():
                getattr(self, func_name)()
