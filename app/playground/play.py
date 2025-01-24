from typing import Any

from ..utils import print_json, log_json


class Play:
    console_print: bool
    console_log: bool

    def __init__(self, **kwargs: Any):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def if_console(
        self,
        res: dict,
        func_name: str
    ) -> None:
        if self.console_print:
            print_json(res)
        if self.console_log:
            log_json(
                res,
                func_name,
                prod_filename=True
            )
