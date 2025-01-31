import re
from concurrent.futures import ThreadPoolExecutor, as_completed

from PyQt5.QtWidgets import QLineEdit
from typing import Any

from .playground import Playground
from ..endpoints import Coins
from ..utils import log_func_name


class PlayCoins(Playground):
    coin_id: str
    coin_id_input: QLineEdit

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

    @Playground.run_wrapper
    def _run_coin_data_by_id(self) -> None:
        response = self.coins.coin_data_by_id(
            coin_id=self.coin_id
        )
        super().handle_run(
            response=response,
            func_name=log_func_name()
        )

    @Playground.run_wrapper
    def _run_clean_up_coin_desc(self) -> None:
        res_coins_list = self.coins.coins_list()
        coin_ids = [coin['id'] for coin in res_coins_list]

        coin_id_desc = {}

        # Threaded requests
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_coin = {
                executor.submit(self._coin_en_desc_by_id, coin_id): coin_id
                for coin_id in coin_ids
            }

            for future in as_completed(future_to_coin):
                coin_id = future_to_coin[future]
                try:
                    response = future.result()
                    coin_id_desc[coin_id] = response.get('description', "NULL")
                except Exception as e:
                    coin_id_desc[coin_id] = f"Error: {str(e)}"

        super().handle_run(
            response=coin_id_desc,
            func_name=log_func_name()
        )

    def _clean_html_tags(self, text: str) -> str:
        """
        Remove HTML tags from text
        """

        if not text:
            return text

        # Replace <a href="...">text</a> with just the text
        text = re.sub(r'<a href="[^"]*">([^<]*)</a>', r'\1', text)

        # Remove any other remaining HTML tags
        text = re.sub(r'<[^>]+>', '', text)

        # Convert HTML entities
        text = text.replace('&nbsp;', ' ')
        text = text.replace('&amp;', '&')
        text = text.replace('&lt;', '<')
        text = text.replace('&gt;', '>')

        return text

    def _coin_en_desc_by_id(self, coin_id: str) -> dict:
        """
        Get only `en` description of the coin
        """

        response = self.coins.coin_data_by_id(
            coin_id=coin_id,
            localization=False,
            tickers=False,
            market_data=False,
            community_data=False,
            developer_data=False
        )

        if 'description' in response:
            response['description'] = self._clean_html_tags(response['description']['en'])

        return response

    def gui_callback(self) -> None:
        self.coin_id = self.coin_id_input.text()

        Playground.gui_callback(self)
