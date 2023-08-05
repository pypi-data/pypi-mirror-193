from enum import Enum


class AccountStatusesItem(str, Enum):
    BLOCKED = "BLOCKED"
    ACTIVE = "ACTIVE"
    CLIENT_BLOCKED = "CLIENT_BLOCKED"
    CLOSED = "CLOSED"

    def __str__(self) -> str:
        return str(self.value)
