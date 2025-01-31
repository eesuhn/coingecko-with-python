from .endpoints import Endpoints
from .enums import StatusCoinsList


class Coins(Endpoints):
    def coins_list(
        self,
        include_platform: bool = False,
        status: StatusCoinsList = StatusCoinsList.ACTIVE
    ) -> dict:
        """
        Query all the supported coins on CoinGecko with coins id, name and symbol
        Ref: https://docs.coingecko.com/reference/coins-list
        """

        endpoint = "/coins/list"
        query_params = {
            "include": super().handle_include_params(
                include_platform=include_platform,
                status=status.value
            )
        }
        return super().make_request(
            endpoint=endpoint,
            query_params=query_params
        )
