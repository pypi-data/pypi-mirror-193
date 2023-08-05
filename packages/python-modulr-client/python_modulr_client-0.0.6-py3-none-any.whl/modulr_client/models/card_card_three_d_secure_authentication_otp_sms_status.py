from enum import Enum


class CardCardThreeDSecureAuthenticationOtpSmsStatus(str, Enum):
    NOT_ENROLLED = "NOT_ENROLLED"
    UNENROLLED = "UNENROLLED"
    ENROLLED = "ENROLLED"

    def __str__(self) -> str:
        return str(self.value)
