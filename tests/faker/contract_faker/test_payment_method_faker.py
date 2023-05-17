from unittest import TestCase

from risc_generator import PaymentMethodFaker


class PaymentMethodFakerTests(TestCase):
    n = 250000
    delta = 0.05  # A delta of 0.05, meaning we accept a 5% deviation from the expected probabilities

    def setUp(self) -> None:
        self.payment_method_faker = PaymentMethodFaker(locale="en_CA")

    def test_whenPaymentMethodFaker_thenAreInDeltaExpectedPreAuthorizeProb(
        self,
    ):
        payment_method = [self.payment_method_faker.payment_method() == "pre-authorize" for _ in range(self.n)]

        actual = sum(payment_method) / self.n  # Prob of having a pre-authorize payment method
        expected = 0.95

        self.assertAlmostEqual(actual, expected, delta=self.delta)
