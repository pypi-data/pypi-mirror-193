from enum import Enum


class PispgatewayPaymentContextPaymentContextCode(str, Enum):
    Bill_Payment = "BillPayment"
    Ecommerce_Goods = "EcommerceGoods"
    Ecommerce_Services = "EcommerceServices"
    Other = "Other"
    Party_To_Party = "PartyToParty"
    BILLPAYMENT = "BILLPAYMENT"
    ECOMMERCEGOODS = "ECOMMERCEGOODS"
    ECOMMERCESERVICES = "ECOMMERCESERVICES"
    OTHER = "OTHER"
    PARTYTOPARTY = "PARTYTOPARTY"

    def __str__(self) -> str:
        return str(self.value)
