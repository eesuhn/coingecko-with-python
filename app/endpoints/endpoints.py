import requests

from ._constants import CG_API_KEY


class Endpoints:
    def cg_request(
        self,
        endpoint: str,
        base_url: str = "https://pro-api.coingecko.com/api/v3",
        timeout: int = 10
    ) -> dict:
        url = f"{base_url}/{endpoint}"
        headers = {
            "accept": "application/json",
            "x-cg-pro-api-key": CG_API_KEY
        }
        response = requests.get(url=url, headers=headers, timeout=timeout)
        return response.json()
