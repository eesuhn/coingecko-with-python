from PyQt5.QtWidgets import (
    QLineEdit,
)

from typing import Any

from .playground import Playground
from ..endpoints import Onchain
from ..utils import log_func_name


class PlayOnchain(Playground):
    network: str
    token_address: str
    network_input: QLineEdit
    token_address_input: QLineEdit

    def __init__(
        self,
        **kwargs: Any
    ):
        self.console_print = False
        self.console_log = False

        super().__init__(**kwargs)
        self.onchain = Onchain()

    @Playground.run_wrapper
    def _run_token_data_by_token_address(self) -> None:
        if not self.network or not self.token_address:
            print("(network, token_address) are required")
            return

        response = self.onchain.token_data_by_token_address(
            network=self.network,
            token_address=self.token_address
        )
        super().handle_run(
            response=response,
            func_name=log_func_name()
        )

    @Playground.run_wrapper
    def _run_top_pools_by_token_address(self) -> None:
        if not self.network or not self.token_address:
            print("(network, token_address) are required")
            return

        response = self.onchain.top_pools_by_token_address(
            network=self.network,
            token_address=self.token_address
        )
        super().handle_run(
            response=response,
            func_name=log_func_name()
        )

    def gui_callback(self) -> None:
        self.network = self.network_input.text()
        self.token_address = self.token_address_input.text()

        for func_name in self.get_run_methods():
            getattr(self, func_name)()
