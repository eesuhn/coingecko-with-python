import sys

from PyQt5.QtWidgets import QApplication

from .gui import (
    GUIOnchain,
    GUICoins
)


class Main:
    def __init__(self) -> None:
        if 'gui' in sys.argv:
            self._run_gui()

    def _run_gui(self) -> None:
        app = QApplication(sys.argv)

        if 'onchain' in sys.argv:
            gui = GUIOnchain()
        elif 'coins' in sys.argv:
            gui = GUICoins()
        else:
            return

        gui.show()
        sys.exit(app.exec_())
