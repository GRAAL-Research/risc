from unittest import TestCase

from risc_generator import liability_coverage_faker


class LiabilityCoverageFakerTests(TestCase):
    n = 250000
    delta = 0.05  # A delta of 0.05, meaning we accept a 5% deviation from the expected probabilities

    def test_givenASyntheticCoverage_whenNotOnlyLiabilityCoverage_thenAreInDeltaExpectedNotOnlyProb(
        self,
    ):
        coverages = [
            liability_coverage_faker(is_only_liability_coverage=False).get("LiabilityCoverage") == 1000000
            for _ in range(self.n)
        ]

        actual = sum(coverages) / self.n  # Prob of having 1 million in liability coverage
        expected = 0.6

        self.assertAlmostEqual(actual, expected, delta=self.delta)

    def test_givenASyntheticCoverage_whenNotOnlyLiabilityCoverage_thenAreInDeltaExpectedOnlyProb(
        self,
    ):
        coverages = [
            liability_coverage_faker(is_only_liability_coverage=True).get("LiabilityCoverage") == 1000000
            for _ in range(self.n)
        ]

        actual = sum(coverages) / self.n  # Prob of having 1 million in liability coverage
        expected = 0.95

        self.assertAlmostEqual(actual, expected, delta=self.delta)
