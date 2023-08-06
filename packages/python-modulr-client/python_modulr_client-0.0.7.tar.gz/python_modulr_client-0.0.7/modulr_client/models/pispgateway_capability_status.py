from enum import Enum


class PispgatewayCapabilityStatus(str, Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    INACTIVE = "INACTIVE"

    def __str__(self) -> str:
        return str(self.value)
