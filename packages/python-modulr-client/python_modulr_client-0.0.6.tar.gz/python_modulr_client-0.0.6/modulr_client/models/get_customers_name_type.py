from enum import Enum


class GetCustomersNameType(str, Enum):
    SUFFIX = "SUFFIX"
    WORD_MATCH = "WORD_MATCH"
    CONTAINS = "CONTAINS"
    PREFIX = "PREFIX"
    EXACT = "EXACT"
    WORD_MATCH_ALPHANUMERIC = "WORD_MATCH_ALPHANUMERIC"

    def __str__(self) -> str:
        return str(self.value)
