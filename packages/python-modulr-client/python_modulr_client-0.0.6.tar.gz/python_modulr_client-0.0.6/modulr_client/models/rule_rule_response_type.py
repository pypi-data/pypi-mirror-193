from enum import Enum


class RuleRuleResponseType(str, Enum):
    SPLIT = "SPLIT"
    FUNDING = "FUNDING"
    SWEEP = "SWEEP"

    def __str__(self) -> str:
        return str(self.value)
