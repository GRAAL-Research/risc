from unittest import TestCase

from risc_generator import SexFaker


class SexFakerTests(TestCase):
    n = 250000
    delta = 0.01  # A delta of 1%, meaning we accept a 1% deviation from the expected probabilities

    def setUp(self) -> None:
        self.a_fr_locale = "fr_CA"
        self.a_en_locale = "en_CA"

    def test_whenSexFakerEn_thenAreInDeltaExpectedDefaultProb(
        self,
    ):
        sex_faker = SexFaker(locale=self.a_en_locale)

        sex = [sex_faker.gender() == "male" for _ in range(self.n)]

        actual = sum(sex) / self.n  # Prob of been a male driver
        expected = 0.52  # 2860709 / 5546433

        self.assertAlmostEqual(actual, expected, delta=self.delta)

    def test_whenSexFakerEn_thenAreInDeltaExpectedUserProb(
        self,
    ):
        sex_faker = SexFaker(locale=self.a_en_locale, population_of_drivers=1000000, number_of_male_drivers=100000)

        sex = [sex_faker.gender() == "male" for _ in range(self.n)]

        actual = sum(sex) / self.n  # Prob of been a male driver
        expected = 0.10  # (50000 + 50000) / 1000000

        self.assertAlmostEqual(actual, expected, delta=self.delta)

    def test_whenSexFakerFr_thenAreInDeltaExpectedDefaultProb(
        self,
    ):
        sex_faker = SexFaker(locale=self.a_fr_locale)

        sex = [sex_faker.gender() == "homme" for _ in range(self.n)]

        actual = sum(sex) / self.n  # Prob of been a male driver
        expected = 0.52  # 2860709 / 5546433

        self.assertAlmostEqual(actual, expected, delta=self.delta)

    def test_whenSexFakerFr_thenAreInDeltaExpectedUserProb(
        self,
    ):
        sex_faker = SexFaker(locale=self.a_fr_locale, population_of_drivers=1000000, number_of_male_drivers=100000)

        sex = [sex_faker.gender() == "homme" for _ in range(self.n)]

        actual = sum(sex) / self.n  # Prob of been a male driver
        expected = 0.10  # (50000 + 50000) / 1000000

        self.assertAlmostEqual(actual, expected, delta=self.delta)
