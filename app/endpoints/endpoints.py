import requests

from typing import (
    Dict,
    Any,
    Optional,
)
from urllib.parse import urlencode

from ._constants import CG_API_KEY


class Endpoints:
    def cg_request(
        self,
        endpoint: str,
        base_url: str = "https://pro-api.coingecko.com/api/v3",
        timeout: int = 10
    ) -> dict:
        url = f"{base_url}/{endpoint}"

        # TODO: Color this print statement
        print(url)

        headers = {
            "accept": "application/json",
            "x-cg-pro-api-key": CG_API_KEY
        }
        response = requests.get(url=url, headers=headers, timeout=timeout)
        return response.json()

    def _build_query_params(self, **params: Any) -> str:
        """
        Build query string from parameters
        """

        filtered_params = {k: v for k, v in params.items() if v}
        if not filtered_params:
            return ""
        return "?" + urlencode(filtered_params)

    def handle_include_params(self, **params: Any) -> Optional[str]:
        """
        Build include parameter string
        """

        include_parts = [k for k, v in params.items() if v]
        return ",".join(include_parts) if include_parts else None

    def make_request(
        self,
        endpoint: str,
        query_params: Optional[Dict[str, Any]] = None
    ) -> dict:
        """
        Validate and make the API request
        """

        if query_params:
            endpoint += self._build_query_params(**query_params)
        return self.cg_request(endpoint=endpoint)
