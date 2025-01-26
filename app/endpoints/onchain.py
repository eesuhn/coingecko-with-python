from typing import Union

from .enums import SortTopPoolsByTokenAddress
from .endpoints import Endpoints


class Onchain(Endpoints):
    def token_data_by_token_address(
        self,
        network: str,
        token_address: str,
        top_pools: bool = False
    ) -> dict:
        endpoint = f"/onchain/networks/{network}/tokens/{token_address}"
        if top_pools:
            endpoint += "?include=top_pools"
        return super().cg_request(endpoint)

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
        if sort:
            endpoint += f"?sort={sort.value}"
        return super().cg_request(endpoint)
