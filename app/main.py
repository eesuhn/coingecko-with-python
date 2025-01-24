from typing import Any

from .playground import PlayOnchain


class Main:
    def __init__(self, *argv: Any) -> None:
        args = set(argv[1:])
        self.play_onchain = PlayOnchain(
            console_print="print" in args,
            console_log="log" in args
        )
        if "onchain" in args:
            self.play_onchain.run()
