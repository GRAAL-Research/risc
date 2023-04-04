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

    def test_givenAFRContract_whenGenerateItem1Text_thenReturnProperFRText(self):
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

        actual = fr.declaration_articles.generate_item_1_text(
            insuree_name=fpq1_contract.insuree.name, insuree_address=fpq1_contract.insuree.address
        )

        a_insuree_name = "A Name"
        a_insuree_address = "An address\nA city, QC, A1A 1A1"

        expected = (
            "Article 1. NOM ET ADRESSE DE L'ASSURÉ DÉSIGNÉ*\n"
            f"{a_insuree_name}\n"
            f"{a_insuree_address}\n"
            "*La ville et la province de l'adresse écrite à cet article 1 constituent les lieux d'usage principal, "
            "de remisage et de stationnement du véhicule désigné. Si ce n'est pas le cas, le preneur ou l'assuré "
            "désigné doit le déclarer.\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContract_whenGenerateItem1Text_thenReturnProperENText(self):
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

        actual = en.declaration_articles.generate_item_1_text(
            insuree_name=fpq1_contract.insuree.name, insuree_address=fpq1_contract.insuree.address
        )

        a_insuree_name = "A Name"
        a_insuree_address = "An address\nA city, QC, A1A 1A1"

        expected = (
            "Item 1. NAME AND ADDRESS OF THE NAMED INSURED*\n"
            f"{a_insuree_name}\n"
            f"{a_insuree_address}\n"
            "*The described vehicle is and will be mainly used, stored and parked in the town/city and "
            "province shown in Item 1. If not, the client or the named insured must so declare.\n"
        )

        self.assertEqual(expected, actual)
