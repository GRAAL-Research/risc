import datetime
from unittest import TestCase
from unittest.mock import MagicMock

from risc_generator import Protections, Premium
from risc_generator.domain.insuree import Insuree
from risc_generator.domain.vehicle import Vehicle

INCLUDE = "include"
EXCLUDE = "exclude"


class ContractTestBase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.a_client_number = "1234567"

        cls.a_contract_start_date = datetime.date(year=2022, month=2, day=1)

        cls.a_sex = "male"
        cls.a_name = "A Name"
        cls.a_date_of_birth = datetime.date(year=2020, month=1, day=1)
        cls.an_address = "An address\nA city, QC, A1A 1A1"
        cls.a_suspension = False
        cls.a_number_of_claims_past_years = 1
        cls.a_association_rebate = False
        cls.a_insuree = Insuree(
            sex=cls.a_sex,
            name=cls.a_name,
            birth_date=cls.a_date_of_birth,
            address=cls.an_address,
            suspension=cls.a_suspension,
            number_of_claims_past_years=cls.a_number_of_claims_past_years,
            association_rebate=cls.a_association_rebate,
        )

        cls.a_year = 2020
        cls.a_maker = "AMaker"
        cls.a_model = "AModel"
        cls.a_vin = "1234567890"
        cls.a_purchase_condition = "used"
        cls.a_vehicle = Vehicle(
            year=cls.a_year,
            make=cls.a_maker,
            model=cls.a_model,
            vin=cls.a_vin,
            purchase_condition=cls.a_purchase_condition,
            electric_vehicle=False,
        )

        cls.a_pre_authorize_payment_method = "pre-authorize"
        cls.a_bill_payment_method = "bill"

        cls.a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ27ACoverage": INCLUDE,
        }

        cls.a_fr_locale = "fr_CA"
        cls.a_en_locale = "en_CA"
        cls.a_locale = cls.a_fr_locale

        cls.a_premium_mock = MagicMock()

        cls.a_creditor = "A Bank An Address for The Bank"

        cls.a_protections = Protections(protections=cls.a_dict_of_protections)
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

        cls.a_premium = Premium(**protection_premiums)
