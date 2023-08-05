from enum import Enum


class GetCardActivitiesStatuses(str, Enum):
    APPROVED = "APPROVED"
    EXPIRED = "EXPIRED"
    DECLINED = "DECLINED"
    SETTLED = "SETTLED"

    def __str__(self) -> str:
        return str(self.value)
