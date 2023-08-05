from enum import Enum


class NotificationNotificationConfigDaysToRunItem(str, Enum):
    WEDNESDAY = "WEDNESDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    TUESDAY = "TUESDAY"
    THURSDAY = "THURSDAY"
    SUNDAY = "SUNDAY"
    MONDAY = "MONDAY"

    def __str__(self) -> str:
        return str(self.value)
