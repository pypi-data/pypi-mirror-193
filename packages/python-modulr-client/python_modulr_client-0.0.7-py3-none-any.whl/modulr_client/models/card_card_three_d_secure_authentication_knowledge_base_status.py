from enum import Enum


class CardCardThreeDSecureAuthenticationKnowledgeBaseStatus(str, Enum):
    NOT_ENROLLED = "NOT_ENROLLED"
    ENROLLED = "ENROLLED"
    UNENROLLED = "UNENROLLED"

    def __str__(self) -> str:
        return str(self.value)
