from enum import Enum


class CardCardKnowledgeBasedAuthenticationType(str, Enum):
    FIRST_PET_NAME = "FIRST_PET_NAME"
    MATERNAL_GRANDMOTHER_MAIDEN_NAME = "MATERNAL_GRANDMOTHER_MAIDEN_NAME"
    FAVOURITE_CHILDHOOD_FRIEND = "FAVOURITE_CHILDHOOD_FRIEND"
    FIRST_CAR = "FIRST_CAR"
    CITY_PARENTS_MET = "CITY_PARENTS_MET"

    def __str__(self) -> str:
        return str(self.value)
