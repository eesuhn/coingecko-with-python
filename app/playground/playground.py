from typing import Any

from ..utils import print_json, log_json


class Playground:
    console_print: bool
    console_log: bool

    def __init__(
        self,
        **kwargs: Any
    ):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def if_console(
        self,
        response: dict,
        func_name: str
    ) -> None:
        """
        Handle console arguments
        """

        if self.console_print:
            print_json(response)
        if self.console_log:
            log_json(
                d=response,
                filename=func_name,
                prod_filename=True
            )
