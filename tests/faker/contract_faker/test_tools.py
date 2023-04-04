from unittest import TestCase

from risc_generator import generate_a_client_number


class ContractFakerToolsTest(TestCase):
    def test_whenGenerateAClientNumber_thenIs6Digits(self):
        client_number = generate_a_client_number()
        actual = len(client_number)
        expected = 6
        self.assertEqual(expected, actual)

    def test_whenGenerateAClientNumber_thenIsDigits(self):
        client_number = generate_a_client_number()
        expected = str
        self.assertIsInstance(client_number, expected)
