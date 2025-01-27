import sys

from PyQt5.QtWidgets import QApplication

from .playground import PlayOnchain
from .gui import GUI


class Main:
    def __init__(self) -> None:
        if 'gui' in sys.argv:
            self._run_gui()

    def _run_gui(self) -> None:
        app = QApplication(sys.argv)

        if 'onchain' in sys.argv:
            self.play_onchain = PlayOnchain()
            gui = GUI(
                callback=self.play_onchain.gui_callback
            )
        else:
            return

        gui.show()
        sys.exit(app.exec_())
