from .endpoints import Onchain
from .utils import print_json, log_json

from typing import Any


class Main:
    def __init__(self, *argv: Any) -> None:
        self.args = set(argv[1:])
        if "--onchain" in self.args:
            self._run_onchain()

    def _run_onchain(self) -> None:
        self.network = "avax"
        self.token_address = "0x2b2c81e08f1af8835a78bb2a90ae924ace0ea4be"
        self.onchain = Onchain()

        self._run_onchain_token_data_by_token_address()
        self._run_onchain_top_pools_by_token_address()

    def _run_onchain_token_data_by_token_address(self) -> None:
        res_onchain_token_data_by_token_address = self.onchain.token_data_by_token_address(
            network=self.network,
            token_address=self.token_address,
            top_pools=True
        )
        print_json(res_onchain_token_data_by_token_address)
        log_json(
            res_onchain_token_data_by_token_address,
            "onchain_token_data_by_token_address",
            prod_filename=True
        )

    def _run_onchain_top_pools_by_token_address(self) -> None:
        res_onchain_top_pools_by_token_address = self.onchain.top_pools_by_token_address(
            network=self.network,
            token_address=self.token_address,
        )
        print_json(res_onchain_top_pools_by_token_address)
        log_json(
            res_onchain_top_pools_by_token_address,
            "onchain_top_pools_by_token_address",
            prod_filename=True
        )
