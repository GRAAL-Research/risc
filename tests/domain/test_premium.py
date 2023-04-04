from unittest import TestCase

from risc_generator import Premium

INCLUDE = "include"
EXCLUDE = "exclude"


class PremiumTest(TestCase):
    def test_givenASetOfProtection_whenPremium_thenSetProtections(self):
        a_premium_amount = 1
        protection_premiums = {
            "LiabilityPremium": a_premium_amount,
            "PropertyDamageB2CoveragePremium": a_premium_amount,
            "PropertyDamageB3CoveragePremium": a_premium_amount,
            "FAQ20ACoveragePremium": a_premium_amount,
            "FAQ33CoveragePremium": a_premium_amount,
            "FAQ34CoveragePremium": a_premium_amount,
            "FAQ43CoveragePremium": a_premium_amount,
        }

        actual_premium = Premium(**protection_premiums)
        self.assertIsInstance(actual_premium, Premium)

        self.assertIsNotNone(actual_premium.get("LiabilityPremium"))

        # + 1 for the total premium amount
        self.assertEqual(len(list(actual_premium.__dict__.items())), len(list(protection_premiums.items())) + 1)

    def test_givenASetOfProtection_whenGet_thenReturnPremium(self):
        a_premium_amount = 1
        protection_premiums = {
            "LiabilityPremium": a_premium_amount,
            "PropertyDamageB2CoveragePremium": a_premium_amount,
            "PropertyDamageB3CoveragePremium": a_premium_amount,
            "FAQ20ACoveragePremium": a_premium_amount,
            "FAQ33CoveragePremium": a_premium_amount,
            "FAQ34CoveragePremium": a_premium_amount,
            "FAQ43CoveragePremium": a_premium_amount,
        }

        actual_premium = Premium(**protection_premiums)
        self.assertIsInstance(actual_premium, Premium)

        for key, _ in protection_premiums.items():
            self.assertIsNotNone(actual_premium.get(key))

    def test_givenASetOfProtection_whenGetOnProtectionNotInSetOfProtection_thenReturnNone(self):
        a_premium_amount = 1
        protection_premiums = {
            "LiabilityPremium": a_premium_amount,
            "PropertyDamageB2CoveragePremium": a_premium_amount,
            "PropertyDamageB3CoveragePremium": a_premium_amount,
        }

        actual_premium = Premium(**protection_premiums)
        self.assertIsInstance(actual_premium, Premium)

        protection_not_in_set_of_protections = [
            "FAQ20ACoveragePremium",
            "FAQ33CoveragePremium",
            "FAQ34CoveragePremium",
            "FAQ43CoveragePremium",
        ]
        for key in protection_not_in_set_of_protections:
            self.assertIsNone(actual_premium.get(key))

    def test_whenAProtection_getWithCamelCaseProtectionName_returnProtection(self):
        a_premium_amount = 1
        protection_premiums = {
            "LiabilityPremium": a_premium_amount,
            "PropertyDamageB2CoveragePremium": a_premium_amount,
            "PropertyDamageB3CoveragePremium": a_premium_amount,
        }

        actual_premium = Premium(**protection_premiums)
        self.assertIsNotNone(actual_premium.get("LiabilityPremium"))
