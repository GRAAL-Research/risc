import datetime
import re
from unittest.mock import patch

from risc_generator import FPQ1Contract
from risc_generator.content import fr, en
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

    @patch("risc_generator.contract.Faker")
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
            "Fait par l'Assureur à Québec le 1 février 2022\n"
            "Sherlock Holmes\n"
            "Président et chef de la direction\n"
            "Ceci n'est pas une facture, veuillez vous référer aux documents de la facturation pour "
            "les montants à payer ou à recevoir\n"
            "PRIME DU VÉHICULE 1\n"
            "Catégorie d'assurance :\n"
            "AUTOMOBILE\n"
            "PRIME ANNUELLE\n"
            "7$ (excluant taxe)\n"
            "VOTRE NOUVELLE POLICE 12 MOIS\n"
            "MONTANT\n"
            "7$ (excluant taxe)\n"
            "TAXE\n"
            "0.63$\n"
        )

        self.assertEqual(expected, actual)

    @patch("risc_generator.contract.Faker")
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
            "Prepared by the Insurer in Quebec City on February 1, 2022\n"
            "Sherlock Holmes\n"
            "President and chief executive officer\n"
            "This is not an invoice. Please refer to the billing documents"
            "for information on the amounts payable or receivable\n"
            "PREMIUM VEHICLE 1\n"
            "Class of insurance:\n"
            "AUTOMOBILE\n"
            "ANNUAL PREMIUM\n"
            "7$ (excluding tax)\n"
            "YOUR NEW 12-MONTH POLICY\n"
            "MONTANT\n"
            "7$ (excluding tax)\n"
            "TAX\n"
            "0.63$\n"
        )

        self.assertEqual(expected, actual)
