from unittest import TestCase

from risc_generator import DriverLicenseSuspensionFaker


class DiverLicenseSuspensionFakerTests(TestCase):
    n = 250000
    delta = 0.01  # A delta of 1%, meaning we accept a 1% deviation from the expected probabilities

    def test_whenDiverLicenseSuspensionFaker_thenAreInDeltaExpectedDefaultProb(
        self,
    ):
        driver_license_suspension_faker = DriverLicenseSuspensionFaker()

        payment_method = [driver_license_suspension_faker.suspension() for _ in range(self.n)]

        actual = sum(payment_method) / self.n  # Prob of having a driver license suspension
        expected = 0.02  # (14273 + 93047) / 5528681

        self.assertAlmostEqual(actual, expected, delta=self.delta)

    def test_whenDiverLicenseSuspensionFaker_thenAreInDeltaExpectedUserProb(
        self,
    ):
        driver_license_suspension_faker = DriverLicenseSuspensionFaker(
            total_drivers=1000000,
            total_alcohol_suspension=50000,
            total_points_suspension=50000,
        )

        payment_method = [driver_license_suspension_faker.suspension() for _ in range(self.n)]

        actual = sum(payment_method) / self.n  # Prob of having a driver license suspension
        expected = 0.10  # (50000 + 50000) / 1000000

        self.assertAlmostEqual(actual, expected, delta=self.delta)
