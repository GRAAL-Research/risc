# pylint: disable=too-many-locals

from risc_generator import Protections, FPQ1Contract, Premium
from risc_generator.content import fr
from tests.domain.contract.contract_base import ContractTestBase

INCLUDE = "include"
EXCLUDE = "exclude"


class ContractDeclarationTest(ContractTestBase):
    def test_givenAFRContractLiabilityOnly_whenGenerateItem4Text_thenReturnProperFRText(self):
        a_liability_coverage_premium = 1
        protection_premiums = {"LiabilityCoveragePremium": a_liability_coverage_premium}
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB2Coverage": EXCLUDE,
            "PropertyDamageB3Coverage": EXCLUDE,
            "PropertyDamageB4Coverage": EXCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDÉLITÉ"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Article 4. GARANTIES / RISQUES : Les risques couverts par le contrat d'assurance sont ceux "
            "pour lesquels un montant d'assurance, une franchise ou une prime d'assurance est écrit au tableau "
            "ci-dessous. Ils sont couverts aux conditions énoncées dans le contrat d'assurance.\n"
            "PRIME\n"
            "\t Chapitre A - RESPONSABILITÉ CIVILE -\n"
            "Dommages matériels ou dommages corporels causés à d'autres personnes - Montant : 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Chapitre B - DOMMAGES AUX VÉHICULES ASSURÉS\n"
            "Protection 1 : Tous risques Non couvert\n"
            "Protection 2 : Risques de collision et de renversement Non couvert\n"
            "Protection 3 : Tous les risques sauf collision ou renversement Non couvert\n"
            "Protection 4 : Risques spécifiques Non couvert\n"
            f"{a_new_page}\n"
            f"\t Programme {fidelity_program_name}\n"
            f"F.A.Q. N 41\n"
            f"- Modification aux franchises (Chapitre B) : Incluse\n"
            f"Cet avenant apporte les modifications suivantes aux franchises du chapitre B :\n"
            f"\t - Suppression de la franchise, pour un délit de fuite s'il y a eu un rapport de police.\n"
            f"\t - Suppression de la franchise, pour une perte totale.\n"
            f"\t - Suppression de la franchise, pour une réparation de pare-brise sauf lors de son remplacement.\n"
            f"\t - Si vous êtes victime d'un sinistre qui affecte deux produits ou plus, assurés à "
            f"{a_insurer_name}, vous n'aurez qu'une seule franchise à payer, soit la plus élevée.\n"
            "Date d'échéance de prime : selon le mode de paiement convenu\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractLiabilityWithB1_whenGenerateItem4Text_thenReturnProperFRText(self):
        a_liability_coverage_premium = 1
        a_b1_premium = 2
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB1CoveragePremium": a_b1_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": 250,
            "PropertyDamageB2Coverage": EXCLUDE,
            "PropertyDamageB3Coverage": EXCLUDE,
            "PropertyDamageB4Coverage": EXCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDÉLITÉ"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Article 4. GARANTIES / RISQUES : Les risques couverts par le contrat d'assurance sont ceux "
            "pour lesquels un montant d'assurance, une franchise ou une prime d'assurance est écrit au tableau "
            "ci-dessous. Ils sont couverts aux conditions énoncées dans le contrat d'assurance.\n"
            "PRIME\n"
            "\t Chapitre A - RESPONSABILITÉ CIVILE -\n"
            "Dommages matériels ou dommages corporels causés à d'autres personnes - Montant : 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Chapitre B - DOMMAGES AUX VÉHICULES ASSURÉS\n"
            "Protection 1 : Tous risques - Franchise 250$ par sinistre 2$\n"
            "Protection 2 : Risques de collision et de renversement Non couvert\n"
            "Protection 3 : Tous les risques sauf collision ou renversement Non couvert\n"
            "Protection 4 : Risques spécifiques Non couvert\n"
            f"{a_new_page}\n"
            f"\t Programme {fidelity_program_name}\n"
            f"F.A.Q. N 41\n"
            f"- Modification aux franchises (Chapitre B) : Incluse\n"
            f"Cet avenant apporte les modifications suivantes aux franchises du chapitre B :\n"
            f"\t - Suppression de la franchise, pour un délit de fuite s'il y a eu un rapport de police.\n"
            f"\t - Suppression de la franchise, pour une perte totale.\n"
            f"\t - Suppression de la franchise, pour une réparation de pare-brise sauf lors de son remplacement.\n"
            f"\t - Si vous êtes victime d'un sinistre qui affecte deux produits ou plus, assurés à "
            f"{a_insurer_name}, vous n'aurez qu'une seule franchise à payer, soit la plus élevée.\n"
            "Date d'échéance de prime : selon le mode de paiement convenu\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractLiabilityWithB2B3_whenGenerateItem4Text_thenReturnProperFRText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDÉLITÉ"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Article 4. GARANTIES / RISQUES : Les risques couverts par le contrat d'assurance sont ceux "
            "pour lesquels un montant d'assurance, une franchise ou une prime d'assurance est écrit au tableau "
            "ci-dessous. Ils sont couverts aux conditions énoncées dans le contrat d'assurance.\n"
            "PRIME\n"
            "\t Chapitre A - RESPONSABILITÉ CIVILE -\n"
            "Dommages matériels ou dommages corporels causés à d'autres personnes - Montant : 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Chapitre B - DOMMAGES AUX VÉHICULES ASSURÉS\n"
            "Protection 1 : Tous risques Incluse\n"
            "Protection 2 : Risques de collision et de renversement - Franchise 250$ par sinistre 2$\n"
            "Protection 3 : Tous les risques sauf collision ou renversement - Franchise 250$ par sinistre 3$\n"
            "Protection 4 : Risques spécifiques Non couvert\n"
            f"{a_new_page}\n"
            f"\t Programme {fidelity_program_name}\n"
            f"F.A.Q. N 41\n"
            f"- Modification aux franchises (Chapitre B) : Incluse\n"
            f"Cet avenant apporte les modifications suivantes aux franchises du chapitre B :\n"
            f"\t - Suppression de la franchise, pour un délit de fuite s'il y a eu un rapport de police.\n"
            f"\t - Suppression de la franchise, pour une perte totale.\n"
            f"\t - Suppression de la franchise, pour une réparation de pare-brise sauf lors de son remplacement.\n"
            f"\t - Si vous êtes victime d'un sinistre qui affecte deux produits ou plus, assurés à "
            f"{a_insurer_name}, vous n'aurez qu'une seule franchise à payer, soit la plus élevée.\n"
            "Date d'échéance de prime : selon le mode de paiement convenu\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractLiabilityWithB2B4_whenGenerateItem4Text_thenReturnProperFRText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b4_premium = 3
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB4CoveragePremium": a_b4_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": EXCLUDE,
            "PropertyDamageB4Coverage": 250,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDÉLITÉ"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Article 4. GARANTIES / RISQUES : Les risques couverts par le contrat d'assurance sont ceux "
            "pour lesquels un montant d'assurance, une franchise ou une prime d'assurance est écrit au tableau "
            "ci-dessous. Ils sont couverts aux conditions énoncées dans le contrat d'assurance.\n"
            "PRIME\n"
            "\t Chapitre A - RESPONSABILITÉ CIVILE -\n"
            "Dommages matériels ou dommages corporels causés à d'autres personnes - Montant : 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Chapitre B - DOMMAGES AUX VÉHICULES ASSURÉS\n"
            "Protection 1 : Tous risques Incluse\n"
            "Protection 2 : Risques de collision et de renversement - Franchise 250$ par sinistre 2$\n"
            "Protection 3 : Tous les risques sauf collision ou renversement Non couvert\n"
            "Protection 4 : Risques spécifiques - Franchise 250$ par sinistre 3$\n"
            f"{a_new_page}\n"
            f"\t Programme {fidelity_program_name}\n"
            f"F.A.Q. N 41\n"
            f"- Modification aux franchises (Chapitre B) : Incluse\n"
            f"Cet avenant apporte les modifications suivantes aux franchises du chapitre B :\n"
            f"\t - Suppression de la franchise, pour un délit de fuite s'il y a eu un rapport de police.\n"
            f"\t - Suppression de la franchise, pour une perte totale.\n"
            f"\t - Suppression de la franchise, pour une réparation de pare-brise sauf lors de son remplacement.\n"
            f"\t - Si vous êtes victime d'un sinistre qui affecte deux produits ou plus, assurés à "
            f"{a_insurer_name}, vous n'aurez qu'une seule franchise à payer, soit la plus élevée.\n"
            "Date d'échéance de prime : selon le mode de paiement convenu\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractWithEndorsementFAQ33_whenGenerateItem4Text_thenReturnProperFRText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ33CoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ33Coverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDÉLITÉ"
        a_new_page = "<###NEW_PAGE###>"
        a_roadside_program_name = "ABC"

        expected = (
            "Article 4. GARANTIES / RISQUES : Les risques couverts par le contrat d'assurance sont ceux "
            "pour lesquels un montant d'assurance, une franchise ou une prime d'assurance est écrit au tableau "
            "ci-dessous. Ils sont couverts aux conditions énoncées dans le contrat d'assurance.\n"
            "PRIME\n"
            "\t Chapitre A - RESPONSABILITÉ CIVILE -\n"
            "Dommages matériels ou dommages corporels causés à d'autres personnes - Montant : 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Chapitre B - DOMMAGES AUX VÉHICULES ASSURÉS\n"
            "Protection 1 : Tous risques Incluse\n"
            "Protection 2 : Risques de collision et de renversement - Franchise 250$ par sinistre 2$\n"
            "Protection 3 : Tous les risques sauf collision ou renversement - Franchise 250$ par sinistre 3$\n"
            "Protection 4 : Risques spécifiques Non couvert\n"
            f"{a_new_page}\n"
            "Avenant(s) : F.A.Q. N 33 - Assurance pour les frais d'assistance routière\n"
            f"{a_roadside_program_name} Programme d'assistance routière, disponible 24 heures sur 24, 7 jours sur 7\n"
            f"Rayon maximum 50 km -\n"
            f"En cas de panne, la distance de remorquage est haussée à 100 km dans le parc des Laurentides, "
            f"150 km dans le parc de la Vérendrye et 100 km dans le parc national de la Gaspésie\n"
            f"Nombre d'événements maximum par année d'assurance 4 4$\n"
            f"Limite par dépannage 60$(1) - Pour un remorquage ou un véhicule enlisé, cette limite est haussée à "
            f"100$(1)\n"
            f"Limite par année d'assurance 400$(1)\n"
            f"(1) Ces limites s'appliquent uniquement lorsque, de façon exceptionnelle, le service de dépannage ou de "
            f"remorquage n'est pas disponible par le programme d'assistance routière\n"
            f"Consultez votre brochure pour connaître tous les services additionnels qui vous sont offerts\n"
            f"\t Programme {fidelity_program_name}\n"
            f"F.A.Q. N 41\n"
            f"- Modification aux franchises (Chapitre B) : Incluse\n"
            f"Cet avenant apporte les modifications suivantes aux franchises du chapitre B :\n"
            f"\t - Suppression de la franchise, pour un délit de fuite s'il y a eu un rapport de police.\n"
            f"\t - Suppression de la franchise, pour une perte totale.\n"
            f"\t - Suppression de la franchise, pour une réparation de pare-brise sauf lors de son remplacement.\n"
            f"\t - Si vous êtes victime d'un sinistre qui affecte deux produits ou plus, assurés à "
            f"{a_insurer_name}, vous n'aurez qu'une seule franchise à payer, soit la plus élevée.\n"
            "Date d'échéance de prime : selon le mode de paiement convenu\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractWithEndorsementFAQ20A_whenGenerateItem4Text_thenReturnProperFRText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ20ACoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ20ACoverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDÉLITÉ"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Article 4. GARANTIES / RISQUES : Les risques couverts par le contrat d'assurance sont ceux "
            "pour lesquels un montant d'assurance, une franchise ou une prime d'assurance est écrit au tableau "
            "ci-dessous. Ils sont couverts aux conditions énoncées dans le contrat d'assurance.\n"
            "PRIME\n"
            "\t Chapitre A - RESPONSABILITÉ CIVILE -\n"
            "Dommages matériels ou dommages corporels causés à d'autres personnes - Montant : 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Chapitre B - DOMMAGES AUX VÉHICULES ASSURÉS\n"
            "Protection 1 : Tous risques Incluse\n"
            "Protection 2 : Risques de collision et de renversement - Franchise 250$ par sinistre 2$\n"
            "Protection 3 : Tous les risques sauf collision ou renversement - Franchise 250$ par sinistre 3$\n"
            "Protection 4 : Risques spécifiques Non couvert\n"
            f"{a_new_page}\n"
            "Avenant(s) : F.A.Q. N 20a - Frais de déplacement (formule étendue) (Chapitre B) 4$\n"
            "Frais de déplacement 50$ par jour, limitation totale de 1500$ par sinistre\n"
            "Autres frais couverts au cours d'un voyage - 750$\n"
            f"\t Programme {fidelity_program_name}\n"
            f"F.A.Q. N 41\n"
            f"- Modification aux franchises (Chapitre B) : Incluse\n"
            f"Cet avenant apporte les modifications suivantes aux franchises du chapitre B :\n"
            f"\t - Suppression de la franchise, pour un délit de fuite s'il y a eu un rapport de police.\n"
            f"\t - Suppression de la franchise, pour une perte totale.\n"
            f"\t - Suppression de la franchise, pour une réparation de pare-brise sauf lors de son remplacement.\n"
            f"\t - Si vous êtes victime d'un sinistre qui affecte deux produits ou plus, assurés à "
            f"{a_insurer_name}, vous n'aurez qu'une seule franchise à payer, soit la plus élevée.\n"
            "Date d'échéance de prime : selon le mode de paiement convenu\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractWithEndorsementFAQ20_whenGenerateItem4Text_thenReturnProperFRText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ20CoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ20Coverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDÉLITÉ"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Article 4. GARANTIES / RISQUES : Les risques couverts par le contrat d'assurance sont ceux "
            "pour lesquels un montant d'assurance, une franchise ou une prime d'assurance est écrit au tableau "
            "ci-dessous. Ils sont couverts aux conditions énoncées dans le contrat d'assurance.\n"
            "PRIME\n"
            "\t Chapitre A - RESPONSABILITÉ CIVILE -\n"
            "Dommages matériels ou dommages corporels causés à d'autres personnes - Montant : 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Chapitre B - DOMMAGES AUX VÉHICULES ASSURÉS\n"
            "Protection 1 : Tous risques Incluse\n"
            "Protection 2 : Risques de collision et de renversement - Franchise 250$ par sinistre 2$\n"
            "Protection 3 : Tous les risques sauf collision ou renversement - Franchise 250$ par sinistre 3$\n"
            "Protection 4 : Risques spécifiques Non couvert\n"
            f"{a_new_page}\n"
            "Avenant(s) : F.A.Q. N 20 - Frais de déplacement (formule étendue) (Chapitre B) 4$\n"
            "Frais de déplacement 50$ par jour, limitation totale de 1500$ par sinistre\n"
            "Autres frais couverts au cours d'un voyage - 750$\n"
            f"\t Programme {fidelity_program_name}\n"
            f"F.A.Q. N 41\n"
            f"- Modification aux franchises (Chapitre B) : Incluse\n"
            f"Cet avenant apporte les modifications suivantes aux franchises du chapitre B :\n"
            f"\t - Suppression de la franchise, pour un délit de fuite s'il y a eu un rapport de police.\n"
            f"\t - Suppression de la franchise, pour une perte totale.\n"
            f"\t - Suppression de la franchise, pour une réparation de pare-brise sauf lors de son remplacement.\n"
            f"\t - Si vous êtes victime d'un sinistre qui affecte deux produits ou plus, assurés à "
            f"{a_insurer_name}, vous n'aurez qu'une seule franchise à payer, soit la plus élevée.\n"
            "Date d'échéance de prime : selon le mode de paiement convenu\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractWithEndorsementFAQ34_whenGenerateItem4Text_thenReturnProperFRText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ34CoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ34Coverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDÉLITÉ"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Article 4. GARANTIES / RISQUES : Les risques couverts par le contrat d'assurance sont ceux "
            "pour lesquels un montant d'assurance, une franchise ou une prime d'assurance est écrit au tableau "
            "ci-dessous. Ils sont couverts aux conditions énoncées dans le contrat d'assurance.\n"
            "PRIME\n"
            "\t Chapitre A - RESPONSABILITÉ CIVILE -\n"
            "Dommages matériels ou dommages corporels causés à d'autres personnes - Montant : 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Chapitre B - DOMMAGES AUX VÉHICULES ASSURÉS\n"
            "Protection 1 : Tous risques Incluse\n"
            "Protection 2 : Risques de collision et de renversement - Franchise 250$ par sinistre 2$\n"
            "Protection 3 : Tous les risques sauf collision ou renversement - Franchise 250$ par sinistre 3$\n"
            "Protection 4 : Risques spécifiques Non couvert\n"
            f"{a_new_page}\n"
            "Avenant(s) : F.A.Q. N 34 - Assurance de personnes : 4$\n"
            "Division 1 : Subdivision A et B - Indemnités en cas de décès - mutilation : 20000$ capital assuré\n"
            "Subdivision C - Remboursement de frais médicaux : 2000$ par personne\n"
            "Division 2 : Incapacité totale : non couvert\n"
            f"\t Programme {fidelity_program_name}\n"
            f"F.A.Q. N 41\n"
            f"- Modification aux franchises (Chapitre B) : Incluse\n"
            f"Cet avenant apporte les modifications suivantes aux franchises du chapitre B :\n"
            f"\t - Suppression de la franchise, pour un délit de fuite s'il y a eu un rapport de police.\n"
            f"\t - Suppression de la franchise, pour une perte totale.\n"
            f"\t - Suppression de la franchise, pour une réparation de pare-brise sauf lors de son remplacement.\n"
            f"\t - Si vous êtes victime d'un sinistre qui affecte deux produits ou plus, assurés à "
            f"{a_insurer_name}, vous n'aurez qu'une seule franchise à payer, soit la plus élevée.\n"
            "Date d'échéance de prime : selon le mode de paiement convenu\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractWithEndorsementFAQ34AB_whenGenerateItem4Text_thenReturnProperFRText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ34ABCoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ34ABCoverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDÉLITÉ"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Article 4. GARANTIES / RISQUES : Les risques couverts par le contrat d'assurance sont ceux "
            "pour lesquels un montant d'assurance, une franchise ou une prime d'assurance est écrit au tableau "
            "ci-dessous. Ils sont couverts aux conditions énoncées dans le contrat d'assurance.\n"
            "PRIME\n"
            "\t Chapitre A - RESPONSABILITÉ CIVILE -\n"
            "Dommages matériels ou dommages corporels causés à d'autres personnes - Montant : 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Chapitre B - DOMMAGES AUX VÉHICULES ASSURÉS\n"
            "Protection 1 : Tous risques Incluse\n"
            "Protection 2 : Risques de collision et de renversement - Franchise 250$ par sinistre 2$\n"
            "Protection 3 : Tous les risques sauf collision ou renversement - Franchise 250$ par sinistre 3$\n"
            "Protection 4 : Risques spécifiques Non couvert\n"
            f"{a_new_page}\n"
            "Avenant(s) : F.A.Q. N 34ab - Assurance de personnes : 4$\n"
            "Division 1 : Subdivision A et B - Indemnités en cas de décès - mutilation : 20000$ capital assuré\n"
            "Subdivision C - Remboursement de frais médicaux : 2000$ par personne\n"
            "Division 2 : Incapacité totale : non couvert\n"
            f"\t Programme {fidelity_program_name}\n"
            f"F.A.Q. N 41\n"
            f"- Modification aux franchises (Chapitre B) : Incluse\n"
            f"Cet avenant apporte les modifications suivantes aux franchises du chapitre B :\n"
            f"\t - Suppression de la franchise, pour un délit de fuite s'il y a eu un rapport de police.\n"
            f"\t - Suppression de la franchise, pour une perte totale.\n"
            f"\t - Suppression de la franchise, pour une réparation de pare-brise sauf lors de son remplacement.\n"
            f"\t - Si vous êtes victime d'un sinistre qui affecte deux produits ou plus, assurés à "
            f"{a_insurer_name}, vous n'aurez qu'une seule franchise à payer, soit la plus élevée.\n"
            "Date d'échéance de prime : selon le mode de paiement convenu\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractWithEndorsementFAQ43_whenGenerateItem4Text_thenReturnProperFRText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ43CoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ43Coverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDÉLITÉ"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Article 4. GARANTIES / RISQUES : Les risques couverts par le contrat d'assurance sont ceux "
            "pour lesquels un montant d'assurance, une franchise ou une prime d'assurance est écrit au tableau "
            "ci-dessous. Ils sont couverts aux conditions énoncées dans le contrat d'assurance.\n"
            "PRIME\n"
            "\t Chapitre A - RESPONSABILITÉ CIVILE -\n"
            "Dommages matériels ou dommages corporels causés à d'autres personnes - Montant : 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Chapitre B - DOMMAGES AUX VÉHICULES ASSURÉS\n"
            "Protection 1 : Tous risques Incluse\n"
            "Protection 2 : Risques de collision et de renversement - Franchise 250$ par sinistre 2$\n"
            "Protection 3 : Tous les risques sauf collision ou renversement - Franchise 250$ par sinistre 3$\n"
            "Protection 4 : Risques spécifiques Non couvert\n"
            f"{a_new_page}\n"
            "Avenant(s) : F.A.Q. N 43a - Modification à l'indemnisation (Chapitre B) - Perte partielle - Pièces neuves"
            " 1$\n"
            "F.A.Q. N 43e - Modification à l'indemnisation (Chapitre B) - Perte totale - Indemnisation selon la "
            "valeur de remplacement du véhicule 3$\n"
            f"\t Programme {fidelity_program_name}\n"
            f"F.A.Q. N 41\n"
            f"- Modification aux franchises (Chapitre B) : Incluse\n"
            f"Cet avenant apporte les modifications suivantes aux franchises du chapitre B :\n"
            f"\t - Suppression de la franchise, pour un délit de fuite s'il y a eu un rapport de police.\n"
            f"\t - Suppression de la franchise, pour une perte totale.\n"
            f"\t - Suppression de la franchise, pour une réparation de pare-brise sauf lors de son remplacement.\n"
            f"\t - Si vous êtes victime d'un sinistre qui affecte deux produits ou plus, assurés à "
            f"{a_insurer_name}, vous n'aurez qu'une seule franchise à payer, soit la plus élevée.\n"
            "Date d'échéance de prime : selon le mode de paiement convenu\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractWithEndorsementFAQ2_whenGenerateItem4Text_thenReturnProperFRText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ2CoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ2Coverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDÉLITÉ"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Article 4. GARANTIES / RISQUES : Les risques couverts par le contrat d'assurance sont ceux "
            "pour lesquels un montant d'assurance, une franchise ou une prime d'assurance est écrit au tableau "
            "ci-dessous. Ils sont couverts aux conditions énoncées dans le contrat d'assurance.\n"
            "PRIME\n"
            "\t Chapitre A - RESPONSABILITÉ CIVILE -\n"
            "Dommages matériels ou dommages corporels causés à d'autres personnes - Montant : 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Chapitre B - DOMMAGES AUX VÉHICULES ASSURÉS\n"
            "Protection 1 : Tous risques Incluse\n"
            "Protection 2 : Risques de collision et de renversement - Franchise 250$ par sinistre 2$\n"
            "Protection 3 : Tous les risques sauf collision ou renversement - Franchise 250$ par sinistre 3$\n"
            "Protection 4 : Risques spécifiques Non couvert\n"
            f"{a_new_page}\n"
            "Avenant(s) : F.A.Q. N 2 - Conduite de véhicules dont l'assuré désigné n'est pas propriétaire par "
            "des conducteurs désignés (Chapitre A) Incluse\n"
            f"\t Programme {fidelity_program_name}\n"
            f"F.A.Q. N 41\n"
            f"- Modification aux franchises (Chapitre B) : Incluse\n"
            f"Cet avenant apporte les modifications suivantes aux franchises du chapitre B :\n"
            f"\t - Suppression de la franchise, pour un délit de fuite s'il y a eu un rapport de police.\n"
            f"\t - Suppression de la franchise, pour une perte totale.\n"
            f"\t - Suppression de la franchise, pour une réparation de pare-brise sauf lors de son remplacement.\n"
            f"\t - Si vous êtes victime d'un sinistre qui affecte deux produits ou plus, assurés à "
            f"{a_insurer_name}, vous n'aurez qu'une seule franchise à payer, soit la plus élevée.\n"
            "Date d'échéance de prime : selon le mode de paiement convenu\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractWithEndorsementFAQ5A_whenGenerateItem4Text_thenReturnProperFRText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ5ACoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ5ACoverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDÉLITÉ"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Article 4. GARANTIES / RISQUES : Les risques couverts par le contrat d'assurance sont ceux "
            "pour lesquels un montant d'assurance, une franchise ou une prime d'assurance est écrit au tableau "
            "ci-dessous. Ils sont couverts aux conditions énoncées dans le contrat d'assurance.\n"
            "PRIME\n"
            "\t Chapitre A - RESPONSABILITÉ CIVILE -\n"
            "Dommages matériels ou dommages corporels causés à d'autres personnes - Montant : 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Chapitre B - DOMMAGES AUX VÉHICULES ASSURÉS\n"
            "Protection 1 : Tous risques Incluse\n"
            "Protection 2 : Risques de collision et de renversement - Franchise 250$ par sinistre 2$\n"
            "Protection 3 : Tous les risques sauf collision ou renversement - Franchise 250$ par sinistre 3$\n"
            "Protection 4 : Risques spécifiques Non couvert\n"
            f"{a_new_page}\n"
            "Avenant(s) : F.A.Q. N 5a - Véhicules loués ou sous contrat de location Incluse\n"
            f"\t Programme {fidelity_program_name}\n"
            f"F.A.Q. N 41\n"
            f"- Modification aux franchises (Chapitre B) : Incluse\n"
            f"Cet avenant apporte les modifications suivantes aux franchises du chapitre B :\n"
            f"\t - Suppression de la franchise, pour un délit de fuite s'il y a eu un rapport de police.\n"
            f"\t - Suppression de la franchise, pour une perte totale.\n"
            f"\t - Suppression de la franchise, pour une réparation de pare-brise sauf lors de son remplacement.\n"
            f"\t - Si vous êtes victime d'un sinistre qui affecte deux produits ou plus, assurés à "
            f"{a_insurer_name}, vous n'aurez qu'une seule franchise à payer, soit la plus élevée.\n"
            "Date d'échéance de prime : selon le mode de paiement convenu\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractWithEndorsementFAQ23A_whenGenerateItem4Text_thenReturnProperFRText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ23ACoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ23ACoverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDÉLITÉ"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Article 4. GARANTIES / RISQUES : Les risques couverts par le contrat d'assurance sont ceux "
            "pour lesquels un montant d'assurance, une franchise ou une prime d'assurance est écrit au tableau "
            "ci-dessous. Ils sont couverts aux conditions énoncées dans le contrat d'assurance.\n"
            "PRIME\n"
            "\t Chapitre A - RESPONSABILITÉ CIVILE -\n"
            "Dommages matériels ou dommages corporels causés à d'autres personnes - Montant : 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Chapitre B - DOMMAGES AUX VÉHICULES ASSURÉS\n"
            "Protection 1 : Tous risques Incluse\n"
            "Protection 2 : Risques de collision et de renversement - Franchise 250$ par sinistre 2$\n"
            "Protection 3 : Tous les risques sauf collision ou renversement - Franchise 250$ par sinistre 3$\n"
            "Protection 4 : Risques spécifiques Non couvert\n"
            f"{a_new_page}\n"
            "Avenant(s) : F.A.Q. N 23a - Véhicules sous financement Incluse\n"
            f"\t Programme {fidelity_program_name}\n"
            f"F.A.Q. N 41\n"
            f"- Modification aux franchises (Chapitre B) : Incluse\n"
            f"Cet avenant apporte les modifications suivantes aux franchises du chapitre B :\n"
            f"\t - Suppression de la franchise, pour un délit de fuite s'il y a eu un rapport de police.\n"
            f"\t - Suppression de la franchise, pour une perte totale.\n"
            f"\t - Suppression de la franchise, pour une réparation de pare-brise sauf lors de son remplacement.\n"
            f"\t - Si vous êtes victime d'un sinistre qui affecte deux produits ou plus, assurés à "
            f"{a_insurer_name}, vous n'aurez qu'une seule franchise à payer, soit la plus élevée.\n"
            "Date d'échéance de prime : selon le mode de paiement convenu\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractWithEndorsementFAQ27_whenGenerateItem4Text_thenReturnProperFRText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ27CoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ27Coverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDÉLITÉ"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Article 4. GARANTIES / RISQUES : Les risques couverts par le contrat d'assurance sont ceux "
            "pour lesquels un montant d'assurance, une franchise ou une prime d'assurance est écrit au tableau "
            "ci-dessous. Ils sont couverts aux conditions énoncées dans le contrat d'assurance.\n"
            "PRIME\n"
            "\t Chapitre A - RESPONSABILITÉ CIVILE -\n"
            "Dommages matériels ou dommages corporels causés à d'autres personnes - Montant : 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Chapitre B - DOMMAGES AUX VÉHICULES ASSURÉS\n"
            "Protection 1 : Tous risques Incluse\n"
            "Protection 2 : Risques de collision et de renversement - Franchise 250$ par sinistre 2$\n"
            "Protection 3 : Tous les risques sauf collision ou renversement - Franchise 250$ par sinistre 3$\n"
            "Protection 4 : Risques spécifiques Non couvert\n"
            f"{a_new_page}\n"
            "Avenant(s) : F.A.Q. N 27 - Responsabilité civile du fait de dommages causés à des véhicules "
            "dont l'assuré désigné n'est pas propriétaire (incluant les véhicules fournis par un employeur) "
            "(Chapitre A) - 75000$\n"
            "Véhicules assimilables au véhicule désigné, aux caravanes ou remorques utilitaires Chapitre "
            "B2 - Franchise 250$ et chapitre B3 - Franchise 50$ Incluse\n"
            f"\t Programme {fidelity_program_name}\n"
            f"F.A.Q. N 41\n"
            f"- Modification aux franchises (Chapitre B) : Incluse\n"
            f"Cet avenant apporte les modifications suivantes aux franchises du chapitre B :\n"
            f"\t - Suppression de la franchise, pour un délit de fuite s'il y a eu un rapport de police.\n"
            f"\t - Suppression de la franchise, pour une perte totale.\n"
            f"\t - Suppression de la franchise, pour une réparation de pare-brise sauf lors de son remplacement.\n"
            f"\t - Si vous êtes victime d'un sinistre qui affecte deux produits ou plus, assurés à "
            f"{a_insurer_name}, vous n'aurez qu'une seule franchise à payer, soit la plus élevée.\n"
            "Date d'échéance de prime : selon le mode de paiement convenu\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractWithEndorsementFAQ27a_whenGenerateItem4Text_thenReturnProperFRText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ27ACoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ27ACoverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDÉLITÉ"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Article 4. GARANTIES / RISQUES : Les risques couverts par le contrat d'assurance sont ceux "
            "pour lesquels un montant d'assurance, une franchise ou une prime d'assurance est écrit au tableau "
            "ci-dessous. Ils sont couverts aux conditions énoncées dans le contrat d'assurance.\n"
            "PRIME\n"
            "\t Chapitre A - RESPONSABILITÉ CIVILE -\n"
            "Dommages matériels ou dommages corporels causés à d'autres personnes - Montant : 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Chapitre B - DOMMAGES AUX VÉHICULES ASSURÉS\n"
            "Protection 1 : Tous risques Incluse\n"
            "Protection 2 : Risques de collision et de renversement - Franchise 250$ par sinistre 2$\n"
            "Protection 3 : Tous les risques sauf collision ou renversement - Franchise 250$ par sinistre 3$\n"
            "Protection 4 : Risques spécifiques Non couvert\n"
            f"{a_new_page}\n"
            "Avenant(s) : F.A.Q. N 27a - Responsabilité civile du fait de dommages causés à des véhicules "
            "dont l'assuré désigné n'est pas propriétaire (incluant les véhicules fournis par un employeur) "
            "(Chapitre A) - 75000$\n"
            "Véhicules assimilables au véhicule désigné, aux caravanes ou remorques utilitaires Chapitre "
            "B2 - Franchise 250$ et chapitre B3 - Franchise 50$ Incluse\n"
            f"\t Programme {fidelity_program_name}\n"
            f"F.A.Q. N 41\n"
            f"- Modification aux franchises (Chapitre B) : Incluse\n"
            f"Cet avenant apporte les modifications suivantes aux franchises du chapitre B :\n"
            f"\t - Suppression de la franchise, pour un délit de fuite s'il y a eu un rapport de police.\n"
            f"\t - Suppression de la franchise, pour une perte totale.\n"
            f"\t - Suppression de la franchise, pour une réparation de pare-brise sauf lors de son remplacement.\n"
            f"\t - Si vous êtes victime d'un sinistre qui affecte deux produits ou plus, assurés à "
            f"{a_insurer_name}, vous n'aurez qu'une seule franchise à payer, soit la plus élevée.\n"
            "Date d'échéance de prime : selon le mode de paiement convenu\n"
        )

        self.assertEqual(expected, actual)
