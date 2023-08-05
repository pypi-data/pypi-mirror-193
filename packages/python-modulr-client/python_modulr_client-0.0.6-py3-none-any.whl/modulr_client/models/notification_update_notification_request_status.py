from enum import Enum


class NotificationUpdateNotificationRequestStatus(str, Enum):
    INACTIVE = "INACTIVE"
    ACTIVE = "ACTIVE"

    def __str__(self) -> str:
        return str(self.value)
