# pylint: disable=unnecessary-dunder-call


from unittest import TestCase

from risc_generator import Protections

INCLUDE = "include"
EXCLUDE = "exclude"


class ProtectionsTest(TestCase):
    def test_GivenASetOfProtection_whenSTR_thenReturnProperText(self):
        # Case 1
        dict_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ5ACoverage": INCLUDE,
        }
        protections = Protections(protections=dict_protections)

        actual = protections.__str__()
        expected = (
            "Chapter A: 1000000$\nChapter B: \nCollision protected with 250$ franchise\nOther non "
            "collision protected with 250$ franchise"
        )
        self.assertEqual(expected, actual)

        # Case 2
        dict_protections = {
            "LiabilityCoverage": 2000000,
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB2Coverage": 500,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ5ACoverage": INCLUDE,
        }
        protections = Protections(protections=dict_protections)

        actual = protections.__str__()
        expected = (
            "Chapter A: 2000000$\nChapter B: \nCollision protected with 500$ franchise\nOther non "
            "collision protected with 250$ franchise"
        )
        self.assertEqual(expected, actual)

        # Case 3
        dict_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": EXCLUDE,
            "PropertyDamageB4Coverage": 250,
            "FAQ5ACoverage": INCLUDE,
        }
        protections = Protections(protections=dict_protections)

        actual = protections.__str__()
        expected = (
            "Chapter A: 1000000$\nChapter B: \nCollision protected with 250$ franchise\nDesignated "
            "protected with 250$ franchise"
        )
        self.assertEqual(expected, actual)

    def test_givenASetOfProtectionsWithProtectionNameInProtection_whenIsProtected_thenReturnTrue(
        self,
    ):
        dict_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": EXCLUDE,
            "PropertyDamageB4Coverage": 250,
            "FAQ5ACoverage": INCLUDE,
        }
        protections = Protections(protections=dict_protections)

        protected = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB4Coverage": 250,
            "FAQ5ACoverage": INCLUDE,
        }

        for protection_name, _ in protected.items():
            self.assertTrue(protections.is_protected(protection_name))

        not_protected = {
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB3": EXCLUDE,
        }

        for protection_name, _ in not_protected.items():
            self.assertFalse(protections.is_protected(protection_name))

    def test_givenASetOfProtectionsWithProtectionNameInProtection_whenPropertyDamageProtections_thenReturnCorrectList(
        self,
    ):
        dict_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": EXCLUDE,
            "PropertyDamageB4Coverage": 250,
            "FAQ5ACoverage": INCLUDE,
        }
        protections = Protections(protections=dict_protections)

        expected_number_of_element_in_property_damage_protections = 2
        actual_number_of_element = len(protections.property_damage_protections())
        self.assertEqual(expected_number_of_element_in_property_damage_protections, actual_number_of_element)

    def test_givenAProtection_whenGetWithCamelCaseProtectionName_returnProtection(self):
        dict_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": EXCLUDE,
            "PropertyDamageB4Coverage": 250,
            "FAQ5ACoverage": INCLUDE,
        }
        protections = Protections(protections=dict_protections)

        self.assertIsNotNone(protections.get("LiabilityCoverage"))

    def test_givenAProtection_whenEndorsementProtections_returnAllEndorsementInCamelCase(self):
        dict_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": EXCLUDE,
            "PropertyDamageB4Coverage": 250,
            "FAQ5ACoverage": INCLUDE,
        }
        protections = Protections(protections=dict_protections)

        actual = protections.endorsement_protections()

        expected_len = 1
        self.assertEqual(len(actual), expected_len)
        expected_element = ["FAQ5ACoverage"]
        self.assertEqual(actual, expected_element)

        dict_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": EXCLUDE,
            "PropertyDamageB4Coverage": 250,
            "FAQ5ACoverage": INCLUDE,
            "FAQ23ACoverage": INCLUDE,
            "FAQ55Limitation": INCLUDE,
        }
        protections = Protections(protections=dict_protections)

        actual = protections.endorsement_protections()

        expected_len = 3
        self.assertEqual(len(actual), expected_len)
        expected_element = ["FAQ5ACoverage", "FAQ23ACoverage", "FAQ55Limitation"]
        self.assertEqual(actual, expected_element)
