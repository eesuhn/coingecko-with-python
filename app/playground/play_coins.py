from typing import Any

from .playground import Playground
from ..endpoints import Coins
from ..utils import log_func_name


class PlayCoins(Playground):
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
