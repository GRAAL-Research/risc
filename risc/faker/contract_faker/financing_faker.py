from random import choice

from faker import Faker

bank_names_fr = [
    "Banque CIBC",
    "BMO Banque de Montréal",
    "Banque Desjardins",
    "Banque HSBC Canada",
    "Banque Laurentienne du Canada",
    "Banque Nationale du Canada",
    "Banque Royale du Canada",
    "Banque Scotia",
    "Banque TD Canada Trust",
]

bank_names_en = [
    "CIBC Bank",
    "BMO Montreal Bank",
    "Desjardins Bank",
    "HSBC Canada Bank",
    "Laurentian Bank of Canada",
    "National Bank of Canada",
    "Royal Bank of Canada",
    "Scotia Bank",
    "TD Canada Trust Bank",
]


class FinancingFaker:
    def __init__(self, locale: str) -> None:
        """
        A faker to fake a financing institution.

                locale (str): The locale language setting to use for simulation. Can either be `'fr_CA'` or `'en_CA'`.
        """
        self.locale = locale

        self.address_faker = Faker(locale=self.locale)

        if self.locale == "fr_CA":
            self.bank_name = bank_names_fr
        elif self.locale == "en_CA":
            self.bank_name = bank_names_en
        else:
            raise ValueError(f"The locale {locale} is not supporter. It can either be 'fr_CA' or 'en_CA'.")

    def financing(self) -> str:
        """
        Method to fake a financing details information. Namely, is name and address.

        Return:
            A string of the bank name and address in capitalize characters.
        """
        bank = choice(self.bank_name)
        address = self.address_faker.address()

        return f"{bank} {address}"
