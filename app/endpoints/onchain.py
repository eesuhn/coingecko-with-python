from ..utils import cg_request


class Onchain:
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
