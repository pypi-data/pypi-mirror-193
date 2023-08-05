from enum import Enum


class GetCardActivitiesTypes(str, Enum):
    SETTLEMENT = "SETTLEMENT"
    AUTHORISATION = "AUTHORISATION"
    REVERSAL = "REVERSAL"
    REFUND = "REFUND"

    def __str__(self) -> str:
        return str(self.value)
