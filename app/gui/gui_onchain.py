from PyQt5.QtWidgets import (
    QLineEdit,
    QVBoxLayout,
    QCheckBox,
    QLabel
)

from .gui import GUI
from ..playground import PlayOnchain


class GUIOnchain(GUI):
    network_input_default = "eth"
    token_address_input_default = "0xdac17f958d2ee523a2206206994597c13d831ec7"

    def __init__(
        self,
        playground: PlayOnchain
    ):
        self.playground = playground
        super().__init__(
            callback=playground.gui_callback
        )

    def init_inputs(self) -> None:
        network_label = QLabel("Network")
        self.network_input = QLineEdit()
        self.network_input.setText(self.network_input_default)

        token_address_label = QLabel("Token Address")
        self.token_address_input = QLineEdit()
        self.token_address_input.setText(self.token_address_input_default)

        self.inputs_layout.addWidget(network_label)
        self.inputs_layout.addWidget(self.network_input)
        self.inputs_layout.addWidget(token_address_label)
        self.inputs_layout.addWidget(self.token_address_input)

        # Link inputs to playground instance
        self.playground.network_input = self.network_input
        self.playground.token_address_input = self.token_address_input

    def init_options(self) -> None:
        output_options_layout = QVBoxLayout()

        self.print_checkbox = QCheckBox("Print to Console")
        self.print_checkbox.setChecked(False)
        self.log_checkbox = QCheckBox("Log to File")
        self.log_checkbox.setChecked(False)

        output_options_layout.addWidget(self.print_checkbox)
        output_options_layout.addWidget(self.log_checkbox)
        self.output_options_group.setLayout(output_options_layout)

        # Link checkboxes to playground instance
        self.playground.print_checkbox = self.print_checkbox
        self.playground.log_checkbox = self.log_checkbox
