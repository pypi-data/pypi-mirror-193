from enum import Enum


class CardCardReplacementRequestReason(str, Enum):
    STOLEN = "STOLEN"
    DAMAGED = "DAMAGED"
    LOST = "LOST"
    RENEW = "RENEW"

    def __str__(self) -> str:
        return str(self.value)
