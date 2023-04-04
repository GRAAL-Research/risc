from unittest import TestCase

from risc_generator import (
    is_valid_protections,
    is_only_liability_coverage,
    include_b1_coverage,
    include_b2_coverage,
    include_b3_coverage,
    include_b4_coverage,
)


class ProtectionsFakerValidationToolsTest(TestCase):
    def test_GivenASetOfValidProtection_whenIsValidProtections_thenReturnTrue(self):
        a_value = True

        # Case 1
        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 1,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
        }
        actual_is_valid_protections = is_valid_protections(synthetic_coverage=dict_protections, can_have_faq_41=a_value)
        self.assertTrue(actual_is_valid_protections)

        # Case 2
        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 1,
            "PropertyDamageB3Coverage": 1,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
        }
        actual_is_valid_protections = is_valid_protections(synthetic_coverage=dict_protections, can_have_faq_41=a_value)
        self.assertTrue(actual_is_valid_protections)

        # Case 3
        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 1,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 1,
            "FAQ5ACoverage": 1,
        }
        actual_is_valid_protections = is_valid_protections(synthetic_coverage=dict_protections, can_have_faq_41=a_value)
        self.assertTrue(actual_is_valid_protections)

    def test_GivenAInvalidNoLiabilityCoverageProtection_whenIsValidProtections_thenReturnFalse(
        self,
    ):
        dict_protections = {
            "LiabilityCoverage": 0,  # No liability coverage is invalid
            "PropertyDamageB1Coverage": 1,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 1,
        }
        actual_is_valid_protections = is_valid_protections(synthetic_coverage=dict_protections, can_have_faq_41=True)
        self.assertFalse(actual_is_valid_protections)

    def test_GivenAInvalidB1WithAnyOtherBCoverageProtection_whenIsValidProtections_thenReturnFalse(
        self,
    ):
        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 1,  # B1 with any other B[2-4] is invalid
            "PropertyDamageB2Coverage": 1,
            "PropertyDamageB3Coverage": 1,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 1,
        }
        actual_is_valid_protections = is_valid_protections(synthetic_coverage=dict_protections, can_have_faq_41=True)
        self.assertFalse(actual_is_valid_protections)

    def test_GivenAInvalidFAQ41CoverageProtection_whenIsValidProtections_thenReturnFalse(
        self,
    ):
        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 1,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 1,
            "FAQ5ACoverage": 1,
            "FAQ41Coverage": 1,
        }

        # Invalid since client cannot have a FAQ41
        actual_is_valid_protections = is_valid_protections(synthetic_coverage=dict_protections, can_have_faq_41=False)
        self.assertFalse(actual_is_valid_protections)

    def test_GivenAInvalidB3B4CoverageProtection_whenIsValidProtections_thenReturnFalse(
        self,
    ):
        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 1,  # B3 and B4 invalid protection
            "PropertyDamageB4Coverage": 1,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 1,
        }
        actual_is_valid_protections = is_valid_protections(synthetic_coverage=dict_protections, can_have_faq_41=True)
        self.assertFalse(actual_is_valid_protections)

    def test_givenALiabilityOnlyCoverageProtection_whenIsOnlyLiabilityCoverage_thenReturnTrue(
        self,
    ):
        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 0,
        }
        actual_is_valid_protections = is_only_liability_coverage(synthetic_coverage=dict_protections)
        self.assertTrue(actual_is_valid_protections)

    def test_givenANotLiabilityOnlyCoverageProtection_whenIsOnlyLiabilityCoverage_thenReturnFalse(
        self,
    ):
        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 1,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 0,
        }
        actual_is_valid_protections = is_only_liability_coverage(synthetic_coverage=dict_protections)
        self.assertFalse(actual_is_valid_protections)

    def test_givenACoverageWithB1_whenIncludeB1Coverage_thenReturnTrue(self):
        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 1,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 0,
        }
        actual_is_valid_protections = include_b1_coverage(synthetic_coverage=dict_protections)
        self.assertTrue(actual_is_valid_protections)

    def test_givenACoverageWithoutB1_whenIncludeB1Coverage_thenReturnFalse(self):
        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 0,
        }
        actual_is_valid_protections = include_b1_coverage(synthetic_coverage=dict_protections)
        self.assertFalse(actual_is_valid_protections)

    def test_givenACoverageWithB2_whenIncludeB2Coverage_thenReturnTrue(self):
        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 1,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 0,
        }
        actual_is_valid_protections = include_b2_coverage(synthetic_coverage=dict_protections)
        self.assertTrue(actual_is_valid_protections)

    def test_givenACoverageWithoutB2_whenIncludeB2Coverage_thenReturnFalse(self):
        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 0,
        }
        actual_is_valid_protections = include_b2_coverage(synthetic_coverage=dict_protections)
        self.assertFalse(actual_is_valid_protections)

    def test_givenACoverageWithB3_whenIncludeB3Coverage_thenReturnTrue(self):
        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 1,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 0,
        }
        actual_is_valid_protections = include_b3_coverage(synthetic_coverage=dict_protections)
        self.assertTrue(actual_is_valid_protections)

    def test_givenACoverageWithoutB3_whenIncludeB3Coverage_thenReturnFalse(self):
        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 0,
        }
        actual_is_valid_protections = include_b3_coverage(synthetic_coverage=dict_protections)
        self.assertFalse(actual_is_valid_protections)

    def test_givenACoverageWithB4_whenIncludeB4Coverage_thenReturnTrue(self):
        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 1,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 0,
        }
        actual_is_valid_protections = include_b4_coverage(synthetic_coverage=dict_protections)
        self.assertTrue(actual_is_valid_protections)

    def test_givenACoverageWithoutB4_whenIncludeB4Coverage_thenReturnFalse(self):
        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 0,
        }
        actual_is_valid_protections = include_b4_coverage(synthetic_coverage=dict_protections)
        self.assertFalse(actual_is_valid_protections)

    def test_GivenAFAQ43CoverageWithSectionBProtection_whenIsValidProtections_thenReturnTrue(
        self,
    ):
        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 1,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 1,
            "FAQ43Coverage": 1,
        }
        actual_is_valid_protections = is_valid_protections(synthetic_coverage=dict_protections, can_have_faq_41=True)
        self.assertTrue(actual_is_valid_protections)

        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 1,
            "PropertyDamageB3Coverage": 1,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 1,
            "FAQ43Coverage": 1,
        }
        actual_is_valid_protections = is_valid_protections(synthetic_coverage=dict_protections, can_have_faq_41=True)
        self.assertTrue(actual_is_valid_protections)

        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 1,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 1,
            "FAQ43Coverage": 1,
        }
        actual_is_valid_protections = is_valid_protections(synthetic_coverage=dict_protections, can_have_faq_41=True)
        self.assertTrue(actual_is_valid_protections)

        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 1,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 1,
            "FAQ43Coverage": 1,
        }
        actual_is_valid_protections = is_valid_protections(synthetic_coverage=dict_protections, can_have_faq_41=True)
        self.assertTrue(actual_is_valid_protections)

        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 1,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 1,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 1,
            "FAQ43Coverage": 1,
        }
        actual_is_valid_protections = is_valid_protections(synthetic_coverage=dict_protections, can_have_faq_41=True)
        self.assertTrue(actual_is_valid_protections)

    def test_GivenAFAQ43CoverageWithoutSectionBProtection_whenIsValidProtections_thenReturnFalse(
        self,
    ):
        dict_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
            "FAQ41Coverage": 1,
            "FAQ43Coverage": 1,
        }
        actual_is_valid_protections = is_valid_protections(synthetic_coverage=dict_protections, can_have_faq_41=True)
        self.assertFalse(actual_is_valid_protections)
