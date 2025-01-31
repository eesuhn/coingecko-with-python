from typing import (
    Optional,
)

from .enums import SortTopPoolsByTokenAddress
from .endpoints import Endpoints


class Onchain(Endpoints):
    def token_data_by_token_address(
        self,
        network: str,
        token_address: str,
        top_pools: bool = False
    ) -> dict:
        """
        Query specific token data based on the provided token contract address on a network
        Ref: https://docs.coingecko.com/reference/token-data-contract-address
        """

        endpoint = f"/onchain/networks/{network}/tokens/{token_address}"
        query_params = {
            "include": super().handle_include_params(
                top_pools=top_pools
            )
        }
        return super().make_request(
            endpoint=endpoint,
            query_params=query_params
        )

    def top_pools_by_token_address(
        self,
        network: str,
        token_address: str,
        base_token: bool = False,
        quote_token: bool = False,
        dex: bool = False,
        page: int = 1,
        sort: Optional[SortTopPoolsByTokenAddress] = None
    ) -> dict:
        """
        Query top pools based on the provided token contract address on a network
        Ref: https://docs.coingecko.com/reference/top-pools-contract-address
        """

        endpoint = f"/onchain/networks/{network}/tokens/{token_address}/pools"
        query_params = {
            "include": super().handle_include_params(
                base_token=base_token,
                quote_token=quote_token,
                dex=dex
            ),
            "page": page,
            "sort": sort.value if sort else None
        }
        return super().make_request(
            endpoint=endpoint,
            query_params=query_params
        )
