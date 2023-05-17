# pylint: disable=unnecessary-dunder-call

from unittest import TestCase

from risc_generator import Vehicle


class VehicleTest(TestCase):
    def test_givenAVehicle_whenSTR_thenReturnProperText(self):
        a_year = 2020
        a_maker = "AMaker"
        a_model = "AModel"
        a_vin = "1234567890"
        a_purchase_condition = "used"

        vehicle_config = {
            "year": a_year,
            "make": a_maker,
            "model": a_model,
            "vin": a_vin,
            "purchase_condition": a_purchase_condition,
            "electric_vehicle": False,
        }
        vehicle = Vehicle(**vehicle_config)

        actual = vehicle.__str__()
        expected = "Amaker Amodel 2020 VIN: 1234567890"
        self.assertEqual(expected, actual)

    def test_givenAVehicleNotElectric_whenIsElectric_thenReturnFalse(self):
        a_year = 2020
        a_maker = "AMaker"
        a_model = "AModel"
        a_vin = "1234567890"
        a_purchase_condition = "used"

        vehicle_config = {
            "year": a_year,
            "make": a_maker,
            "model": a_model,
            "vin": a_vin,
            "purchase_condition": a_purchase_condition,
            "electric_vehicle": False,
        }
        vehicle = Vehicle(**vehicle_config)

        actual = vehicle.is_electric()
        self.assertFalse(actual)

    def test_givenAVehicleElectric_whenIsElectric_thenReturnTrue(self):
        a_year = 2020
        a_maker = "AMaker"
        a_model = "AModel"
        a_vin = "1234567890"
        a_purchase_condition = "used"

        vehicle_config = {
            "year": a_year,
            "make": a_maker,
            "model": a_model,
            "vin": a_vin,
            "purchase_condition": a_purchase_condition,
            "electric_vehicle": True,
        }
        vehicle = Vehicle(**vehicle_config)

        actual = vehicle.is_electric()
        self.assertTrue(actual)

    def test_givenAVehicleDetails_whenFormatVehicleCompleteDetails_thenReturnProperText(self):
        a_year = 2020
        a_maker = "AMaker"
        a_model = "AModel"
        a_vin = "1234567890"
        a_purchase_condition = "used"

        vehicle_config = {
            "year": a_year,
            "make": a_maker,
            "model": a_model,
            "vin": a_vin,
            "purchase_condition": a_purchase_condition,
            "electric_vehicle": True,
        }
        vehicle = Vehicle(**vehicle_config)

        actual = vehicle.format_vehicle_complete_details()
        expect = "AMaker AModel 2020 1234567890"
        self.assertEqual(actual, expect)

    def test_givenAVehicleDetails_whenFormatVehicleCompleteDetailsWithText_thenReturnProperText(self):
        a_year = 2020
        a_maker = "AMaker"
        a_model = "AModel"
        a_vin = "1234567890"
        a_purchase_condition = "used"

        vehicle_config = {
            "year": a_year,
            "make": a_maker,
            "model": a_model,
            "vin": a_vin,
            "purchase_condition": a_purchase_condition,
            "electric_vehicle": True,
        }
        vehicle = Vehicle(**vehicle_config)

        actual = vehicle.format_vehicle_complete_details(with_text="Serial number")
        expect = "AMaker - AModel - 2020 - Serial number 1234567890"
        self.assertEqual(actual, expect)

    def test_givenAVehicleDetails_whenFormatVehicleMakeYearDetails_thenReturnProperText(self):
        a_year = 2020
        a_maker = "AMaker"
        a_model = "AModel"
        a_vin = "1234567890"
        a_purchase_condition = "used"

        vehicle_config = {
            "year": a_year,
            "make": a_maker,
            "model": a_model,
            "vin": a_vin,
            "purchase_condition": a_purchase_condition,
            "electric_vehicle": True,
        }
        vehicle = Vehicle(**vehicle_config)

        actual = vehicle.format_vehicle_make_year_details()
        expect = "AMaker - 2020"
        self.assertEqual(actual, expect)

    def test_givenAVehicleDetails_whenFormatVehicleMakeModelYearDetailsWithText_thenReturnProperText(self):
        a_year = 2020
        a_maker = "AMaker"
        a_model = "AModel"
        a_vin = "1234567890"
        a_purchase_condition = "used"

        vehicle_config = {
            "year": a_year,
            "make": a_maker,
            "model": a_model,
            "vin": a_vin,
            "purchase_condition": a_purchase_condition,
            "electric_vehicle": True,
        }
        vehicle = Vehicle(**vehicle_config)

        actual = vehicle.format_vehicle_make_model_year_details()
        expect = "AMaker AModel 2020"
        self.assertEqual(actual, expect)
