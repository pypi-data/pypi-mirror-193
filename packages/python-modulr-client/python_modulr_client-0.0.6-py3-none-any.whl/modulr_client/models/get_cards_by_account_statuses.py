from enum import Enum


class GetCardsByAccountStatuses(str, Enum):
    SUSPENDED = "SUSPENDED"
    EXPIRED = "EXPIRED"
    BLOCKED = "BLOCKED"
    ACTIVE = "ACTIVE"
    CREATED = "CREATED"
    CANCELLED = "CANCELLED"

    def __str__(self) -> str:
        return str(self.value)
