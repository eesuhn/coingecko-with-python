from .gui import GUI
from ..playground import PlayCoins


class GUICoins(GUI):
    coin_id_input_default = "bitcoin"

    def __init__(self) -> None:
        self.playground = PlayCoins()
        super().__init__(
            callback=self.playground.gui_callback
        )

    def init_inputs(self) -> None:
        self.playground.coin_id_input = super().add_input(
            label="ID",
            default=self.coin_id_input_default
        )
