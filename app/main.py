from typing import Any


class Main:
    def __init__(self, *argv: Any) -> None:
        self.args = set(argv[1:])
