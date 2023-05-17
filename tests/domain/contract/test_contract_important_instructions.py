# pylint: disable=too-many-locals

import datetime
from unittest.mock import patch

from risc_generator import FPQ1Contract, Protections
from tests.domain.contract.contract_base import ContractTestBase

INCLUDE = "include"
EXCLUDE = "exclude"


class ContractImportantInstructionsTest(ContractTestBase):
    @patch("risc_generator.domain.contract.Faker")
    def test_givenAFRContractNoEndorsements_whenGenerateImportantInstructionText_thenReturnProperFRText(
        self, faker_mock
    ):
        # a_date
        a_year = 2022
        a_month = 1
        a_day = 2
        faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

        a_protections = Protections(protections=self.a_dict_of_protections.copy())

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fpq1_contract.generate_important_instructions_text()

        a_date = "Le 2 janvier 2022\n"
        a_general_phone_number_1_800 = "1 800 123-4567"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "INSTRUCTIONS IMPORTANTES\n\n"
            f"{a_date}"
            "Vous trouverez ci-dessous des instructions concernant des éléments très importants de votre police "
            "d'assurance et nous vous recommandons de les lire attentivement et d'y donner suite s'il y a lieu.\n\n"
            "Programme FIDÉLITÉ\n\n"
            "Parce que votre fidélité nous tient à coeur, nous sommes heureux de vous offrir des privilèges qui "
            "s'accumulent en même temps que vos années de fidélité, grâce à notre programme FIDÉLITÉ. "
            "Voici le détail de vos privilèges, que vous trouverez également dans votre Espace client.\n"
            "Votre fidélité reconnue: Nouveau client\n"
            "Vos privilèges:\n"
            "\t Offres exclusives chez nos partenaires\n"
            "\t Assistance juridique\n"
            "\t Service d'aide psychologique\n"
            "Cette liste représente l'ensemble des privilèges associés à votre fidélité reconnue. "
            "Veuillez noter que les nouveaux privilèges seront disponibles au "
            "moment du renouvellement de chacune des polices d'assurance détenues par un "
            "membre de votre maisonnée. Référez-vous aux Conditions "
            "particulières de vos divers contrats d'assurance détenus chez "
            "nous pour connaître le détail des protections applicables.\n"
            f"{a_new_page}\n"
            "\nActions à entreprendre\n\n"
            "Assurance auto\n"
            "\t Détachez et conservez avec vous vos certificats d'assurance.\n"
            "\t Détachez et conservez avec votre permis de conduire le certificat d'assurance pour location de "
            "voiture. Vous éviterez ainsi de débourser les frais d'assurance additionnels auprès de l'agence de "
            "location.\n"
            "\t Veuillez prendre connaissance de la section Conditions particulières de votre police d'assurance "
            "automobile du Québec, afin de vous assurer que vos couvertures répondent bien à vos besoins.\n"
            f"\t N'hésitez pas à joindre le service à la clientèle au {a_general_phone_number_1_800} "
            f"pour toute question relative à votre contrat.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    @patch("risc_generator.domain.contract.Faker")
    def test_givenAFRContractFAQ41_whenGenerateImportantInstructionText_thenReturnProperFRText(self, faker_mock):
        # a_date
        a_year = 2022
        a_month = 1
        a_day = 2
        faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

        dict_protections = self.a_dict_of_protections.copy()
        dict_protections.update({"FAQ41Coverage": INCLUDE})

        protections = Protections(protections=dict_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fpq1_contract.generate_important_instructions_text()

        a_date = "Le 2 janvier 2022\n"
        a_general_phone_number_1_800 = "1 800 123-4567"
        a_new_page = "<###NEW_PAGE###>"

        faq41_endorsement_text = "\t Congé de franchise en cas de perte totale ou de délit de fuite (auto)\n"

        expected = (
            "INSTRUCTIONS IMPORTANTES\n\n"
            f"{a_date}"
            "Vous trouverez ci-dessous des instructions concernant des éléments très importants de votre police "
            "d'assurance et nous vous recommandons de les lire attentivement et d'y donner suite s'il y a lieu.\n\n"
            "Programme FIDÉLITÉ\n\n"
            "Parce que votre fidélité nous tient à coeur, nous sommes heureux de vous offrir des privilèges qui "
            "s'accumulent en même temps que vos années de fidélité, grâce à notre programme FIDÉLITÉ. "
            "Voici le détail de vos privilèges, que vous trouverez également dans votre Espace client.\n"
            "Votre fidélité reconnue: Nouveau client\n"
            "Vos privilèges:\n"
            "\t Offres exclusives chez nos partenaires\n"
            "\t Assistance juridique\n"
            "\t Service d'aide psychologique\n"
            f"{faq41_endorsement_text}"
            "Cette liste représente l'ensemble des privilèges associés à votre fidélité reconnue. "
            "Veuillez noter que les nouveaux privilèges seront disponibles au "
            "moment du renouvellement de chacune des polices d'assurance détenues par un "
            "membre de votre maisonnée. Référez-vous aux Conditions "
            "particulières de vos divers contrats d'assurance détenus chez "
            "nous pour connaître le détail des protections applicables.\n"
            f"{a_new_page}\n"
            "\nActions à entreprendre\n\n"
            "Assurance auto\n"
            "\t Détachez et conservez avec vous vos certificats d'assurance.\n"
            "\t Détachez et conservez avec votre permis de conduire le certificat d'assurance pour location de "
            "voiture. Vous éviterez ainsi de débourser les frais d'assurance additionnels auprès de l'agence de "
            "location.\n"
            "\t Veuillez prendre connaissance de la section Conditions particulières de votre police d'assurance "
            "automobile du Québec, afin de vous assurer que vos couvertures répondent bien à vos besoins.\n"
            f"\t N'hésitez pas à joindre le service à la clientèle au {a_general_phone_number_1_800} "
            f"pour toute question relative à votre contrat.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    @patch("risc_generator.domain.contract.Faker")
    def test_givenAFRContractFAQ33_whenGenerateImportantInstructionText_thenReturnProperFRText(self, faker_mock):
        # a_date
        a_year = 2022
        a_month = 1
        a_day = 2
        faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

        dict_protections = self.a_dict_of_protections.copy()
        dict_protections.update({"FAQ33Coverage": INCLUDE})

        protections = Protections(protections=dict_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fpq1_contract.generate_important_instructions_text()

        a_date = "Le 2 janvier 2022\n"
        a_general_phone_number_1_800 = "1 800 123-4567"
        a_new_page = "<###NEW_PAGE###>"

        a_roadside_program_name = "ABC"
        a_roadside_phone_number = "1 877 012-3456"
        a_policy_number = "1234567-001"
        faq33_endorsement_text = (
            f"POLICE AUTOMOBILE N {a_policy_number}\n"
            f"Vous avez opté pour {a_roadside_program_name} assistance routière, qui vous procure des services "
            f"de dépannage partout au Canada et aux États-Unis, 24 heures sur 24, 365 jours par année.\n"
            f"Ainsi, trois semaines après la date de prise d'effet de l'avenant F.A.Q. N 33 Assurance des frais "
            f"de dépannage, vous recevrez une trousse pour chaque véhicule admissible, contenant entre autres "
            f"votre carte d'adhérent ainsi que votre guide de l'usager.\n"
            f"Dès que l'avenant F.A.Q. N 33 entrera en vigueur, vous pourrez bénéficier de ce service même si "
            f"vous n'avez pas reçu votre trousse {a_roadside_program_name} assistance routière. En cas de besoin, "
            f"il vous suffira de composer le {a_roadside_phone_number} (24 heures sur 24, 7 jours sur 7) "
            f"et de mentionner le numéro de police du véhicule couvert au préposé.\n"
        )

        expected = (
            "INSTRUCTIONS IMPORTANTES\n\n"
            f"{a_date}"
            "Vous trouverez ci-dessous des instructions concernant des éléments très importants de votre police "
            "d'assurance et nous vous recommandons de les lire attentivement et d'y donner suite s'il y a lieu.\n\n"
            "Programme FIDÉLITÉ\n\n"
            "Parce que votre fidélité nous tient à coeur, nous sommes heureux de vous offrir des privilèges qui "
            "s'accumulent en même temps que vos années de fidélité, grâce à notre programme FIDÉLITÉ. "
            "Voici le détail de vos privilèges, que vous trouverez également dans votre Espace client.\n"
            "Votre fidélité reconnue: Nouveau client\n"
            "Vos privilèges:\n"
            "\t Offres exclusives chez nos partenaires\n"
            "\t Assistance juridique\n"
            "\t Service d'aide psychologique\n"
            "Cette liste représente l'ensemble des privilèges associés à votre fidélité reconnue. "
            "Veuillez noter que les nouveaux privilèges seront disponibles au "
            "moment du renouvellement de chacune des polices d'assurance détenues par un "
            "membre de votre maisonnée. Référez-vous aux Conditions "
            "particulières de vos divers contrats d'assurance détenus chez "
            "nous pour connaître le détail des protections applicables.\n"
            "Avis à l'assuré\n"
            f"{faq33_endorsement_text}"
            f"{a_new_page}\n"
            "\nActions à entreprendre\n\n"
            "Assurance auto\n"
            "\t Détachez et conservez avec vous vos certificats d'assurance.\n"
            "\t Détachez et conservez avec votre permis de conduire le certificat d'assurance pour location de "
            "voiture. Vous éviterez ainsi de débourser les frais d'assurance additionnels auprès de l'agence de "
            "location.\n"
            "\t Veuillez prendre connaissance de la section Conditions particulières de votre police d'assurance "
            "automobile du Québec, afin de vous assurer que vos couvertures répondent bien à vos besoins.\n"
            f"\t N'hésitez pas à joindre le service à la clientèle au {a_general_phone_number_1_800} "
            f"pour toute question relative à votre contrat.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    @patch("risc_generator.domain.contract.Faker")
    def test_givenAFRContractFAQ5A_whenGenerateImportantInstructionText_thenReturnProperFRText(self, faker_mock):
        # a_date
        a_year = 2022
        a_month = 1
        a_day = 2
        faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

        dict_protections = self.a_dict_of_protections.copy()
        dict_protections.update({"FAQ5ACoverage": INCLUDE})

        protections = Protections(protections=dict_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fpq1_contract.generate_important_instructions_text()

        a_date = "Le 2 janvier 2022\n"
        a_general_phone_number_1_800 = "1 800 123-4567"
        a_new_page = "<###NEW_PAGE###>"

        a_location_car = "locateur"
        a_policy_number = "1234567-001"
        a_vehicle = "AMaker AModel 2020"
        faq5a_endorsement_text = (
            f"POLICE AUTOMOBILE N {a_policy_number} - Véhicule 1 : {a_vehicle}\n"
            f"Nous joignons une copie de votre police à remettre à votre {a_location_car}, s'il la demande. Elle se "
            f"trouve à la toute fin du présent envoi.\n"
        )

        expected = (
            "INSTRUCTIONS IMPORTANTES\n\n"
            f"{a_date}"
            "Vous trouverez ci-dessous des instructions concernant des éléments très importants de votre police "
            "d'assurance et nous vous recommandons de les lire attentivement et d'y donner suite s'il y a lieu.\n\n"
            "Programme FIDÉLITÉ\n\n"
            "Parce que votre fidélité nous tient à coeur, nous sommes heureux de vous offrir des privilèges qui "
            "s'accumulent en même temps que vos années de fidélité, grâce à notre programme FIDÉLITÉ. "
            "Voici le détail de vos privilèges, que vous trouverez également dans votre Espace client.\n"
            "Votre fidélité reconnue: Nouveau client\n"
            "Vos privilèges:\n"
            "\t Offres exclusives chez nos partenaires\n"
            "\t Assistance juridique\n"
            "\t Service d'aide psychologique\n"
            "Cette liste représente l'ensemble des privilèges associés à votre fidélité reconnue. "
            "Veuillez noter que les nouveaux privilèges seront disponibles au "
            "moment du renouvellement de chacune des polices d'assurance détenues par un "
            "membre de votre maisonnée. Référez-vous aux Conditions "
            "particulières de vos divers contrats d'assurance détenus chez "
            "nous pour connaître le détail des protections applicables.\n"
            "Avis à l'assuré\n"
            f"{faq5a_endorsement_text}"
            f"{a_new_page}\n"
            "\nActions à entreprendre\n\n"
            "Assurance auto\n"
            "\t Détachez et conservez avec vous vos certificats d'assurance.\n"
            "\t Détachez et conservez avec votre permis de conduire le certificat d'assurance pour location de "
            "voiture. Vous éviterez ainsi de débourser les frais d'assurance additionnels auprès de l'agence de "
            "location.\n"
            "\t Veuillez prendre connaissance de la section Conditions particulières de votre police d'assurance "
            "automobile du Québec, afin de vous assurer que vos couvertures répondent bien à vos besoins.\n"
            f"\t N'hésitez pas à joindre le service à la clientèle au {a_general_phone_number_1_800} "
            f"pour toute question relative à votre contrat.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    @patch("risc_generator.domain.contract.Faker")
    def test_givenAFRContractFAQ23A_whenGenerateImportantInstructionText_thenReturnProperFRText(self, faker_mock):
        # a_date
        a_year = 2022
        a_month = 1
        a_day = 2
        faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

        dict_protections = self.a_dict_of_protections.copy()
        dict_protections.update({"FAQ23ACoverage": INCLUDE})

        protections = Protections(protections=dict_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fpq1_contract.generate_important_instructions_text()

        a_date = "Le 2 janvier 2022\n"
        a_general_phone_number_1_800 = "1 800 123-4567"
        a_new_page = "<###NEW_PAGE###>"

        a_financed_car = "créancier"
        a_policy_number = "1234567-001"
        a_vehicle = "AMaker AModel 2020"
        faq23a_endorsement_text = (
            f"POLICE AUTOMOBILE N {a_policy_number} - Véhicule 1 : {a_vehicle}\n"
            f"Nous joignons une copie de votre police à remettre à votre {a_financed_car}, s'il la demande. Elle se "
            f"trouve à la toute fin du présent envoi.\n"
        )

        expected = (
            "INSTRUCTIONS IMPORTANTES\n\n"
            f"{a_date}"
            "Vous trouverez ci-dessous des instructions concernant des éléments très importants de votre police "
            "d'assurance et nous vous recommandons de les lire attentivement et d'y donner suite s'il y a lieu.\n\n"
            "Programme FIDÉLITÉ\n\n"
            "Parce que votre fidélité nous tient à coeur, nous sommes heureux de vous offrir des privilèges qui "
            "s'accumulent en même temps que vos années de fidélité, grâce à notre programme FIDÉLITÉ. "
            "Voici le détail de vos privilèges, que vous trouverez également dans votre Espace client.\n"
            "Votre fidélité reconnue: Nouveau client\n"
            "Vos privilèges:\n"
            "\t Offres exclusives chez nos partenaires\n"
            "\t Assistance juridique\n"
            "\t Service d'aide psychologique\n"
            "Cette liste représente l'ensemble des privilèges associés à votre fidélité reconnue. "
            "Veuillez noter que les nouveaux privilèges seront disponibles au "
            "moment du renouvellement de chacune des polices d'assurance détenues par un "
            "membre de votre maisonnée. Référez-vous aux Conditions "
            "particulières de vos divers contrats d'assurance détenus chez "
            "nous pour connaître le détail des protections applicables.\n"
            "Avis à l'assuré\n"
            f"{faq23a_endorsement_text}"
            f"{a_new_page}\n"
            "\nActions à entreprendre\n\n"
            "Assurance auto\n"
            "\t Détachez et conservez avec vous vos certificats d'assurance.\n"
            "\t Détachez et conservez avec votre permis de conduire le certificat d'assurance pour location de "
            "voiture. Vous éviterez ainsi de débourser les frais d'assurance additionnels auprès de l'agence de "
            "location.\n"
            "\t Veuillez prendre connaissance de la section Conditions particulières de votre police d'assurance "
            "automobile du Québec, afin de vous assurer que vos couvertures répondent bien à vos besoins.\n"
            f"\t N'hésitez pas à joindre le service à la clientèle au {a_general_phone_number_1_800} "
            f"pour toute question relative à votre contrat.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    @patch("risc_generator.domain.contract.Faker")
    def test_givenAFRContractFAQ33And23A_whenGenerateImportantInstructionText_thenReturnProperFRText(self, faker_mock):
        # a_date
        a_year = 2022
        a_month = 1
        a_day = 2
        faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

        dict_protections = self.a_dict_of_protections.copy()
        dict_protections.update({"FAQ33Coverage": INCLUDE})
        dict_protections.update({"FAQ23ACoverage": INCLUDE})

        protections = Protections(protections=dict_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fpq1_contract.generate_important_instructions_text()

        a_date = "Le 2 janvier 2022\n"
        a_general_phone_number_1_800 = "1 800 123-4567"
        a_new_page = "<###NEW_PAGE###>"

        a_financed_car = "créancier"
        a_policy_number = "1234567-001"
        a_vehicle = "AMaker AModel 2020"
        a_roadside_program_name = "ABC"
        a_roadside_phone_number = "1 877 012-3456"
        endorsements_text = (
            f"POLICE AUTOMOBILE N {a_policy_number}\n"
            f"Vous avez opté pour {a_roadside_program_name} assistance routière, qui vous procure des services "
            f"de dépannage partout au Canada et aux États-Unis, 24 heures sur 24, 365 jours par année.\n"
            f"Ainsi, trois semaines après la date de prise d'effet de l'avenant F.A.Q. N 33 Assurance des frais "
            f"de dépannage, vous recevrez une trousse pour chaque véhicule admissible, contenant entre autres "
            f"votre carte d'adhérent ainsi que votre guide de l'usager.\n"
            f"Dès que l'avenant F.A.Q. N 33 entrera en vigueur, vous pourrez bénéficier de ce service même si "
            f"vous n'avez pas reçu votre trousse {a_roadside_program_name} assistance routière. En cas de besoin, "
            f"il vous suffira de composer le {a_roadside_phone_number} (24 heures sur 24, 7 jours sur 7) "
            f"et de mentionner le numéro de police du véhicule couvert au préposé.\n"
            f"POLICE AUTOMOBILE N {a_policy_number} - Véhicule 1 : {a_vehicle}\n"
            f"Nous joignons une copie de votre police à remettre à votre {a_financed_car}, s'il la demande. Elle se "
            f"trouve à la toute fin du présent envoi.\n"
        )

        expected = (
            "INSTRUCTIONS IMPORTANTES\n\n"
            f"{a_date}"
            "Vous trouverez ci-dessous des instructions concernant des éléments très importants de votre police "
            "d'assurance et nous vous recommandons de les lire attentivement et d'y donner suite s'il y a lieu.\n\n"
            "Programme FIDÉLITÉ\n\n"
            "Parce que votre fidélité nous tient à coeur, nous sommes heureux de vous offrir des privilèges qui "
            "s'accumulent en même temps que vos années de fidélité, grâce à notre programme FIDÉLITÉ. "
            "Voici le détail de vos privilèges, que vous trouverez également dans votre Espace client.\n"
            "Votre fidélité reconnue: Nouveau client\n"
            "Vos privilèges:\n"
            "\t Offres exclusives chez nos partenaires\n"
            "\t Assistance juridique\n"
            "\t Service d'aide psychologique\n"
            "Cette liste représente l'ensemble des privilèges associés à votre fidélité reconnue. "
            "Veuillez noter que les nouveaux privilèges seront disponibles au "
            "moment du renouvellement de chacune des polices d'assurance détenues par un "
            "membre de votre maisonnée. Référez-vous aux Conditions "
            "particulières de vos divers contrats d'assurance détenus chez "
            "nous pour connaître le détail des protections applicables.\n"
            "Avis à l'assuré\n"
            f"{endorsements_text}"
            f"{a_new_page}\n"
            "\nActions à entreprendre\n\n"
            "Assurance auto\n"
            "\t Détachez et conservez avec vous vos certificats d'assurance.\n"
            "\t Détachez et conservez avec votre permis de conduire le certificat d'assurance pour location de "
            "voiture. Vous éviterez ainsi de débourser les frais d'assurance additionnels auprès de l'agence de "
            "location.\n"
            "\t Veuillez prendre connaissance de la section Conditions particulières de votre police d'assurance "
            "automobile du Québec, afin de vous assurer que vos couvertures répondent bien à vos besoins.\n"
            f"\t N'hésitez pas à joindre le service à la clientèle au {a_general_phone_number_1_800} "
            f"pour toute question relative à votre contrat.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    @patch("risc_generator.domain.contract.Faker")
    def test_givenAENContractNoEndorsements_whenGenerateImportantInstructionText_thenReturnProperENText(
        self, faker_mock
    ):
        # a_date
        a_year = 2022
        a_month = 1
        a_day = 2
        faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

        a_protections = Protections(protections=self.a_dict_of_protections.copy())

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = fpq1_contract.generate_important_instructions_text()

        a_date = "January 2, 2022\n"
        a_general_phone_number_1_800 = "1 800 123-4567"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "IMPORTANT INSTRUCTIONS\n\n"
            f"{a_date}"
            "Please find hereafter instructions on very important parts of your insurance policy; we suggest that "
            "you read them carefully and take any required action, if necessary.\n\n"
            "FIDELITY Program\n\n"
            "Because we appreciate your loyalty, we're pleased to offer you privileges that accumulate with your "
            "years of loyalty, thanks to our FIDELITY Program. Here are the details regarding your privileges, "
            "which you can also find in your Client Centre.\n"
            "Your recognized loyalty: New client\n"
            "Your privileges:\n"
            "\t Exclusive partner offers\n"
            "\t Legal assistance\n"
            "\t Psychological assistance service\n"
            "This list contains all the privileges associated with your recognized loyalty. Please note that the new "
            "privileges will be available at the renewal of each insurance policy held by a member of your household. "
            "Please see the Declarations or Coverage Summary Page(s) of your various insurance contracts held with "
            "us to learn more about applicable coverage details.\n"
            f"{a_new_page}\n"
            "\nActions Required\n\n"
            "Automobile insurance\n"
            "\t Detach and keep your insurance certificates with you.\n"
            "\t Detach and keep the automobile rental certificate with your driver's licence. This way, you will "
            "avoid paying additional insurance fees to the car rental agency.\n"
            "\t Please read the Coverage Summary section of your Quebec automobile insurance contract to ensure "
            "that your coverages are well-suited to your needs.\n"
            f"\t Don't hesitate to contact customer service at {a_general_phone_number_1_800} for any questions "
            f"regarding your contract.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    @patch("risc_generator.domain.contract.Faker")
    def test_givenAENContractFAQ41_whenGenerateImportantInstructionText_thenReturnProperENText(self, faker_mock):
        # a_date
        a_year = 2022
        a_month = 1
        a_day = 2
        faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

        dict_protections = self.a_dict_of_protections.copy()
        dict_protections.update({"FAQ41Coverage": INCLUDE})

        protections = Protections(protections=dict_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = fpq1_contract.generate_important_instructions_text()

        a_date = "January 2, 2022\n"
        a_general_phone_number_1_800 = "1 800 123-4567"
        a_new_page = "<###NEW_PAGE###>"

        faq41_endorsement_text = "\t No deductible to pay in the case of a total loss or hit-and-run (auto)\n"

        expected = (
            "IMPORTANT INSTRUCTIONS\n\n"
            f"{a_date}"
            "Please find hereafter instructions on very important parts of your insurance policy; we suggest that "
            "you read them carefully and take any required action, if necessary.\n\n"
            "FIDELITY Program\n\n"
            "Because we appreciate your loyalty, we're pleased to offer you privileges that accumulate with your "
            "years of loyalty, thanks to our FIDELITY Program. Here are the details regarding your privileges, "
            "which you can also find in your Client Centre.\n"
            "Your recognized loyalty: New client\n"
            "Your privileges:\n"
            "\t Exclusive partner offers\n"
            "\t Legal assistance\n"
            "\t Psychological assistance service\n"
            f"{faq41_endorsement_text}"
            "This list contains all the privileges associated with your recognized loyalty. Please note that the new "
            "privileges will be available at the renewal of each insurance policy held by a member of your household. "
            "Please see the Declarations or Coverage Summary Page(s) of your various insurance contracts held with "
            "us to learn more about applicable coverage details.\n"
            f"{a_new_page}\n"
            "\nActions Required\n\n"
            "Automobile insurance\n"
            "\t Detach and keep your insurance certificates with you.\n"
            "\t Detach and keep the automobile rental certificate with your driver's licence. This way, you will "
            "avoid paying additional insurance fees to the car rental agency.\n"
            "\t Please read the Coverage Summary section of your Quebec automobile insurance contract to ensure "
            "that your coverages are well-suited to your needs.\n"
            f"\t Don't hesitate to contact customer service at {a_general_phone_number_1_800} for any questions "
            f"regarding your contract.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    @patch("risc_generator.domain.contract.Faker")
    def test_givenAENContractFAQ33_whenGenerateImportantInstructionText_thenReturnProperENText(self, faker_mock):
        # a_date
        a_year = 2022
        a_month = 1
        a_day = 2
        faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

        dict_protections = self.a_dict_of_protections.copy()
        dict_protections.update({"FAQ33Coverage": INCLUDE})

        protections = Protections(protections=dict_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = fpq1_contract.generate_important_instructions_text()

        a_date = "January 2, 2022\n"
        a_general_phone_number_1_800 = "1 800 123-4567"
        a_new_page = "<###NEW_PAGE###>"

        a_roadside_program_name = "ABC"
        a_roadside_phone_number = "1 877 012-3456"
        a_policy_number = "1234567-001"
        faq33_endorsement_text = (
            f"AUTOMOBILE POLICY No {a_policy_number}\n"
            f"You have chosen {a_roadside_program_name} Roadside Assistance, which provides you with 24-hour "
            f"roadside assistance throughout Canada and the United States, 365 days a year.\n"
            f"Therefore, three weeks after the effective date of the Q.E.F. endorsement N 33 Roadside Assistance "
            f"Coverage, you will receive a kit for each eligible vehicle, including your membership card and your "
            f"user's guide.\n"
            f"As soon as the endorsement Q.E.F. N 33 comes into effect, you will be able to benefit from "
            f"this service even if you have not received your {a_roadside_program_name} roadside assistance kit."
            f"In case of need, simply call {a_roadside_phone_number} (24 hours a day, 7 days a week) "
            f"and mention the policy number of the covered vehicle to the agent.\n"
        )

        expected = (
            "IMPORTANT INSTRUCTIONS\n\n"
            f"{a_date}"
            "Please find hereafter instructions on very important parts of your insurance policy; we suggest that "
            "you read them carefully and take any required action, if necessary.\n\n"
            "FIDELITY Program\n\n"
            "Because we appreciate your loyalty, we're pleased to offer you privileges that accumulate with your "
            "years of loyalty, thanks to our FIDELITY Program. Here are the details regarding your privileges, "
            "which you can also find in your Client Centre.\n"
            "Your recognized loyalty: New client\n"
            "Your privileges:\n"
            "\t Exclusive partner offers\n"
            "\t Legal assistance\n"
            "\t Psychological assistance service\n"
            "This list contains all the privileges associated with your recognized loyalty. Please note that the new "
            "privileges will be available at the renewal of each insurance policy held by a member of your household. "
            "Please see the Declarations or Coverage Summary Page(s) of your various insurance contracts held with "
            "us to learn more about applicable coverage details.\n"
            "Notice to the insured\n"
            f"{faq33_endorsement_text}"
            f"{a_new_page}\n"
            "\nActions Required\n\n"
            "Automobile insurance\n"
            "\t Detach and keep your insurance certificates with you.\n"
            "\t Detach and keep the automobile rental certificate with your driver's licence. This way, you will "
            "avoid paying additional insurance fees to the car rental agency.\n"
            "\t Please read the Coverage Summary section of your Quebec automobile insurance contract to ensure "
            "that your coverages are well-suited to your needs.\n"
            f"\t Don't hesitate to contact customer service at {a_general_phone_number_1_800} for any questions "
            f"regarding your contract.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    @patch("risc_generator.domain.contract.Faker")
    def test_givenAENContractFAQ5A_whenGenerateImportantInstructionText_thenReturnProperENText(self, faker_mock):
        # a_date
        a_year = 2022
        a_month = 1
        a_day = 2
        faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

        dict_protections = self.a_dict_of_protections.copy()
        dict_protections.update({"FAQ5ACoverage": INCLUDE})

        protections = Protections(protections=dict_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = fpq1_contract.generate_important_instructions_text()

        a_date = "January 2, 2022\n"
        a_general_phone_number_1_800 = "1 800 123-4567"
        a_new_page = "<###NEW_PAGE###>"

        a_location_car = "locator"
        a_policy_number = "1234567-001"
        a_vehicle = "AMaker AModel 2020"
        faq5a_endorsement_text = (
            f"AUTOMOBILE POLICY No {a_policy_number} - Vehicle 1 : {a_vehicle}\n"
            f"We are enclosing a copy of your policy to give to your {a_location_car}, "
            f"if requested. It is included at the very end of this mailing.\n"
        )

        expected = (
            "IMPORTANT INSTRUCTIONS\n\n"
            f"{a_date}"
            "Please find hereafter instructions on very important parts of your insurance policy; we suggest that "
            "you read them carefully and take any required action, if necessary.\n\n"
            "FIDELITY Program\n\n"
            "Because we appreciate your loyalty, we're pleased to offer you privileges that accumulate with your "
            "years of loyalty, thanks to our FIDELITY Program. Here are the details regarding your privileges, "
            "which you can also find in your Client Centre.\n"
            "Your recognized loyalty: New client\n"
            "Your privileges:\n"
            "\t Exclusive partner offers\n"
            "\t Legal assistance\n"
            "\t Psychological assistance service\n"
            "This list contains all the privileges associated with your recognized loyalty. Please note that the new "
            "privileges will be available at the renewal of each insurance policy held by a member of your household. "
            "Please see the Declarations or Coverage Summary Page(s) of your various insurance contracts held with "
            "us to learn more about applicable coverage details.\n"
            "Notice to the insured\n"
            f"{faq5a_endorsement_text}"
            f"{a_new_page}\n"
            "\nActions Required\n\n"
            "Automobile insurance\n"
            "\t Detach and keep your insurance certificates with you.\n"
            "\t Detach and keep the automobile rental certificate with your driver's licence. This way, you will "
            "avoid paying additional insurance fees to the car rental agency.\n"
            "\t Please read the Coverage Summary section of your Quebec automobile insurance contract to ensure "
            "that your coverages are well-suited to your needs.\n"
            f"\t Don't hesitate to contact customer service at {a_general_phone_number_1_800} for any questions "
            f"regarding your contract.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    @patch("risc_generator.domain.contract.Faker")
    def test_givenAENContractFAQ23A_whenGenerateImportantInstructionText_thenReturnProperENText(self, faker_mock):
        # a_date
        a_year = 2022
        a_month = 1
        a_day = 2
        faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

        dict_protections = self.a_dict_of_protections.copy()
        dict_protections.update({"FAQ23ACoverage": INCLUDE})

        protections = Protections(protections=dict_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = fpq1_contract.generate_important_instructions_text()

        a_date = "January 2, 2022\n"
        a_general_phone_number_1_800 = "1 800 123-4567"
        a_new_page = "<###NEW_PAGE###>"

        a_financed_car = "creditor"
        a_policy_number = "1234567-001"
        a_vehicle = "AMaker AModel 2020"
        faq23a_endorsement_text = (
            f"AUTOMOBILE POLICY No {a_policy_number} - Vehicle 1 : {a_vehicle}\n"
            f"We are enclosing a copy of your policy to give to your {a_financed_car}, "
            f"if requested. It is included at the very end of this mailing.\n"
        )

        expected = (
            "IMPORTANT INSTRUCTIONS\n\n"
            f"{a_date}"
            "Please find hereafter instructions on very important parts of your insurance policy; we suggest that "
            "you read them carefully and take any required action, if necessary.\n\n"
            "FIDELITY Program\n\n"
            "Because we appreciate your loyalty, we're pleased to offer you privileges that accumulate with your "
            "years of loyalty, thanks to our FIDELITY Program. Here are the details regarding your privileges, "
            "which you can also find in your Client Centre.\n"
            "Your recognized loyalty: New client\n"
            "Your privileges:\n"
            "\t Exclusive partner offers\n"
            "\t Legal assistance\n"
            "\t Psychological assistance service\n"
            "This list contains all the privileges associated with your recognized loyalty. Please note that the new "
            "privileges will be available at the renewal of each insurance policy held by a member of your household. "
            "Please see the Declarations or Coverage Summary Page(s) of your various insurance contracts held with "
            "us to learn more about applicable coverage details.\n"
            "Notice to the insured\n"
            f"{faq23a_endorsement_text}"
            f"{a_new_page}\n"
            "\nActions Required\n\n"
            "Automobile insurance\n"
            "\t Detach and keep your insurance certificates with you.\n"
            "\t Detach and keep the automobile rental certificate with your driver's licence. This way, you will "
            "avoid paying additional insurance fees to the car rental agency.\n"
            "\t Please read the Coverage Summary section of your Quebec automobile insurance contract to ensure "
            "that your coverages are well-suited to your needs.\n"
            f"\t Don't hesitate to contact customer service at {a_general_phone_number_1_800} for any questions "
            f"regarding your contract.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)
