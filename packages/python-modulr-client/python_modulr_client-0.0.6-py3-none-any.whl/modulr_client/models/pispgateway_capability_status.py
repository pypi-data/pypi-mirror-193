from enum import Enum


class PispgatewayCapabilityStatus(str, Enum):
    INACTIVE = "INACTIVE"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"

    def __str__(self) -> str:
        return str(self.value)
