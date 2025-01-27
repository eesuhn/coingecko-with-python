from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
)
from typing import Callable


class GUI(QWidget):
    network_input_default = "eth"
    token_address_input_default = "0xdac17f958d2ee523a2206206994597c13d831ec7"

    def __init__(
        self,
        callback: Callable
    ):
        super().__init__()
        self.callback = callback
        self._init_ui()

    def _init_ui(self) -> None:
        layout = QVBoxLayout()
        self.form_layout = QFormLayout()

        self._init_inputs()

        layout.addLayout(self.form_layout)
        super().setLayout(layout)
        self.setWindowTitle("CoinGecko Playground")

    def _init_inputs(self) -> None:
        self.network_input = QLineEdit()
        self.network_input.setText(self.network_input_default)
        self.form_layout.addRow("Network", self.network_input)

        self.token_address_input = QLineEdit()
        self.token_address_input.setText(self.token_address_input_default)
        self.form_layout.addRow("Token Address", self.token_address_input)
