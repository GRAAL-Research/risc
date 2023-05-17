from unittest import TestCase
from unittest.mock import patch

from risc_generator import Insuree, InsureeFaker


class InsureeFakerTest(TestCase):
    def setUp(self) -> None:
        self.a_fr_locale = "fr_CA"
        self.a_en_locale = "en_CA"
        self.a_locale = self.a_en_locale

    def test_whenCreateAnInsuree_thenReturnAnInsuree(self):
        insuree_faker = InsureeFaker(self.a_locale)
        insuree = insuree_faker.insuree()
        self.assertIsInstance(insuree, Insuree)

    @patch("risc_generator.insuree_faker.SexFaker")
    def test_givenCreateMaleFakeInsuree_whenInsuree_thenReturnAMaleInsuree(self, sex_faker_mock):
        sex_faker_mock().gender.return_value = "male"
        insuree_faker = InsureeFaker(self.a_en_locale)

        insuree = insuree_faker.insuree()

        actual_sex = insuree.sex
        expected_sex = "male"

        self.assertEqual(actual_sex, expected_sex)

    @patch("risc_generator.insuree_faker.SexFaker")
    def test_givenCreateFemaleFakeInsuree_whenInsuree_thenReturnAFemaleInsuree(self, sex_faker_mock):
        sex_faker_mock().gender.return_value = "female"
        insuree_faker = InsureeFaker(self.a_en_locale)

        insuree = insuree_faker.insuree()

        actual_sex = insuree.sex
        expected_sex = "female"

        self.assertEqual(actual_sex, expected_sex)

    @patch("risc_generator.insuree_faker.SexFaker")
    def test_givenCreateHommeFakeInsuree_whenInsuree_thenReturnAHommeInsuree(self, sex_faker_mock):
        sex_faker_mock().gender.return_value = "homme"
        insuree_faker = InsureeFaker(self.a_en_locale)

        insuree = insuree_faker.insuree()

        actual_sex = insuree.sex
        expected_sex = "homme"

        self.assertEqual(actual_sex, expected_sex)

    @patch("risc_generator.insuree_faker.SexFaker")
    def test_givenCreateFemmeFakeInsuree_whenInsuree_thenReturnAFemmeInsuree(self, sex_faker_mock):
        sex_faker_mock().gender.return_value = "femme"
        insuree_faker = InsureeFaker(self.a_en_locale)

        insuree = insuree_faker.insuree()

        actual_sex = insuree.sex
        expected_sex = "femme"

        self.assertEqual(actual_sex, expected_sex)
