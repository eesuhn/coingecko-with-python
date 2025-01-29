from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QGroupBox,
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
        self.inputs_layout = QVBoxLayout()
        self.output_options_group = QGroupBox()
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
