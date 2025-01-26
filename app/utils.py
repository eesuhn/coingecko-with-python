import json
import inspect

from datetime import datetime
from pathlib import Path


def get_package_root() -> Path:
    return Path(__file__).parent


def print_json(d: dict) -> None:
    """
    Print JSON response with Prettier format
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
    Log response to specified directory
    """
    path = get_package_root() / dest
    path.mkdir(exist_ok=True)
    if prod_filename:
        filename = generate_filename_by_func_name(filename)
    with open(path / f"{filename}.{extension}", "w", encoding="utf-8") as f:
        f.write(json.dumps(d, indent=2))
    print(f"Logged {extension} response to {dest}/{filename}.{extension}'")


def generate_filename_by_func_name(
    func_name: str
) -> str:
    """
    Generate filename by function name and current datetime
    """
    return f"{func_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"


def log_func_name() -> str:
    return inspect.currentframe().f_back.f_code.co_name
