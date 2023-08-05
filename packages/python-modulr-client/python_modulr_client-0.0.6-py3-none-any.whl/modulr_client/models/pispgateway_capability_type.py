from enum import Enum


class PispgatewayCapabilityType(str, Enum):
    STANDING_ORDER = "STANDING_ORDER"
    SINGLE_IMMEDIATE = "SINGLE_IMMEDIATE"

    def __str__(self) -> str:
        return str(self.value)
