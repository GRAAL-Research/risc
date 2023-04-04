from risc_generator.content import fr, en
from tests.domain.contract.contract_base import ContractTestBase

INCLUDE = "include"
EXCLUDE = "exclude"


class ContractDeclarationTest(ContractTestBase):
    def test_givenAFRContract_whenGenerateDivulgationText_thenReturnProperFRText(self):
        actual = fr.declaration_articles.generate_divulgation_text()

        a_website = "assureur.ca"
        a_insurer_name = "Assureur"
        a_insurer_address = "221 B Baker Street\nVille (Province)\nA1A 1A1"

        expected = (
            "DIVULGATION\n\n"
            "AVIS CONCERNANT LA PROTECTION DES RENSEIGNEMENTS PERSONNELS\n"
            f"{a_insurer_name} traite de façon confidentielle les renseignements personnels "
            f"qu'elle détient sur vous.\n"
            f"Objet de votre dossier\n"
            f"Nous recueillons et utilisons les renseignements personnels qui vous concernent dans le but de "
            f"gérer votre dossier d'assurance de dommages.\n"
            f"Sécurité\n"
            f"Vos renseignements personnels sont conservés à nos bureaux et protégés par des standards de "
            f"sécurité élevés. Seuls nos employés, mandataires, partenaires de distribution et fournisseurs "
            f"de services peuvent y avoir accès et ce, uniquement lorsque requis par leurs fonctions, mandats "
            f"ou contrats.\n"
            f"{a_insurer_name} peut faire affaires avec un (ou des) fournisseur(s) de services basés "
            f"à l'extérieur du Québec. Ainsi, il est possible que certains de vos renseignements personnels "
            f"détenus par {a_insurer_name} puissent être hébergés à l'extérieur du Québec et être régis par les "
            f"lois applicables à des pays ou états étrangers.\n"
            f"Accès et rectification\n"
            f"Pour avoir accès à votre dossier ou en demander la rectification, faites-en la "
            f"demande à l'adresse suivante :\n"
            f"{a_insurer_name}\n"
            f"a/s du Service d'accès à l'information\n"
            f"{a_insurer_address}\n"
            f"Offre de service\n"
            f"Il se peut que {a_insurer_name}, ses filiales et représentants autorisés "
            f"utilisent vos renseignements nominatifs pour vous informer des produits et services "
            f"susceptibles de vous intéresser. Si toutefois vous ne désirez pas recevoir ce type "
            f"d'information, écrivez-nous à l'adresse ci-dessus.\n"
            f"Pour plus d'informations sur nos pratiques en matière de protection des renseignements "
            f"personnels, consultez notre Énoncé de confidentialité des renseignements personnels sur "
            f"{a_website}/fr/protection-renseignements-personnels.\n"
            f"Votre agent offre exclusivement les produits de {a_insurer_name} et il "
            f"ne reçoit aucune commission.\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContract_whenGenerateDivulgationText_thenReturnProperENText(self):
        actual = en.declaration_articles.generate_divulgation_text()

        a_website = "assureur.ca"
        a_insurer_name = "Assureur"
        a_insurer_address = "221 B Baker Street\nVille (Province)\nA1A 1A1"

        expected = (
            "DISCLOSURE\n\n"
            "NOTICE CONCERNING THE PROTECTION OF PERSONAL INFORMATION\n"
            f"{a_insurer_name} protects the confidentiality of your personal information.\n"
            f"PURPOSE OF YOUR FILE\n"
            f"We collect and use your personal information to manage your Property and Casualty insurance file.\n"
            f"SECURITY\n"
            f"Your personal information is stored at our offices and protected by high security measures. Only "
            f"our employees, mandataries, distribution partners and service providers may access your personal "
            f"information, and solely when such access is required to perform their duties, carry out their "
            f"mandate or fulfill their service contract.\n"
            f"{a_insurer_name} may do business with one or more service providers based outside of Quebec. "
            f"It is therefore possible that some of your personal information held by {a_insurer_name} may be "
            f"stored outside of Quebec and governed by the laws of foreign countries or states.\n"
            f"ACCESS AND CORRECTION\n"
            f"To access your file or make a correction to it, send your request in writing to the following address:\n"
            f"{a_insurer_name}\n"
            f"c/o Access to Information Service\n"
            f"{a_insurer_address}\n"
            f"SERVICE OFFERING\n"
            f"{a_insurer_name}, its subsidiaries and their authorized representatives may use your personal "
            f"information to inform you of products and services that may be of interest to you. If, however, "
            f"you do not wish to receive this type of information, please write to us at the address above.\n"
            f"For more information about our personal information protection practices, refer to our personal "
            f"information protection statement at {a_website}/en/personal-information-protection.\n"
            f"Your agent offers {a_insurer_name} products on an exclusive basis and does not receive any commission.\n"
        )

        self.assertEqual(expected, actual)
