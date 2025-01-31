from PyQt5.QtWidgets import QLineEdit
from typing import Any

from .playground import Playground
from ..endpoints import Coins
from ..utils import log_func_name


class PlayCoins(Playground):
    coin_id: str
    coin_id_input: QLineEdit

    def __init__(
        self,
        **kwargs: Any
    ):
        super().__init__(**kwargs)
        self.coins = Coins()

    @Playground.run_wrapper
    def _run_coins_list(self) -> None:
        response = self.coins.coins_list()
        super().handle_run(
            response=response,
            func_name=log_func_name()
        )

    @Playground.run_wrapper
    def _run_coin_data_by_id(self) -> None:
        response = self.coins.coin_data_by_id(
            coin_id=self.coin_id
        )
        super().handle_run(
            response=response,
            func_name=log_func_name()
        )

    def gui_callback(self) -> None:
        self.coin_id = self.coin_id_input.text()

        Playground.gui_callback(self)
