from enum import Enum


class GetCardActivitiesStatuses(str, Enum):
    DECLINED = "DECLINED"
    APPROVED = "APPROVED"
    SETTLED = "SETTLED"
    EXPIRED = "EXPIRED"

    def __str__(self) -> str:
        return str(self.value)
