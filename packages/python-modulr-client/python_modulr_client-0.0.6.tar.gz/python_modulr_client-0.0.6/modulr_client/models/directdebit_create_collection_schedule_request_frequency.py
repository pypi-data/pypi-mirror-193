from enum import Enum


class DirectdebitCreateCollectionScheduleRequestFrequency(str, Enum):
    MONTHLY = "MONTHLY"
    ANNUALLY = "ANNUALLY"
    EVERY_TWO_WEEKS = "EVERY_TWO_WEEKS"
    EVERY_FOUR_WEEKS = "EVERY_FOUR_WEEKS"
    ONCE = "ONCE"
    SEMI_ANNUALLY = "SEMI_ANNUALLY"
    WEEKLY = "WEEKLY"
    QUARTERLY = "QUARTERLY"

    def __str__(self) -> str:
        return str(self.value)
