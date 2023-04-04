from risc_generator import FPQ1Contract, Protections, Premium
from risc_generator.content import fr, en
from tests.domain.contract.contract_base import ContractTestBase


class ArticlesHeaderTest(ContractTestBase):
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

    def test_givenAFRContract_whenGenerateHeaderText_thenReturnProperFRText(self):
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

        a_policy_number = "1234567-001"

        expected = (
            "POLICE D'ASSURANCE AUTOMOBILE DU QUÉBEC\n"
            "F.P.Q. N 1 - FORMULAIRE DES PROPRIÉTAIRES\n"
            f"Numéro de police : {a_policy_number}\n\n"
            "CONDITIONS PARTICULIÈRES\n"
            "ÉMISSION de votre nouvelle police d'assurance\n"
        )

        actual = fr.declaration_articles.generate_declaration_header_text(fpq1_contract.policy_number)

        self.assertEqual(expected, actual)

    def test_givenAENContract_whenGenerateHeaderText_thenReturnProperENText(self):
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

        a_policy_number = "1234567-001"
        expected = (
            "QUEBEC AUTOMOBILE INSURANCE POLICY\n"
            "Q.P.F. B 1 - OWNER'S FORM\n"
            f"Policy Number: {a_policy_number}\n\n"
            "DECLARATIONS\n"
            "ISSUE of your new insurance policy\n"
        )

        actual = en.declaration_articles.generate_declaration_header_text(fpq1_contract.policy_number)

        self.assertEqual(expected, actual)
