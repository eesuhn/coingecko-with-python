from .endpoints import Onchain
from .utils import print_json, log_json

from typing import Any


class Main:
    def __init__(self, *argv: Any) -> None:
        self.args = set(argv[1:])
        if "--onchain" in self.args:
            self._run_onchain()

    def _run_onchain(self) -> None:
        self.onchain = Onchain()
        response = self.onchain.token_data_by_token_address(
            network="avax",
            token_address="0x2b2c81e08f1af8835a78bb2a90ae924ace0ea4be",
            top_pools=True
        )
        print_json(response)
        # log_json(response, "onchain_token_data_by_token_address", prod_filename=True)
