from unittest import TestCase

from risc_generator import ClaimsFaker


class ClaimsFakerTests(TestCase):
    n = 100000
    delta = 0.01  # A delta of 1%, meaning we accept a 1% deviation from the expected probabilities

    def test_whenClaimsFaker_thenAreInDeltaExpectedAverageNumberOfClaims(
        self,
    ):
        claims_faker = ClaimsFaker()
        number_of_years = 5

        payment_method = [claims_faker.claims(number_of_years=number_of_years) for _ in range(self.n)]

        # Expected number of claims in "number_of_years" (thus self.n for the number fo client times the number
        # of years we simulate claims)
        actual = sum(payment_method) / (self.n * number_of_years)
        expected = 0.0452

        self.assertAlmostEqual(actual, expected, delta=self.delta)
