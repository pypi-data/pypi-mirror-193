from enum import Enum


class RuleCreateRuleRequestType(str, Enum):
    SPLIT = "SPLIT"
    FUNDING = "FUNDING"
    SWEEP = "SWEEP"

    def __str__(self) -> str:
        return str(self.value)
