from enum import Enum


class CardCardResponseStatus(str, Enum):
    CREATED = "CREATED"
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
    SUSPENDED = "SUSPENDED"
    CANCELLED = "CANCELLED"
    EXPIRED = "EXPIRED"

    def __str__(self) -> str:
        return str(self.value)
