import json
import requests

from pathlib import Path
from datetime import datetime
from ._constants import CG_API_KEY


def get_package_root() -> Path:
    return Path(__file__).parent


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


def log_json(
    d: dict,
    filename: str,
    prod_filename: bool = False,
    extension: str = "json",
    dest: str = "logs"
) -> None:
    """
    Log JSON response to a file
    """
    path = get_package_root() / dest
    path.mkdir(exist_ok=True)
    if prod_filename:
        filename = generate_filename(filename)
    with open(path / f"{filename}.{extension}", "w", encoding="utf-8") as f:
        f.write(json.dumps(d, indent=2))
    print(f"Logged {extension} response to {dest}/{filename}.{extension}'")


def generate_filename(
    func_name: str
) -> str:
    """
    Generate filename based on the called function name and timestamp
    """
    return f"{func_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
