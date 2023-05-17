import datetime
from unittest.mock import patch

from risc_generator import FPQ1Contract, Protections
from tests.domain.contract.contract_base import ContractTestBase

INCLUDE = "include"
EXCLUDE = "exclude"


class ContractHeaderTest(ContractTestBase):
    def setUp(self) -> None:
        self.a_protections = Protections(protections=self.a_dict_of_protections)

    @patch("risc_generator.domain.contract.Faker")
    def test_givenAFRContractPreAuthorize_whenGenerateHeaderText_thenReturnProperFRText(self, faker_mock):
        # a_date
        a_year = 2022
        a_month = 1
        a_day = 2
        faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fpq1_contract.generate_header_text()

        a_date = "Le 2 janvier 2022\n\n\n"
        a_client_number = "Numéro client: 1234567\n"
        a_vehicle = "AMaker - 2020\n"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            f"{a_date}"
            "ÉMISSION\n"
            f"{a_client_number}"
            "Police / Durée du terme:\n"
            "001 / 12 mois\n\n"
            "JAMAIS SEUL POUR VOS ASSURANCES\n\n"
            "Vous trouverez vos documents d'assurance aux pages suivantes.\n"
            "Nous vous suggérons de les lire attentivement afin de vous assurer qu'ils sont conformes.\n"
            "Si une page Instructions importantes fait partie de ces documents, veuillez y porter une "
            "attention particulière, puisqu'elle comporte des renseignements essentiels au sujet de "
            "vos protections.\n"
            "N'hésitez pas à communiquer avec nous pour toute question ou commentaire.\n\n"
            "NOUS JOINDRE\n"
            "Service à la clientèle\n"
            "123 456-7890\n"
            "1 800 123-4567\n"
            "Télécopieur: 012 345-6789\n"
            "service.client@assureur.ca\n"
            "8 h à 20 h du lundi au vendredi\n"
            "8 h 30 à 16 h le samedi\n"
            "Réclamations\n"
            "098 765-4321\n"
            "1 800 765-4321\n"
            "Urgence 7 jours/24 heures\n"
            "Assistance juridique\n"
            "1 800 012-3456\n"
            "8 h 30 à 19 h du lundi au jeudi\n"
            "8 h 30 à 17 h le vendredi\n"
            "Votre succursale\n"
            "221 B Baker Street\n"
            "Ville (Province)\nA1A 1A1\n"
            "8 h 30 à 17 h du lundi au vendredi\n"
            "assureur.ca\n"
            "Vos documents d'assurance\n"
            "(Table des matières)\n"
            "Instructions importantes\n"
            "Assurance automobile\n"
            "Numéro police: 001\n"
            f"{a_vehicle}"
            f"Certificats d'assurance\n"
            f"(Documents à conserver)\n"
            f"Avantages Client\n"
            f"(Description de vos bénéfices client)\n"
            f"Libellés et avenants\n"
            f"{a_new_page}\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    @patch("risc_generator.domain.contract.Faker")
    def test_givenAFRContractBill_whenGenerateHeaderText_thenReturnProperFRText(self, faker_mock):
        # a_date
        a_year = 2022
        a_month = 1
        a_day = 2
        faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method="facture",  # FR bill payment method
            protections=self.a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fpq1_contract.generate_header_text()

        a_date = "Le 2 janvier 2022\n\n\n"
        a_client_number = "Numéro client: 1234567\n"
        a_vehicle = "AMaker - 2020\n"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            f"{a_date}"
            "ÉMISSION\n"
            f"{a_client_number}"
            "Police / Durée du terme:\n"
            "001 / 12 mois\n\n"
            "JAMAIS SEUL POUR VOS ASSURANCES\n\n"
            "Vous trouverez vos documents d'assurance aux pages suivantes.\n"
            "Nous vous suggérons de les lire attentivement afin de vous assurer qu'ils sont conformes.\n"
            "Si une page Instructions importantes fait partie de ces documents, veuillez y porter une "
            "attention particulière, puisqu'elle comporte des renseignements essentiels au sujet de "
            "vos protections.\n"
            "N'hésitez pas à communiquer avec nous pour toute question ou commentaire.\n\n"
            "NOUS JOINDRE\n"
            "Service à la clientèle\n"
            "123 456-7890\n"
            "1 800 123-4567\n"
            "Télécopieur: 012 345-6789\n"
            "service.client@assureur.ca\n"
            "8 h à 20 h du lundi au vendredi\n"
            "8 h 30 à 16 h le samedi\n"
            "Réclamations\n"
            "098 765-4321\n"
            "1 800 765-4321\n"
            "Urgence 7 jours/24 heures\n"
            "Assistance juridique\n"
            "1 800 012-3456\n"
            "8 h 30 à 19 h du lundi au jeudi\n"
            "8 h 30 à 17 h le vendredi\n"
            "Votre succursale\n"
            "221 B Baker Street\n"
            "Ville (Province)\nA1A 1A1\n"
            "8 h 30 à 17 h du lundi au vendredi\n"
            "assureur.ca\n"
            "Vos documents d'assurance\n"
            "(Table des matières)\n"
            "Instructions importantes\n"
            "Assurance automobile\n"
            "Numéro police: 001\n"
            f"{a_vehicle}"
            f"Certificats d'assurance\n"
            f"(Documents à conserver)\n"
            f"Facturation\n"
            f"Avantages Client\n"
            f"(Description de vos bénéfices client)\n"
            f"Libellés et avenants\n"
            f"{a_new_page}\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    @patch("risc_generator.domain.contract.Faker")
    def test_givenAENContractPreAuthorize_whenGenerateHeaderText_thenReturnProperENText(self, faker_mock):
        # a_date
        a_year = 2022
        a_month = 1
        a_day = 2
        faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = fpq1_contract.generate_header_text()

        a_date = "January 2, 2022\n\n\n"
        a_client_number = "Client N: 1234567\n"
        a_vehicle = "AMaker - 2020\n"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            f"{a_date}"
            "ISSUE\n"
            f"{a_client_number}"
            "Policy / Term:\n"
            "001 / 12 month\n\n"
            "ALWAYS BY YOUR SIDE FOR YOUR INSURANCE\n\n"
            "Please find enclosed your insurance documents.\n"
            "We recommend that you read them carefully to ensure that they are correct.\n"
            "If an Important Instructions page is included with these documents, please read through it carefully "
            "because it contains crucial information regarding your coverage.\n"
            "Feel free to contact us if you have any questions or comments.\n\n"
            "CONTACT US\n"
            "Customer Service\n"
            "123 456-7890\n"
            "1 800 123-4567\n"
            "Fax: 012 345-6789\n"
            "service.client@assureur.ca\n"
            f"8 a.m. to 8 p.m.\n"
            f"Monday to Friday\n"
            f"8:30 a.m. to 4 p.m., Saturday\n"
            "Claims\n"
            "098 765-4321\n"
            "1 800 765-4321\n"
            "24/7 emergency\n"
            "Legal Assistance\n"
            "1 800 012-3456\n"
            f"8:30 a.m. to 7 p.m.\n"
            f"Monday to Thursday\n"
            f"8:30 a.m. to 5 p.m., Friday\n"
            "Your branch\n"
            "221 B Baker Street\n"
            "Ville (Province)\nA1A 1A1\n"
            f"8:30 a.m. to 5 p.m.\n"
            f"Monday to Friday\n"
            "assureur.ca\n"
            "Your Insurance Documents\n"
            "(Table of Contents)\n"
            "Important Instructions\n"
            "Automobile Insurance\n"
            "Policy number: 001\n"
            f"{a_vehicle}"
            f"Insurance Certificates\n"
            f"(Documents to be kept on file)\n"
            f"Client Advantages\n"
            f"(Description of your client benefits)\n"
            f"Wording and Endorsements\n"
            f"{a_new_page}\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    @patch("risc_generator.domain.contract.Faker")
    def test_givenAENContractBill_whenGenerateHeaderText_thenReturnProperENText(self, faker_mock):
        # a_date
        a_year = 2022
        a_month = 1
        a_day = 2
        faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_bill_payment_method,
            protections=self.a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = fpq1_contract.generate_header_text()

        a_date = "January 2, 2022\n\n\n"
        a_client_number = "Client N: 1234567\n"
        a_vehicle = "AMaker - 2020\n"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            f"{a_date}"
            "ISSUE\n"
            f"{a_client_number}"
            "Policy / Term:\n"
            "001 / 12 month\n\n"
            "ALWAYS BY YOUR SIDE FOR YOUR INSURANCE\n\n"
            "Please find enclosed your insurance documents.\n"
            "We recommend that you read them carefully to ensure that they are correct.\n"
            "If an Important Instructions page is included with these documents, please read through it carefully "
            "because it contains crucial information regarding your coverage.\n"
            "Feel free to contact us if you have any questions or comments.\n\n"
            "CONTACT US\n"
            "Customer Service\n"
            "123 456-7890\n"
            "1 800 123-4567\n"
            "Fax: 012 345-6789\n"
            "service.client@assureur.ca\n"
            f"8 a.m. to 8 p.m.\n"
            f"Monday to Friday\n"
            f"8:30 a.m. to 4 p.m., Saturday\n"
            "Claims\n"
            "098 765-4321\n"
            "1 800 765-4321\n"
            "24/7 emergency\n"
            "Legal Assistance\n"
            "1 800 012-3456\n"
            f"8:30 a.m. to 7 p.m.\n"
            f"Monday to Thursday\n"
            f"8:30 a.m. to 5 p.m., Friday\n"
            "Your branch\n"
            "221 B Baker Street\n"
            "Ville (Province)\nA1A 1A1\n"
            f"8:30 a.m. to 5 p.m.\n"
            f"Monday to Friday\n"
            "assureur.ca\n"
            "Your Insurance Documents\n"
            "(Table of Contents)\n"
            "Important Instructions\n"
            "Automobile Insurance\n"
            "Policy number: 001\n"
            f"{a_vehicle}"
            f"Insurance Certificates\n"
            f"(Documents to be kept on file)\n"
            f"Invoice\n"
            f"Client Advantages\n"
            f"(Description of your client benefits)\n"
            f"Wording and Endorsements\n"
            f"{a_new_page}\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)
