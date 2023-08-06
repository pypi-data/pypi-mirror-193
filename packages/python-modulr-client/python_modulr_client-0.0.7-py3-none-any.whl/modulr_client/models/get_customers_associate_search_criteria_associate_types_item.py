from enum import Enum


class GetCustomersAssociateSearchCriteriaAssociateTypesItem(str, Enum):
    DIRECTOR = "DIRECTOR"
    PARTNER = "PARTNER"
    CSECRETARY = "CSECRETARY"
    SOLETRADER = "SOLETRADER"
    BENE_OWNER = "BENE_OWNER"
    C_INTEREST = "C_INTEREST"
    INDIVIDUAL = "INDIVIDUAL"
    PCM_INDIVIDUAL = "PCM_INDIVIDUAL"
    SIGNATORY = "SIGNATORY"
    TRUST_SETTLOR = "TRUST_SETTLOR"
    TRUST_BENEFICIARY = "TRUST_BENEFICIARY"
    TRUST_TRUSTEE = "TRUST_TRUSTEE"

    def __str__(self) -> str:
        return str(self.value)
