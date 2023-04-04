from risc_generator import Protections, FPQ1Contract, Premium
from tests.domain.contract.contract_base import ContractTestBase

include = "include"


class ContractBillTest(ContractTestBase):
    def setUp(self) -> None:
        self.a_protections = Protections(protections=self.a_dict_of_protections)

    def test_givenAFRContract_whenGenerateBillText_thenReturnProperFRText(self):
        a_premium_amount = 1
        protection_premiums = {
            "LiabilityCoveragePremium": a_premium_amount,
            "PropertyDamageB2CoveragePremium": a_premium_amount,
            "PropertyDamageB3CoveragePremium": a_premium_amount,
            "FAQ20ACoveragePremium": a_premium_amount,
            "FAQ33ACoveragePremium": a_premium_amount,
            "FAQ34ACoveragePremium": a_premium_amount,
            "FAQ43ACoveragePremium": a_premium_amount,
        }
        a_premium = Premium(**protection_premiums)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method="facture",  # FR bill payment method
            protections=self.a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fpq1_contract.generate_bill_text()

        a_client_number = "1234567"
        a_insuree_name = "A Name"
        a_insuree_address = "An address\nA city, QC, A1A 1A1"
        a_premium_total = "7"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "FACTURATION - Reçu officiel\n"
            "Assurance des particuliers\n"
            f"Numéro client : {a_client_number}\n"
            f"Nom et adresse de l'assuré\n"
            f"{a_insuree_name}\n"
            f"{a_insuree_address}\n"
            f"Nom du payeur : {a_insuree_name}\n"
            f"ÉTAT DE VOTRE COMPTE - MODE DE PAIEMENT COMPTANT SEULEMENT\n"
            f"CATÉGORIE D'ASSURANCE | N POLICE | TRANSACTION ACTUELLE | PRISE D'EFFET | TYPE DE TRANSACTION | "
            f"MONTANT INCLUANT TAXE | SOLDE DE LA POLICE | TOTAL\n"
            f"Automobile | 001 | | | SOLDE AVANT TRANSACTION | | {a_premium_total}$ | {a_premium_total}$\n"
            f"À payer-terme en vigueur {a_premium_total}$\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractNoBill_whenGenerateBillText_thenReturnEmptyText(self):
        a_premium_amount = 1
        protection_premiums = {
            "LiabilityCoveragePremium": a_premium_amount,
            "PropertyDamageB2CoveragePremium": a_premium_amount,
            "PropertyDamageB3CoveragePremium": a_premium_amount,
            "FAQ20ACoveragePremium": a_premium_amount,
            "FAQ33ACoveragePremium": a_premium_amount,
            "FAQ34ACoveragePremium": a_premium_amount,
            "FAQ43ACoveragePremium": a_premium_amount,
        }
        a_premium = Premium(**protection_premiums)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fpq1_contract.generate_bill_text()

        expected = ""

        self.assertEqual(expected, actual)

    def test_givenAENContract_whenGenerateBillText_thenReturnProperENText(self):
        a_premium_amount = 1
        protection_premiums = {
            "LiabilityCoveragePremium": a_premium_amount,
            "PropertyDamageB2CoveragePremium": a_premium_amount,
            "PropertyDamageB3CoveragePremium": a_premium_amount,
            "FAQ20ACoveragePremium": a_premium_amount,
            "FAQ33ACoveragePremium": a_premium_amount,
            "FAQ34ACoveragePremium": a_premium_amount,
            "FAQ43ACoveragePremium": a_premium_amount,
        }
        a_premium = Premium(**protection_premiums)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_bill_payment_method,
            protections=self.a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = fpq1_contract.generate_bill_text()

        a_client_number = "1234567"
        a_insuree_name = "A Name"
        a_insuree_address = "An address\nA city, QC, A1A 1A1"
        a_premium_total = "7"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "INVOICING - Official receipt\n"
            "Personal Insurance\n"
            f"Customer number: {a_client_number}\n"
            f"Name and address of the insured\n"
            f"{a_insuree_name}\n"
            f"{a_insuree_address}\n"
            f"Payer's name: {a_insuree_name}\n"
            f"YOUR ACCOUNT STATUS - CASH ONLY\n"
            f"CLASS OF INSURANCE | POLICY NUMBER | CURRENT TRANSACTION | EFFECTIVE DATE | TRANSACTION TYPE "
            f"AMOUNT INCLUDING TAX | POLICY BALANCE | TOTAL\n"
            f"Automotive | 001 | | | BALANCE BEFORE TRANSACTION | | {a_premium_total}$ | {a_premium_total}$\n"
            f"Payable-Term in effect {a_premium_total}$\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractNoBill_whenGenerateBillText_thenReturnEmptyText(self):
        a_premium_amount = 1
        protection_premiums = {
            "LiabilityCoveragePremium": a_premium_amount,
            "PropertyDamageB2CoveragePremium": a_premium_amount,
            "PropertyDamageB3CoveragePremium": a_premium_amount,
            "FAQ20ACoveragePremium": a_premium_amount,
            "FAQ33ACoveragePremium": a_premium_amount,
            "FAQ34ACoveragePremium": a_premium_amount,
            "FAQ43ACoveragePremium": a_premium_amount,
        }
        a_premium = Premium(**protection_premiums)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = fpq1_contract.generate_bill_text()

        expected = ""

        self.assertEqual(expected, actual)
