from unittest import TestCase

from risc_generator import generate_vin, is_valid_vehicle_year


class ToolsTest(TestCase):
    def test_givenValidVehicleYear_whenIsValidVehicleYear_returnTrue(self):
        vehicle_year = 2020
        contract_year = 2020

        self.assertTrue(is_valid_vehicle_year(vehicle_year=vehicle_year, contract_year=contract_year))

        vehicle_year = 2016
        contract_year = 2020

        self.assertTrue(is_valid_vehicle_year(vehicle_year=vehicle_year, contract_year=contract_year))

        vehicle_year = 2015
        contract_year = 2020

        self.assertTrue(is_valid_vehicle_year(vehicle_year=vehicle_year, contract_year=contract_year))

    def test_givenInValidVehicleYear_whenIsValidVehicleYear_returnFalse(self):
        vehicle_year = 214
        contract_year = 2020

        self.assertFalse(is_valid_vehicle_year(vehicle_year=vehicle_year, contract_year=contract_year))

        vehicle_year = 2013
        contract_year = 2020

        self.assertFalse(is_valid_vehicle_year(vehicle_year=vehicle_year, contract_year=contract_year))

        vehicle_year = 2000
        contract_year = 2010

        self.assertFalse(is_valid_vehicle_year(vehicle_year=vehicle_year, contract_year=contract_year))

    def test_whenGenerateAVin_thenIsProperLength(self):
        actual = len(generate_vin())
        expected = 17
        self.assertEqual(expected, actual)

    def test_whenGenerateAVin_thenIsAStringFormat(self):
        actual = generate_vin()
        self.assertIsInstance(actual, str)
