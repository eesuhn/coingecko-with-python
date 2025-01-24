from typing import Any

from .play import Play
from ..utils import log_func_name
from ..endpoints import Onchain


class PlayOnchain(Play):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.onchain = Onchain()
        self.network = "avax"
        self.token_address = "0x2b2c81e08f1af8835a78bb2a90ae924ace0ea4be"

    def run(self) -> None:
        self._run_onchain_token_data_by_token_address()
        self._run_onchain_top_pools_by_token_address()

    def _run_onchain_token_data_by_token_address(self) -> None:
        res_onchain_token_data_by_token_address = self.onchain.token_data_by_token_address(
            network=self.network,
            token_address=self.token_address
        )
        super().if_console(
            res_onchain_token_data_by_token_address,
            log_func_name()
        )

    def _run_onchain_top_pools_by_token_address(self) -> None:
        res_onchain_top_pools_by_token_address = self.onchain.top_pools_by_token_address(
            network=self.network,
            token_address=self.token_address,
        )
        super().if_console(
            res_onchain_top_pools_by_token_address,
            log_func_name()
        )

    def _pool_address_by_token_address(self, d: dict) -> list[str]:
        return [pool["attributes"]["address"] for pool in d["data"]]

    def _gt_url_from_pool_address(
        self,
        pool_address: str,
        network: str,
    ) -> str:
        return f"https://www.geckoterminal.com/{network}/pools/{pool_address}"
