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
            "include_platform": include_platform,
            "status": status.value
        }
        return super().make_request(
            endpoint=endpoint,
            query_params=query_params
        )

    def coin_data_by_id(
        self,
        coin_id: str,
        localization: bool = True,
        tickers: bool = True,
        market_data: bool = True,
        community_data: bool = True,
        developer_data: bool = True,
        sparkline: bool = False
    ) -> dict:
        """
        Query all the coin data of a coin (name, price, market .... including exchange tickers) on CoinGecko coin page based on a particular coin id
        Ref: https://docs.coingecko.com/reference/coins-id
        """

        endpoint = f"/coins/{coin_id}"
        query_params = {
            "localization": localization,
            "tickers": tickers,
            "market_data": market_data,
            "community_data": community_data,
            "developer_data": developer_data,
            "sparkline": sparkline
        }
        return super().make_request(
            endpoint=endpoint,
            query_params=query_params
        )
