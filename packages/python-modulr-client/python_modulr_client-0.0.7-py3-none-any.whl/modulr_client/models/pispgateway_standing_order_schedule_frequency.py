from enum import Enum


class PispgatewayStandingOrderScheduleFrequency(str, Enum):
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"

    def __str__(self) -> str:
        return str(self.value)
