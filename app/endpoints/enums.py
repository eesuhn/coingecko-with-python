from enum import Enum


class SortTopPoolsByTokenAddress(Enum):
    H24_VOLUME_USD_LIQUIDITY_DESC = "h24_volume_usd_liquidity_desc"
    H24_TX_COUNT_DESC = "h24_tx_count_desc"
    H24_VOLUME_USD_DESC = "h24_volume_usd_desc"


class StatusCoinsList(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
