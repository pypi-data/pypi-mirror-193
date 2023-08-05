from enum import Enum


class NotificationNotificationRequestChannel(str, Enum):
    WEBHOOK = "WEBHOOK"
    EMAIL = "EMAIL"

    def __str__(self) -> str:
        return str(self.value)
