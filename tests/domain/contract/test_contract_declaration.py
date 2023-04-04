import datetime
import re
from unittest.mock import patch

from risc import FPQ1Contract
from risc.content import fr, en
from tests.domain.contract.contract_base import ContractTestBase


class ContractDeclarationTest(ContractTestBase):
    def test_givenAFRContract_whenGenerateDeclarationText_thenReturnProperFRText(self):
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

        actual_declaration_text = fpq1_contract.generate_declaration_text()

        actual_number_of_pages = len(re.findall("<###NEW_PAGE###>", actual_declaration_text))

        expected = 5

        self.assertEqual(expected, actual_number_of_pages)

    def test_givenAENContract_whenGenerateDeclarationText_thenReturnProperENText(self):
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

        actual_declaration_text = fpq1_contract.generate_declaration_text()

        actual_number_of_pages = len(re.findall("<###NEW_PAGE###>", actual_declaration_text))

        expected = 5

        self.assertEqual(expected, actual_number_of_pages)

    @patch("risk.contract.Faker")
    def test_givenAFRContract_whenGeneratePremiumTicket_thenReturnProperFRText(self, date_faker_mock):
        a_year = 2022
        a_month = 2
        a_day = 1

        date_faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

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

        actual = fr.declaration.generate_premium_ticket(
            contract_starting_date=fpq1_contract.formatted_text_date(), premium=self.a_premium
        )
        expected = (
            f"Fait par l'Assureur à Québec le 1 février 2022\n"
            f"Sherlock Holmes\n"
            f"Président et chef de la direction\n"
            f"Ceci n'est pas une facture, veuillez vous référer aux documents de la facturation pour "
            f"les montants à payer ou à recevoir\n"
            f"PRIME DU VÉHICULE 1\n"
            f"Catégorie d'assurance :\n"
            f"AUTOMOBILE\n"
            f"PRIME ANNUELLE\n"
            f"7$ (excluant taxe)\n"
            f"VOTRE NOUVELLE POLICE 12 MOIS\n"
            f"MONTANT\n"
            f"7$ (excluant taxe)\n"
            f"TAXE\n"
            f"0.63$\n"
        )

        self.assertEqual(expected, actual)

    @patch("risk.contract.Faker")
    def test_givenAENContract_whenGeneratePremiumTicket_thenReturnProperENText(self, date_faker_mock):
        a_year = 2022
        a_month = 2
        a_day = 1

        date_faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

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

        actual = en.declaration.generate_premium_ticket(
            contract_starting_date=fpq1_contract.formatted_text_date(), premium=self.a_premium
        )
        expected = (
            f"Prepared by the Insurer in Quebec City on February 1, 2022\n"
            f"Sherlock Holmes\n"
            f"President and chief executive officer\n"
            f"This is not an invoice. Please refer to the billing documents"
            f"for information on the amounts payable or receivable\n"
            f"PREMIUM VEHICLE 1\n"
            f"Class of insurance:\n"
            f"AUTOMOBILE\n"
            f"ANNUAL PREMIUM\n"
            f"7$ (excluding tax)\n"
            f"YOUR NEW 12-MONTH POLICY\n"
            f"MONTANT\n"
            f"7$ (excluding tax)\n"
            f"TAX\n"
            f"0.63$\n"
        )

        self.assertEqual(expected, actual)
