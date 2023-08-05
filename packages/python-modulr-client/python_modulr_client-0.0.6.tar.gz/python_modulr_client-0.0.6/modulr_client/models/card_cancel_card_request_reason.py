from enum import Enum


class CardCancelCardRequestReason(str, Enum):
    DESTROYED = "DESTROYED"
    STOLEN = "STOLEN"
    LOST = "LOST"

    def __str__(self) -> str:
        return str(self.value)
