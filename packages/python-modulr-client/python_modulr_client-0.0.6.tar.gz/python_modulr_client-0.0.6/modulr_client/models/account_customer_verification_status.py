from enum import Enum


class AccountCustomerVerificationStatus(str, Enum):
    EXVERIFIED = "EXVERIFIED"
    UNVERIFIED = "UNVERIFIED"
    VERIFIED = "VERIFIED"
    REFERRED = "REFERRED"
    DECLINED = "DECLINED"
    MIGRATED = "MIGRATED"
    REVIEWED = "REVIEWED"

    def __str__(self) -> str:
        return str(self.value)
