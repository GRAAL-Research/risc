import random

from faker import Faker


class PaymentMethodFaker(Faker):
    def __init__(self, locale: str) -> None:
        """
        locale (str): The locale language setting to use for simulation. Can either be `'fr_CA'` or `'en_CA'`.
        """
        if locale == "fr_CA":
            self.bill = "facture"
            self.pre_authorize = "paiement"
        elif locale == "en_CA":
            self.bill = "bill"
            self.pre_authorize = "pre-authorize"
        super().__init__(locale)

    def payment_method(self) -> str:
        """
        A faker function to fake a payment method.

        Return:
            The payment method, either 'bill' or 'pre-authorize'.
        """
        return random.choices([self.bill, self.pre_authorize], weights=[0.05, 0.95], k=1)[0]
