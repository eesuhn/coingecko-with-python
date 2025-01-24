from ._constants import SECRET_KEY

from typing import Any


class Main:
    def __init__(self, *argv: Any) -> None:
        self.args = set(argv[1:])
        print(self.args)
        print(SECRET_KEY)
