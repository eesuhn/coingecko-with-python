from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QGroupBox,
    QLineEdit,
    QLabel,
    QCheckBox
)
from typing import Callable, Union


class GUI(QWidget):
    def __init__(
        self,
        callback: Callable
    ):
        super().__init__()
        self.callback = callback
        self._init_ui()

    def _init_ui(self) -> None:
        """
        Initialize the main GUI layout
        """
        layout = QVBoxLayout()

        # Inputs
        self.inputs_layout = QVBoxLayout()

        # Run options
        run_methods_group = QGroupBox()
        self.run_methods_layout = QVBoxLayout()
        run_methods_group.setLayout(self.run_methods_layout)

        # Output options
        output_options_group = QGroupBox()
        self.output_options_layout = QVBoxLayout()
        output_options_group.setLayout(self.output_options_layout)

        # Submit button
        self.submit_btn = QPushButton("Submit")
        self.submit_btn.clicked.connect(self.callback)

        self.init_inputs()
        self.init_run_options()
        self.init_options()

        layout.addLayout(self.inputs_layout)
        layout.addWidget(run_methods_group)
        layout.addWidget(output_options_group)
        layout.addSpacing(10)
        layout.addWidget(self.submit_btn)

        super().setLayout(layout)
        super().setWindowTitle("CoinGecko Playground")
        super().setMinimumWidth(400)

    def init_inputs(self) -> None:
        """
        Override this method to add inputs
        """
        pass

    def init_run_options(self) -> None:
        """
        Override this method to add run options
        """
        for method in self.playground.get_run_methods():
            display_name = method.replace('_run_', '')
            checkbox = self.add_option(
                label=display_name,
                default=True,
                parent=self.run_methods_layout
            )
            self.playground.run_method_checkboxes[method] = checkbox

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
        self.inputs_layout.addSpacing(10)

        return input_field

    def add_option(
        self,
        label: str,
        default: bool = False,
        parent: Union[QVBoxLayout, None] = None
    ) -> QCheckBox:
        """
        Add an option to GUI
        If parent is not specified, adds to `output_options_layout`
        """

        option = QCheckBox(label)
        option.setChecked(default)

        if parent is None:
            parent = self.output_options_layout

        parent.addWidget(option)

        return option
