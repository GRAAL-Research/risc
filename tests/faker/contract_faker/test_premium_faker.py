import datetime
from unittest import TestCase

from risc_generator import Protections, Insuree
from risc_generator.faker.contract_faker.premium_faker import QuebecPremiumFaker

INCLUDE = "include"
EXCLUDE = "exclude"


class PremiumFakerTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.premium_faker = QuebecPremiumFaker()

    def assertNoPremiumOnProtection(self, actual, protection):
        self.assertIsNone(actual.get(protection))

    def assertPremiumOnProtection(self, actual, protection):
        self.assertGreater(actual.get(protection), 0)

    def test_whenPremiumFaker_withB2B3_thenReturnCorrectPremium(
        self,
    ):
        a_sex = "male"
        a_name = "A Name"
        a_date_of_birth = datetime.date(year=2020, month=1, day=1)
        an_address = "An address\nA city, QC, A1A 1A1"
        a_suspension = False
        a_number_of_claims_past_years = 1
        a_association_rebate = False
        a_insuree = Insuree(
            sex=a_sex,
            name=a_name,
            birth_date=a_date_of_birth,
            address=an_address,
            suspension=a_suspension,
            number_of_claims_past_years=a_number_of_claims_past_years,
            association_rebate=a_association_rebate,
        )

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
        }

        a_protections = Protections(protections=a_dict_of_protections)

        actual_premium = self.premium_faker.premium(protections=a_protections, insuree=a_insuree)

        self.assertPremiumOnProtection(actual_premium, "LiabilityCoveragePremium")

        self.assertPremiumOnProtection(actual_premium, "PropertyDamageB2CoveragePremium")
        self.assertPremiumOnProtection(actual_premium, "PropertyDamageB3CoveragePremium")

        # No premium for B1 and B4
        self.assertNoPremiumOnProtection(actual_premium, "PropertyDamageB1CoveragePremium")
        self.assertNoPremiumOnProtection(actual_premium, "PropertyDamageB4CoveragePremium")

    def test_whenPremiumFaker_withB1_thenReturnCorrectPremium(
        self,
    ):
        a_sex = "male"
        a_name = "A Name"
        a_date_of_birth = datetime.date(year=2020, month=1, day=1)
        an_address = "An address\nA city, QC, A1A 1A1"
        a_suspension = False
        a_number_of_claims_past_years = 1
        a_association_rebate = False
        a_insuree = Insuree(
            sex=a_sex,
            name=a_name,
            birth_date=a_date_of_birth,
            address=an_address,
            suspension=a_suspension,
            number_of_claims_past_years=a_number_of_claims_past_years,
            association_rebate=a_association_rebate,
        )

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": 500,
            "PropertyDamageB2Coverage": INCLUDE,
            "PropertyDamageB3Coverage": INCLUDE,
            "PropertyDamageB4Coverage": EXCLUDE,
        }

        a_protections = Protections(protections=a_dict_of_protections)

        actual_premium = self.premium_faker.premium(protections=a_protections, insuree=a_insuree)

        self.assertPremiumOnProtection(actual_premium, "LiabilityCoveragePremium")

        self.assertPremiumOnProtection(actual_premium, "PropertyDamageB1CoveragePremium")

        # No premium for B2, B3 and B4 since it is covered by B1
        self.assertNoPremiumOnProtection(actual_premium, "PropertyDamageB2CoveragePremium")
        self.assertNoPremiumOnProtection(actual_premium, "PropertyDamageB3CoveragePremium")
        self.assertNoPremiumOnProtection(actual_premium, "PropertyDamageB4CoveragePremium")

    def test_whenPremiumFaker_withB4_thenReturnCorrectPremium(
        self,
    ):
        a_sex = "male"
        a_name = "A Name"
        a_date_of_birth = datetime.date(year=2020, month=1, day=1)
        an_address = "An address\nA city, QC, A1A 1A1"
        a_suspension = False
        a_number_of_claims_past_years = 1
        a_association_rebate = False
        a_insuree = Insuree(
            sex=a_sex,
            name=a_name,
            birth_date=a_date_of_birth,
            address=an_address,
            suspension=a_suspension,
            number_of_claims_past_years=a_number_of_claims_past_years,
            association_rebate=a_association_rebate,
        )

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB2Coverage": EXCLUDE,
            "PropertyDamageB3Coverage": EXCLUDE,
            "PropertyDamageB4Coverage": 250,
            "FAQ27ACoverage": INCLUDE,
        }

        a_protections = Protections(protections=a_dict_of_protections)

        actual_premium = self.premium_faker.premium(protections=a_protections, insuree=a_insuree)

        self.assertPremiumOnProtection(actual_premium, "LiabilityCoveragePremium")

        self.assertPremiumOnProtection(actual_premium, "PropertyDamageB4CoveragePremium")

        # No premium for B2, B3 and B4 since it is covered by B1
        self.assertNoPremiumOnProtection(actual_premium, "PropertyDamageB2CoveragePremium")
        self.assertNoPremiumOnProtection(actual_premium, "PropertyDamageB3CoveragePremium")
        self.assertNoPremiumOnProtection(actual_premium, "PropertyDamageB1CoveragePremium")

    def test_whenPremiumFaker_withEndorsementsWithPremium_thenReturnCorrectPremium(
        self,
    ):
        a_sex = "male"
        a_name = "A Name"
        a_date_of_birth = datetime.date(year=2020, month=1, day=1)
        an_address = "An address\nA city, QC, A1A 1A1"
        a_suspension = False
        a_number_of_claims_past_years = 1
        a_association_rebate = False
        a_insuree = Insuree(
            sex=a_sex,
            name=a_name,
            birth_date=a_date_of_birth,
            address=an_address,
            suspension=a_suspension,
            number_of_claims_past_years=a_number_of_claims_past_years,
            association_rebate=a_association_rebate,
        )

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB2Coverage": EXCLUDE,
            "PropertyDamageB3Coverage": EXCLUDE,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ20ACoverage": INCLUDE,
            "FAQ33Coverage": INCLUDE,
            "FAQ34Coverage": INCLUDE,
            "FAQ43Coverage": INCLUDE,
        }

        a_protections = Protections(protections=a_dict_of_protections)

        actual_premium = self.premium_faker.premium(protections=a_protections, insuree=a_insuree)

        self.assertPremiumOnProtection(actual_premium, "LiabilityCoveragePremium")

        self.assertPremiumOnProtection(actual_premium, "FAQ20ACoveragePremium")
        self.assertPremiumOnProtection(actual_premium, "FAQ33CoveragePremium")
        self.assertPremiumOnProtection(actual_premium, "FAQ34CoveragePremium")
        self.assertPremiumOnProtection(actual_premium, "FAQ43CoveragePremium")
