from enum import Enum


class NotificationNotificationResponseStatus(str, Enum):
    INACTIVE = "INACTIVE"
    ACTIVE = "ACTIVE"

    def __str__(self) -> str:
        return str(self.value)
