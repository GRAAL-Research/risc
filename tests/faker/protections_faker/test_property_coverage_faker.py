from unittest import TestCase
from unittest.mock import ANY

from risc_generator import property_coverage_faker

INCLUDE = "include"
EXCLUDE = "exclude"


class PropertyCoverageFakerTests(TestCase):
    def assertEqualDict(self, expected, actual):
        for actual_key, actual_value in actual.items():
            expected_value = expected.get(actual_key)
            self.assertEqual(expected_value, actual_value)

    def test_givenB1Coverage_whenPropertyCoverageFaker_thenReturnIncludeAllOtherProtections(
        self,
    ):
        include_b1_coverage = True
        include_b2_coverage = False
        include_b3_coverage = False
        include_b4_coverage = False

        actual = property_coverage_faker(
            include_b1_coverage,
            include_b2_coverage,
            include_b3_coverage,
            include_b4_coverage,
        )

        expected = {
            "PropertyDamageB1Coverage": ANY,
            "PropertyDamageB2Coverage": INCLUDE,
            "PropertyDamageB3Coverage": INCLUDE,
            "PropertyDamageB4Coverage": INCLUDE,
        }

        self.assertEqualDict(expected=expected, actual=actual)

    def test_givenB2OnlyCoverage_whenPropertyCoverageFaker_thenReturnExcludeAllOtherProtections(
        self,
    ):
        include_b1_coverage = False
        include_b2_coverage = True
        include_b3_coverage = False
        include_b4_coverage = False

        actual = property_coverage_faker(
            include_b1_coverage,
            include_b2_coverage,
            include_b3_coverage,
            include_b4_coverage,
        )

        expected = {
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB2Coverage": ANY,
            "PropertyDamageB3Coverage": EXCLUDE,
            "PropertyDamageB4Coverage": EXCLUDE,
        }

        self.assertEqualDict(expected=expected, actual=actual)

    def test_givenB3OnlyCoverage_whenPropertyCoverageFaker_thenReturnExcludeAllOtherProtections(
        self,
    ):
        include_b1_coverage = False
        include_b2_coverage = False
        include_b3_coverage = True
        include_b4_coverage = False

        actual = property_coverage_faker(
            include_b1_coverage,
            include_b2_coverage,
            include_b3_coverage,
            include_b4_coverage,
        )

        expected = {
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB2Coverage": EXCLUDE,
            "PropertyDamageB3Coverage": ANY,
            "PropertyDamageB4Coverage": INCLUDE,
        }

        self.assertEqualDict(expected=expected, actual=actual)

    def test_givenB4OnlyCoverage_whenPropertyCoverageFaker_thenReturnExcludeAllOtherProtections(
        self,
    ):
        include_b1_coverage = False
        include_b2_coverage = False
        include_b3_coverage = False
        include_b4_coverage = True

        actual = property_coverage_faker(
            include_b1_coverage,
            include_b2_coverage,
            include_b3_coverage,
            include_b4_coverage,
        )

        expected = {
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB2Coverage": EXCLUDE,
            "PropertyDamageB3Coverage": EXCLUDE,
            "PropertyDamageB4Coverage": ANY,
        }

        self.assertEqualDict(expected=expected, actual=actual)

    def test_givenB2AndB3OnlyCoverage_whenPropertyCoverageFaker_thenReturnExcludeAllOtherProtections(
        self,
    ):
        include_b1_coverage = False
        include_b2_coverage = True
        include_b3_coverage = True
        include_b4_coverage = False

        actual = property_coverage_faker(
            include_b1_coverage,
            include_b2_coverage,
            include_b3_coverage,
            include_b4_coverage,
        )

        expected = {
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": ANY,
            "PropertyDamageB3Coverage": ANY,
            "PropertyDamageB4Coverage": INCLUDE,
        }

        self.assertEqualDict(expected=expected, actual=actual)

    def test_givenB2AndB4OnlyCoverage_whenPropertyCoverageFaker_thenReturnExcludeAllOtherProtections(
        self,
    ):
        include_b1_coverage = False
        include_b2_coverage = True
        include_b3_coverage = False
        include_b4_coverage = True

        actual = property_coverage_faker(
            include_b1_coverage,
            include_b2_coverage,
            include_b3_coverage,
            include_b4_coverage,
        )

        expected = {
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB2Coverage": ANY,
            "PropertyDamageB3Coverage": EXCLUDE,
            "PropertyDamageB4Coverage": ANY,
        }

        self.assertEqualDict(expected=expected, actual=actual)
