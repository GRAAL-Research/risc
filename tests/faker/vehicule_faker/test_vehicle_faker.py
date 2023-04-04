from unittest import TestCase

from risc_generator import Vehicle, QuebecVehicleFaker


class VehicleFakerTest(TestCase):
    n_samples = 1000

    def setUp(self) -> None:
        self.a_fr_locale = "fr_CA"
        self.vehicle_faker = QuebecVehicleFaker(locale=self.a_fr_locale)

    def test_givenAYearOrSoContract_whenVehicleWithFaq43_thenCarIsLessThan5YearsOld(
        self,
    ):
        faq_43 = True
        faq_5a = True
        a_contract_year = 2022

        for _ in range(self.n_samples):
            fake_car = self.vehicle_faker.vehicle(faq_43=faq_43, faq_5a=faq_5a, contract_year=a_contract_year)
            actual_car_age = fake_car.year
            self.assertLessEqual(a_contract_year - actual_car_age, 5)

    def test_givenAYearOrSoContract_whenVehicleWithoutFaq43_thenCarCanBeGreaterThan5YearsOld(
        self,
    ):
        faq_43 = False
        faq_5a = True
        a_contract_year = 2022

        sampled_ages = []
        for _ in range(self.n_samples):
            fake_car = self.vehicle_faker.vehicle(faq_43=faq_43, faq_5a=faq_5a, contract_year=a_contract_year)
            actual_car_age = fake_car.year
            sampled_ages.append(a_contract_year - actual_car_age > 5)

        self.assertGreater(len(sampled_ages), 1)

    def test_givenAYearOrSoContract_whenVehicleWithFaq5a_thenCarIsNew(
        self,
    ):
        faq_43 = True
        faq_5a = True
        a_contract_year = 2022

        expected = "neuf"  # fr locale

        fake_car = self.vehicle_faker.vehicle(faq_43=faq_43, faq_5a=faq_5a, contract_year=a_contract_year)
        actual = fake_car.purchase_condition
        self.assertEqual(expected, actual)

    def test_givenAYearOrSoContract_whenVehicleWithoutFaq5a_thenCarIsNewOrUsed(
        self,
    ):
        faq_43 = False
        faq_5a = False
        a_contract_year = 2022

        sampled_purchase_condition = []
        for _ in range(self.n_samples):
            fake_car = self.vehicle_faker.vehicle(faq_43=faq_43, faq_5a=faq_5a, contract_year=a_contract_year)
            actual = fake_car.purchase_condition
            sampled_purchase_condition.append(actual == "neuf")

        self.assertGreater(sum(sampled_purchase_condition), 1)  # at least one is new ("neuf")
        self.assertGreater(len(sampled_purchase_condition) - sum(sampled_purchase_condition), 1)  # at least one is used

    def test_integration(self):
        # We test all the possible bool conf of the endorsement (FAQ) arguments

        faq_43 = False
        faq_5a = False

        a_contract_year = 2022
        self.assertIsInstance(
            self.vehicle_faker.vehicle(faq_43=faq_43, faq_5a=faq_5a, contract_year=a_contract_year),
            Vehicle,
        )

        faq_43 = True
        faq_5a = False

        a_contract_year = 2022
        self.assertIsInstance(
            self.vehicle_faker.vehicle(faq_43=faq_43, faq_5a=faq_5a, contract_year=a_contract_year),
            Vehicle,
        )

        faq_43 = True
        faq_5a = True

        a_contract_year = 2022
        self.assertIsInstance(
            self.vehicle_faker.vehicle(faq_43=faq_43, faq_5a=faq_5a, contract_year=a_contract_year),
            Vehicle,
        )

        faq_43 = False
        faq_5a = True

        a_contract_year = 2022
        self.assertIsInstance(
            self.vehicle_faker.vehicle(faq_43=faq_43, faq_5a=faq_5a, contract_year=a_contract_year),
            Vehicle,
        )
