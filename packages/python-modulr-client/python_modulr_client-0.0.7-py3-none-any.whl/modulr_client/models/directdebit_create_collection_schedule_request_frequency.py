from enum import Enum


class DirectdebitCreateCollectionScheduleRequestFrequency(str, Enum):
    ONCE = "ONCE"
    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    SEMI_ANNUALLY = "SEMI_ANNUALLY"
    ANNUALLY = "ANNUALLY"
    WEEKLY = "WEEKLY"
    EVERY_TWO_WEEKS = "EVERY_TWO_WEEKS"
    EVERY_FOUR_WEEKS = "EVERY_FOUR_WEEKS"

    def __str__(self) -> str:
        return str(self.value)
