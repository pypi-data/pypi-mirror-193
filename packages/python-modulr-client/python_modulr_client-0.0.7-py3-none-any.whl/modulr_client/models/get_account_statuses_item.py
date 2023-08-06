from enum import Enum


class GetAccountStatusesItem(str, Enum):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
    CLOSED = "CLOSED"
    CLIENT_BLOCKED = "CLIENT_BLOCKED"

    def __str__(self) -> str:
        return str(self.value)
