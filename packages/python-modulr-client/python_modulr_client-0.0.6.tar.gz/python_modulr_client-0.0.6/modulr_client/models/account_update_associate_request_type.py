from enum import Enum


class AccountUpdateAssociateRequestType(str, Enum):
    PARTNER = "PARTNER"
    SIGNATORY = "SIGNATORY"
    SOLETRADER = "SOLETRADER"
    TRUST_BENEFICIARY = "TRUST_BENEFICIARY"
    C_INTEREST = "C_INTEREST"
    PCM_INDIVIDUAL = "PCM_INDIVIDUAL"
    INDIVIDUAL = "INDIVIDUAL"
    BENE_OWNER = "BENE_OWNER"
    DIRECTOR = "DIRECTOR"
    TRUST_TRUSTEE = "TRUST_TRUSTEE"
    TRUST_SETTLOR = "TRUST_SETTLOR"
    CSECRETARY = "CSECRETARY"

    def __str__(self) -> str:
        return str(self.value)
