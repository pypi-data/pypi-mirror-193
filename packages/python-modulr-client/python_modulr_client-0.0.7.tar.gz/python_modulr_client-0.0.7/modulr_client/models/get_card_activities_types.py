from enum import Enum


class GetCardActivitiesTypes(str, Enum):
    AUTHORISATION = "AUTHORISATION"
    REVERSAL = "REVERSAL"
    SETTLEMENT = "SETTLEMENT"
    REFUND = "REFUND"

    def __str__(self) -> str:
        return str(self.value)
