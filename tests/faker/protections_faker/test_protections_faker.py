from unittest import TestCase
from unittest.mock import MagicMock

from risc_generator import ProtectionsFaker


class ProtectionsFakerTest(TestCase):
    def test_GivenAProtectionsModelFaker_whenProtections_thenReturnProperProtections(
        self,
    ):
        # Case 1
        synthetic_faked_protections = {
            "LiabilityCoverage": 1,
            "PropertyDamageB1Coverage": 1,
            "PropertyDamageB2Coverage": 0,
            "PropertyDamageB3Coverage": 0,
            "PropertyDamageB4Coverage": 0,
            "FAQ5ACoverage": 1,
            "FAQ23ACoverage": 0,
        }

        model_mock = MagicMock()
        model_mock.sample.return_value = synthetic_faked_protections

        protection_faker = ProtectionsFaker(model=model_mock)
        protections = protection_faker.protections(can_have_faq_41=True)

        # Protected
        self.assertTrue(protections.is_protected("LiabilityCoverage"))
        self.assertTrue(protections.is_protected("PropertyDamageB1Coverage"))
        self.assertTrue(protections.is_protected("FAQ5ACoverage"))

        # Not protected
        self.assertFalse(protections.is_protected("FAQ23ACoverage"))
