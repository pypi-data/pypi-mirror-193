from enum import Enum


class CardCardReplacementRequestReason(str, Enum):
    STOLEN = "STOLEN"
    RENEW = "RENEW"
    DAMAGED = "DAMAGED"
    LOST = "LOST"

    def __str__(self) -> str:
        return str(self.value)
