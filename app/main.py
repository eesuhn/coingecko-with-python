import sys

from PyQt5.QtWidgets import QApplication

from .gui import (
    GUIOnchain,
    GUICoins
)
from .playground import PlayCoins


class Main:
    def __init__(self) -> None:
        if 'cli' in sys.argv:
            self._run_cli()
        elif 'gui' in sys.argv:
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

    def _run_cli(self) -> None:
        if 'coins' in sys.argv:
            play_coins = PlayCoins()
            if 'clean-desc' in sys.argv:
                play_coins.clean_up_coin_desc()
