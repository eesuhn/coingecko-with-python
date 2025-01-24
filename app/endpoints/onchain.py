from typing import Union
from enum import Enum

from ..utils import cg_request


class Onchain:
    class SortTopPoolsByTokenAddress(Enum):
        H24_VOLUME_USD_LIQUIDITY_DESC = "h24_volume_usd_liquidity_desc"
        H24_TX_COUNT_DESC = "h24_tx_count_desc"
        H24_VOLUME_USD_DESC = "h24_volume_usd_desc"

    def token_data_by_token_address(
        self,
        network: str,
        token_address: str,
        top_pools: bool = False
    ) -> dict:
        endpoint = f"/onchain/networks/{network}/tokens/{token_address}"
        if top_pools:
            endpoint += "?include=top_pools"
        return cg_request(endpoint)

    def top_pools_by_token_address(
        self,
        network: str,
        token_address: str,
        base_token: bool = False,
        quote_token: bool = False,
        dex: bool = False,
        page: int = 1,
        sort: Union[SortTopPoolsByTokenAddress, None] = None,
    ) -> dict:
        endpoint = f"/onchain/networks/{network}/tokens/{token_address}/pools"
        if base_token or quote_token or dex:
            endpoint += "?include="
            if base_token:
                endpoint += "base_token%2C"
            if quote_token:
                endpoint += "quote_token%2C"
            if dex:
                endpoint += "dex%2C"
            endpoint = endpoint[:-3]
        if page:
            endpoint += f"?page={page}"
            print(endpoint)
        if sort:
            endpoint += f"?sort={sort.value}"
        return cg_request(endpoint)
