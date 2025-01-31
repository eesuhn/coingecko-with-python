from .gui import GUI
from ..playground import PlayCoins


class GUICoins(GUI):
    def __init__(self) -> None:
        self.playground = PlayCoins()
        super().__init__(
            callback=self.playground.gui_callback
        )
