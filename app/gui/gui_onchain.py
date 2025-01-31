from .gui import GUI
from ..playground import PlayOnchain


class GUIOnchain(GUI):
    network_input_default = "eth"
    token_address_input_default = "0xdac17f958d2ee523a2206206994597c13d831ec7"

    def __init__(self) -> None:
        self.playground = PlayOnchain()
        super().__init__(
            callback=self.playground.gui_callback
        )

    def init_inputs(self) -> None:
        self.playground.network_input = super().add_input(
            label="Network",
            default=self.network_input_default
        )
        self.playground.token_address_input = super().add_input(
            label="Token Address",
            default=self.token_address_input_default
        )
