from PyQt5.QtWidgets import (
    QLineEdit,
    QCheckBox,
)

from typing import Any, Dict

from .playground import Playground
from ..endpoints import Onchain
from ..utils import log_func_name


class PlayOnchain(Playground):
    network: str
    token_address: str
    network_input: QLineEdit
    token_address_input: QLineEdit
    print_checkbox: QCheckBox
    log_checkbox: QCheckBox
    run_method_checkboxes: Dict[str, QCheckBox]

    def __init__(
        self,
        **kwargs: Any
    ):
        super().__init__(**kwargs)
        self.onchain = Onchain()
        self.run_method_checkboxes = {}

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

        self.console_print = self.print_checkbox.isChecked()
        self.console_log = self.log_checkbox.isChecked()

        for func_name in self.get_run_methods():
            if self.run_method_checkboxes[func_name].isChecked():
                getattr(self, func_name)()
