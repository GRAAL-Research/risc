from unittest import TestCase

from risc_generator import association_rebate_faker


class AssociationRebateFakerTests(TestCase):
    n = 250000
    delta = 0.05  # A delta of 0.05, meaning we accept a 5% deviation from the expected probabilities

    def test_whenAssociationRebateFaker_thenAreInDeltaExpectedRebateProb(
        self,
    ):
        payment_method = [association_rebate_faker() for _ in range(self.n)]

        actual = sum(payment_method) / self.n  # Prob of having a pre-authorize payment method
        expected = 0.05

        self.assertAlmostEqual(actual, expected, delta=self.delta)
