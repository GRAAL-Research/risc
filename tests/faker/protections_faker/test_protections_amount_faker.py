from unittest import TestCase

from risc_generator import (
    liability_coverage_amount_faker,
    b1_deductible_faker,
    b2_deductible_faker,
    b3_deductible_faker,
    b4_deductible_faker,
)


class ProtectionsAmountFakerTests(TestCase):
    n = 250000
    delta = 0.05  # A delta of 0.05, meaning we accept a 5% deviation from the expected probabilities

    def test_givenALiabilityCoverageAmountFaking_thenSimulationAreInDeltaExpectedProb(
        self,
    ):
        probs = [0.6, 0.4]
        coverages = [liability_coverage_amount_faker(liability_amount_probs=probs) == 1000000 for _ in range(self.n)]

        actual = sum(coverages) / self.n  # Prob of having 1 million in liability coverage
        expected = probs[0]

        self.assertAlmostEqual(actual, expected, delta=self.delta)

        probs = [0.8, 0.2]
        coverages = [liability_coverage_amount_faker(liability_amount_probs=probs) == 1000000 for _ in range(self.n)]

        actual = sum(coverages) / self.n  # Prob of having 1 million in liability coverage
        expected = probs[0]

        self.assertAlmostEqual(actual, expected, delta=self.delta)

    def test_givenAB1DeductibleAmountFaking_thenSimulationAreInDeltaExpectedProb(self):
        coverages = [b1_deductible_faker() == 250 for _ in range(self.n)]

        actual = sum(coverages) / self.n  # Prob of having 250 of deductible
        expected_prod = 0.15
        self.assertAlmostEqual(actual, expected_prod, delta=self.delta)

        coverages = [b1_deductible_faker() == 500 for _ in range(self.n)]

        actual = sum(coverages) / self.n  # Prob of having 500 of deductible
        expected_prod = 0.7
        self.assertAlmostEqual(actual, expected_prod, delta=self.delta)

        coverages = [b1_deductible_faker() == 1000 for _ in range(self.n)]

        actual = sum(coverages) / self.n  # Prob of having 1000 of deductible
        expected_prod = 0.15
        self.assertAlmostEqual(actual, expected_prod, delta=self.delta)

    def test_givenAB2DeductibleAmountFaking_thenSimulationAreInDeltaExpectedProb(self):
        coverages = [b2_deductible_faker() == 250 for _ in range(self.n)]

        actual = sum(coverages) / self.n  # Prob of having 250 of deductible
        expected_prod = 0.20
        self.assertAlmostEqual(actual, expected_prod, delta=self.delta)

        coverages = [b2_deductible_faker() == 500 for _ in range(self.n)]

        actual = sum(coverages) / self.n  # Prob of having 500 of deductible
        expected_prod = 0.65
        self.assertAlmostEqual(actual, expected_prod, delta=self.delta)

        coverages = [b2_deductible_faker() == 1000 for _ in range(self.n)]

        actual = sum(coverages) / self.n  # Prob of having 1000 of deductible
        expected_prod = 0.15
        self.assertAlmostEqual(actual, expected_prod, delta=self.delta)

    def test_givenAB3DeductibleAmountFaking_thenSimulationAreInDeltaExpectedProb(self):
        coverages = [b3_deductible_faker() == 250 for _ in range(self.n)]

        actual = sum(coverages) / self.n  # Prob of having 250 of deductible
        expected_prod = 0.50
        self.assertAlmostEqual(actual, expected_prod, delta=self.delta)

        coverages = [b3_deductible_faker() == 500 for _ in range(self.n)]

        actual = sum(coverages) / self.n  # Prob of having 500 of deductible
        expected_prod = 0.40
        self.assertAlmostEqual(actual, expected_prod, delta=self.delta)

        coverages = [b3_deductible_faker() == 1000 for _ in range(self.n)]

        actual = sum(coverages) / self.n  # Prob of having 1000 of deductible
        expected_prod = 0.10
        self.assertAlmostEqual(actual, expected_prod, delta=self.delta)

    def test_givenAB4DeductibleAmountFaking_thenSimulationAreInDeltaExpectedProb(self):
        coverages = [b4_deductible_faker() == 250 for _ in range(self.n)]

        actual = sum(coverages) / self.n  # Prob of having 250 of deductible
        expected_prod = 0.55
        self.assertAlmostEqual(actual, expected_prod, delta=self.delta)

        coverages = [b4_deductible_faker() == 500 for _ in range(self.n)]

        actual = sum(coverages) / self.n  # Prob of having 500 of deductible
        expected_prod = 0.40
        self.assertAlmostEqual(actual, expected_prod, delta=self.delta)

        coverages = [b4_deductible_faker() == 1000 for _ in range(self.n)]

        actual = sum(coverages) / self.n  # Prob of having 1000 of deductible
        expected_prod = 0.05
        self.assertAlmostEqual(actual, expected_prod, delta=self.delta)
