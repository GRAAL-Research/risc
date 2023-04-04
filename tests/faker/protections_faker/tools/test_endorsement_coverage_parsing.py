from unittest import TestCase

from risc_generator import endorsement_coverage_parsing

INCLUDE = "include"
EXCLUDE = "exclude"


class EndorsementCoverageParsingTests(TestCase):
    def test_givenACoverageWithEndorsement_whenEndorsementCoverageParsing_thenReturnProperIncludeExcludeProtections(
        self,
    ):
        synthetic_coverage = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 1,
            "FAQ13ACoverage": 1,
        }
        actual = endorsement_coverage_parsing(synthetic_coverage)

        expected = {
            "FAQ5ACoverage": INCLUDE,
            "FAQ13ACoverage": INCLUDE,
        }

        self.assertDictEqual(actual, expected)

    def test_givenACoverageWithoutEndorsement_whenEndorsementCoverageParsing_thenReturnProperIncludeExcludeProtections(
        self,
    ):
        synthetic_coverage = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 0,
        }
        actual = endorsement_coverage_parsing(synthetic_coverage)

        expected = {}

        self.assertDictEqual(actual, expected)

    def test_givenACoverageWithEndorsementExclude_whenEndorsementCoverageParsing_thenReturnProperExcludeProtections(
        self,
    ):
        synthetic_coverage = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 0,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 0,
            "FAQ13ACoverage": 0,
        }
        actual = endorsement_coverage_parsing(synthetic_coverage)

        expected = {
            "FAQ5ACoverage": EXCLUDE,
            "FAQ13ACoverage": EXCLUDE,
        }

        self.assertDictEqual(actual, expected)
