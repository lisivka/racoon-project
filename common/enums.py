from enum import StrEnum, auto


class LotStatus(StrEnum):
    DRAFT = auto()
    ACTIVE = auto()
    SOLD = auto()


class AuctionStatus(StrEnum):
    PENDING = auto()
    OPEN = auto()
    CLOSED = auto()
    CANCELLED = auto()
