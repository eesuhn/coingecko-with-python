import json
import requests

from ._constants import CG_API_KEY


def cg_request(
    endpoint: str,
    base_url: str = "https://pro-api.coingecko.com/api/v3"
) -> dict:
    url = f"{base_url}/{endpoint}"
    headers = {
        "accept": "application/json",
        "x-cg-pro-api-key": CG_API_KEY
    }
    response = requests.get(url, headers=headers, timeout=10)
    return response.json()


def print_json(d: dict) -> None:
    """
    Print N nested JSON response with Prettier format
    """
    print(json.dumps(d, indent=2))
