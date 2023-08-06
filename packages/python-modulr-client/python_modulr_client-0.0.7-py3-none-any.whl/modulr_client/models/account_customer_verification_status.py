from enum import Enum


class AccountCustomerVerificationStatus(str, Enum):
    UNVERIFIED = "UNVERIFIED"
    VERIFIED = "VERIFIED"
    EXVERIFIED = "EXVERIFIED"
    REFERRED = "REFERRED"
    DECLINED = "DECLINED"
    REVIEWED = "REVIEWED"
    MIGRATED = "MIGRATED"

    def __str__(self) -> str:
        return str(self.value)
