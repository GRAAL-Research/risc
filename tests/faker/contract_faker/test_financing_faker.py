from unittest import TestCase
from unittest.mock import patch

from risc import FinancingFaker


class FinancingFakerTest(TestCase):
    @patch("risk.financing_faker.Faker")
    @patch("risk.financing_faker.choice")
    def test_whenFinancingFaker_thenReturnFinancingDetails(self, bank_faker, address_faker):
        bank_faker.return_value = "A Bank"
        address_faker().address.return_value = "An Address"
        financing_faker = FinancingFaker(locale="fr_CA")

        actual = financing_faker.financing()
        expected = "A Bank An Address"
        self.assertEqual(expected, actual)
