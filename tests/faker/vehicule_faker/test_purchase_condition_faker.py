from unittest import TestCase

from risc_generator import QuebecPurchaseConditionFaker


class QuebecPurchaseConditionFakerTests(TestCase):
    n = 250000
    delta = 0.05  # A delta of 0.05, meaning we accept a 5% deviation from the expected probabilities

    def setUp(self) -> None:
        self.a_fr_locale = "fr_CA"
        self.a_en_locale = "en_CA"

    def test_whenPurchaseConditionFakerEN_thenAreInDeltaExpectedDefaultProb(
        self,
    ):
        quebec_purchase_condition_faker = QuebecPurchaseConditionFaker(locale=self.a_en_locale)

        purchase_conditions = [quebec_purchase_condition_faker.purchase_condition() == "used" for _ in range(self.n)]

        actual = sum(purchase_conditions) / self.n  # Prob of having a used car
        expected = 0.91

        self.assertAlmostEqual(actual, expected, delta=self.delta)

    def test_whenPurchaseConditionFakerFR_thenAreInDeltaExpectedDefaultProb(
        self,
    ):
        quebec_purchase_condition_faker = QuebecPurchaseConditionFaker(locale=self.a_fr_locale)

        purchase_conditions = [quebec_purchase_condition_faker.purchase_condition() == "usagé" for _ in range(self.n)]

        actual = sum(purchase_conditions) / self.n  # Prob of having a used car
        expected = 0.91

        self.assertAlmostEqual(actual, expected, delta=self.delta)

    def test_givenPurchaseConditionFakerFR_whenNewPurchaseCondition_thenReturnFRNew(self):
        quebec_purchase_condition_faker = QuebecPurchaseConditionFaker(locale=self.a_fr_locale)

        expected = "neuf"

        actual = quebec_purchase_condition_faker.new_purchase_condition()

        self.assertEqual(expected, actual)

    def test_givenPurchaseConditionFakerEN_whenNewPurchaseCondition_thenReturnENNew(self):
        quebec_purchase_condition_faker = QuebecPurchaseConditionFaker(locale=self.a_en_locale)

        expected = "new"

        actual = quebec_purchase_condition_faker.new_purchase_condition()

        self.assertEqual(expected, actual)
