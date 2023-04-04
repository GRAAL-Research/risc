from risc_generator import Protections, FPQ1Contract, Premium
from risc_generator.content import fr, en
from tests.domain.contract.contract_base import ContractTestBase

INCLUDE = "include"
EXCLUDE = "exclude"


class ContractDeclarationTest(ContractTestBase):
    def setUp(self) -> None:
        self.a_protections = Protections(protections=self.a_dict_of_protections)
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

        self.a_premium = Premium(**protection_premiums)

    def test_givenAFRContract_whenGenerateItem2Text_thenReturnProperFRText(self):
        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_2_text(
            contract_start_date=fpq1_contract.contract_start_date, contract_end_date=fpq1_contract.contract_end_date
        )

        a_start_date = "2022-02-01"  # See self.a_contract_start_date
        a_contract_end_date = "2023-02-01"  # 1 year later

        expected = (
            "Article 2. DURÉE DU CONTRAT\n"
            f"DU : {a_start_date}* AU : {a_contract_end_date}* EXCLUSIVEMENT\n"
            "*à 0 h 01 selon l'heure normale à l'adresse de l'assuré désigné.\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContract_whenGenerateItem2Text_thenReturnProperENText(self):
        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_2_text(
            contract_start_date=fpq1_contract.contract_start_date, contract_end_date=fpq1_contract.contract_end_date
        )

        a_start_date = "2022-02-01"  # See self.a_contract_start_date
        a_contract_end_date = "2023-02-01"  # 1 year later

        expected = (
            "Item 2. CONTRACT PERIOD\n"
            f"FROM: {a_start_date}* TO: {a_contract_end_date}* EXCLUSIVELY\n"
            "*at 12:01 A.M. standard time at the address of the named insured.\n"
        )

        self.assertEqual(expected, actual)
