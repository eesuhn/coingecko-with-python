from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QGroupBox,
    QLineEdit,
    QLabel,
    QCheckBox
)
from typing import Callable


class GUI(QWidget):
    def __init__(
        self,
        callback: Callable
    ):
        super().__init__()
        self.callback = callback
        self._init_ui()

    def _init_ui(self) -> None:
        layout = QVBoxLayout()

        # Inputs
        self.inputs_layout = QVBoxLayout()

        # Output options
        self.output_options_group = QGroupBox()
        self.output_options_layout = QVBoxLayout()
        self.output_options_group.setLayout(self.output_options_layout)

        # Submit button
        self.submit_btn = QPushButton("Submit")
        self.submit_btn.clicked.connect(self.callback)

        self.init_inputs()
        self.init_options()

        layout.addLayout(self.inputs_layout)
        layout.addSpacing(10)
        layout.addWidget(self.output_options_group)
        layout.addSpacing(10)
        layout.addWidget(self.submit_btn)

        super().setLayout(layout)
        self.setWindowTitle("CoinGecko Playground")

    def init_inputs(self) -> None:
        """
        Override this method to add inputs
        """
        pass

    def init_options(self) -> None:
        """
        Override this method to add options
        """
        pass

    def add_input(
        self,
        label: str,
        default: str = ""
    ) -> QLineEdit:
        """
        Add an input field to GUI `inputs_layout`
        """

        input_label = QLabel(label)
        input_field = QLineEdit()
        input_field.setText(default)

        self.inputs_layout.addWidget(input_label)
        self.inputs_layout.addWidget(input_field)

        return input_field

    def add_option(
        self,
        label: str,
        default: bool = False
    ) -> QCheckBox:
        """
        Add an option to GUI `output_options_layout`
        """

        option = QCheckBox(label)
        option.setChecked(default)

        self.output_options_layout.addWidget(option)

        return option
