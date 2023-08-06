from enum import Enum


class CardCardActivityResponseType(str, Enum):
    AUTHORISATION = "AUTHORISATION"
    REVERSAL = "REVERSAL"
    SETTLEMENT = "SETTLEMENT"
    REFUND = "REFUND"

    def __str__(self) -> str:
        return str(self.value)
