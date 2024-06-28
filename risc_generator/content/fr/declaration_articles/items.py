import re
from typing import Union

from ..general_header import generate_general_pages_header_text
from ...config import (
    FAKE_INSURER_ADDRESS,
    FAKE_INSURER_NAME,
    FAKE_INSURER_WEBSITE,
    NEW_PAGE_TAG,
    FAKE_ROADSIDE_PROGRAM_NAME,
    FAKE_FIDELITY_PROGRAM_NAME_FR,
)
from ....domain.premium import Premium
from ....domain.protections import Protections
from ....domain.tools import change_to_snake_case

all_property_damage_protection = [
    "PropertyDamageB1Coverage",
    "PropertyDamageB2Coverage",
    "PropertyDamageB3Coverage",
    "PropertyDamageB4Coverage",
]
endorsement_with_possible_premium = ["FAQ20", "FAQ20A", "FAQ33", "FAQ34", "FAQ34AB", "FAQ43"]
endorsement_without_premium = ["FAQ2", "FAQ5A", "FAQ23A", "FAQ27", "FAQ27A"]

# Base property damage text that we use to dynamically append the rest of the text base on the protections.
property_damage_b1_coverage_base_text = "Protection 1 : Tous risques"
property_damage_b2_coverage_base_text = "Protection 2 : Risques de collision et de renversement"
property_damage_b3_coverage_base_text = "Protection 3 : Tous les risques sauf collision ou renversement"
property_damage_b4_coverage_base_text = "Protection 4 : Risques spécifiques"

# Template for when the protection specified a deductible and a premium amount
property_damage_b1_coverage_deductible_template = "- Franchise {}$ par sinistre {}$"
property_damage_b2_coverage_deductible_template = "- Franchise {}$ par sinistre {}$"
property_damage_b3_coverage_deductible_template = "- Franchise {}$ par sinistre {}$"
property_damage_b4_coverage_deductible_template = "- Franchise {}$ par sinistre {}$"


def generate_declaration_header_text(policy_number: str) -> str:
    """
    Function to generate the declaration header text.

    policy_number (str): The policy number.

    Return:
        The declaration header text.
    """
    general_header_text = generate_general_pages_header_text(policy_number=policy_number)
    header = f"{general_header_text}" "CONDITIONS PARTICULIÈRES\n" "ÉMISSION de votre nouvelle police d'assurance\n"
    return header


def generate_item_1_text(insuree_name: str, insuree_address: str) -> str:
    """
    Function to generate the item 1 text for the declaration.

    insuree_name (str): The name of the insuree.
    insuree_address (str): The address of the insuree.

    Return:
        The item 1 text.
    """
    text = (
        "Article 1. NOM ET ADRESSE DE L'ASSURÉ DÉSIGNÉ*\n"
        f"{insuree_name}\n"
        f"{insuree_address}\n"
        "*La ville et la province de l'adresse écrite à cet article 1 constituent les lieux d'usage principal, de "
        "remisage et de stationnement du véhicule désigné. Si ce n'est pas le cas, le preneur ou l'assuré désigné doit "
        "le déclarer.\n"
    )
    return text


def generate_item_2_text(contract_start_date: str, contract_end_date: str) -> str:
    """
    Function to generate the item 2 text for the declaration.

    contract_start_date (str): The start date of the contract.
    contract_end_date (str): The end date of the contract.

    Return:
        The item 2 text.
    """
    text = (
        "Article 2. DURÉE DU CONTRAT\n"
        f"DU : {contract_start_date}* AU : {contract_end_date}* EXCLUSIVEMENT\n"
        "*à 0 h 01 selon l'heure normale à l'adresse de l'assuré désigné.\n"
    )
    return text


def generate_item_3_text(
    formatted_vehicle_complete_details: str,
    car_ownership: str,
    vehicle_purchase_condition: str,
    car_with_financing: Union[None, str],
    financing_details: str,
) -> str:
    """
    Function to generate the item 3 text for the declaration.

    formatted_vehicle_complete_details (str): The vehicle complete details in the proper format.
    car_ownership (str): The type of car ownership in the locale language (e.g. Achat/location).
    vehicle_purchase_condition (str): The condition of the vehicle at purchase in the locale language (e.g. Neuf)
    car_with_financing (Union[None, str]) The type of financing, if any. If None, it means no financing.
    financing_details (str): Financing details, if any.

    Return:
        The item 3 text.
    """

    text = (
        "Article 3. CARACTÉRISTIQUES DU VÉHICULE DÉSIGNÉ 1\n"
        f"{formatted_vehicle_complete_details} - {car_ownership} {vehicle_purchase_condition}\n"
    )

    if car_with_financing == "creditor":
        text += (
            "Créancier qui a droit aux indemnités du chapitre B, selon son intérêt - Sujet à l'avenant F.A.Q. N 23a\n"
            f"{financing_details}\n"
        )
    elif car_with_financing == "lessor":
        text += (
            "Locateur qui a droit aux indemnités du chapitre B, selon son intérêt - Sujet à l'avenant F.A.Q. N 5a\n"
            f"{financing_details}\n"
        )

    return text


# Endorsements with premium <


def generate_faq_20_text(faq_premium: str) -> str:
    """
    Function to generate FAQ20 text with a premium amount
    """
    text = (
        f"F.A.Q. N 20 - Frais de déplacement (formule étendue) (Chapitre B) {faq_premium}$\n"
        "Frais de déplacement 50$ par jour, limitation totale de 1500$ par sinistre\n"
        "Autres frais couverts au cours d'un voyage - 750$\n"
    )
    return text


def generate_faq_20a_text(faq_premium: str) -> str:
    """
    Function to generate FAQ20A text with a premium amount
    """
    text = (
        f"F.A.Q. N 20a - Frais de déplacement (formule étendue) (Chapitre B) {faq_premium}$\n"
        "Frais de déplacement 50$ par jour, limitation totale de 1500$ par sinistre\n"
        "Autres frais couverts au cours d'un voyage - 750$\n"
    )
    return text


def generate_faq_33_text(faq_premium: str) -> str:
    """
    Function to generate FAQ33 text with a premium amount
    """
    text = (
        "F.A.Q. N 33 - Assurance pour les frais d'assistance routière\n"
        f"{FAKE_ROADSIDE_PROGRAM_NAME} Programme d'assistance routière, disponible 24 heures sur 24, 7 jours sur 7\n"
        "Rayon maximum 50 km -\n"
        "En cas de panne, la distance de remorquage est haussée à 100 km dans le parc des Laurentides, "
        "150 km dans le parc de la Vérendrye et 100 km dans le parc national de la Gaspésie\n"
        f"Nombre d'événements maximum par année d'assurance 4 {faq_premium}$\n"
        "Limite par dépannage 60$(1) - Pour un remorquage ou un véhicule enlisé, cette limite est haussée à 100$(1)\n"
        "Limite par année d'assurance 400$(1)\n"
        "(1) Ces limites s'appliquent uniquement lorsque, de façon exceptionnelle, le service de dépannage ou de "
        "remorquage n'est pas disponible par le programme d'assistance routière\n"
        "Consultez votre brochure pour connaître tous les services additionnels qui vous sont offerts\n"
    )
    return text


def generate_faq_34ab_text(faq_premium: str) -> str:
    """
    Function to generate FAQ34AB text with a premium amount
    """
    text = (
        f"F.A.Q. N 34ab - Assurance de personnes : {faq_premium}$\n"
        "Division 1 : Subdivision A et B - Indemnités en cas de décès - mutilation : 20000$ capital assuré\n"
        "Subdivision C - Remboursement de frais médicaux : 2000$ par personne\n"
        "Division 2 : Incapacité totale : non couvert\n"
    )
    return text


def generate_faq_34_text(faq_premium: str) -> str:
    """
    Function to generate FAQ34 text with a premium amount
    """
    text = (
        f"F.A.Q. N 34 - Assurance de personnes : {faq_premium}$\n"
        "Division 1 : Subdivision A et B - Indemnités en cas de décès - mutilation : 20000$ capital assuré\n"
        "Subdivision C - Remboursement de frais médicaux : 2000$ par personne\n"
        "Division 2 : Incapacité totale : non couvert\n"
    )
    return text


def generate_faq_43_text(faq_premium: str) -> str:
    """
    Function to generate FAQ43 text with a premium amount.

    25% of the premium is the FAQ43A and 75% of the premium is the FAQ43E.
    """

    text = (
        f"F.A.Q. N 43a - Modification à l'indemnisation (Chapitre B) - Perte partielle - Pièces neuves "
        f"{round(int(faq_premium) * 0.25)}$\n"
        "F.A.Q. N 43e - Modification à l'indemnisation (Chapitre B) - Perte totale - Indemnisation selon la "
        f"valeur de remplacement du véhicule {round(int(faq_premium) * 0.75)}$\n"
    )
    return text


# Endorsements with premium >


# Endorsements with no premium <
def generate_faq_2_text() -> str:
    """
    Function to generate FAQ2 text.
    """

    text = (
        "F.A.Q. N 2 - Conduite de véhicules dont l'assuré désigné n'est pas propriétaire par des conducteurs "
        "désignés (Chapitre A) Incluse\n"
    )
    return text


def generate_faq_5a_text() -> str:
    """
    Function to generate FAQ5a text.
    """

    text = "F.A.Q. N 5a - Véhicules loués ou sous contrat de location Incluse\n"
    return text


def generate_faq_23a_text() -> str:
    """
    Function to generate FAQ23a text.
    """

    text = "F.A.Q. N 23a - Véhicules sous financement Incluse\n"
    return text


def generate_faq_27_text() -> str:
    """
    Function to generate FAQ27 text.
    """

    text = (
        "F.A.Q. N 27 - Responsabilité civile du fait de dommages causés à des véhicules dont l'assuré désigné "
        "n'est pas propriétaire (incluant les véhicules fournis par un employeur) (Chapitre A) - 75000$\n"
        "Véhicules assimilables au véhicule désigné, aux caravanes ou remorques utilitaires Chapitre "
        "B2 - Franchise 250$ et chapitre B3 - Franchise 50$ Incluse\n"
    )
    return text


def generate_faq_27a_text() -> str:
    """
    Function to generate FAQ27a text.
    """

    text = (
        "F.A.Q. N 27a - Responsabilité civile du fait de dommages causés à des véhicules dont l'assuré désigné "
        "n'est pas propriétaire (incluant les véhicules fournis par un employeur) (Chapitre A) - 75000$\n"
        "Véhicules assimilables au véhicule désigné, aux caravanes ou remorques utilitaires Chapitre "
        "B2 - Franchise 250$ et chapitre B3 - Franchise 50$ Incluse\n"
    )
    return text


# Endorsements with no premium >


def generate_item_4_text(protections: Protections, premium: Premium) -> str:
    """
    Function to generate the item 4 text for the declaration.

    protections (Protections): The protections.
    premium (Premium): The premiums.

    Return:
        The item 4 text.
    """

    text = (
        "Article 4. GARANTIES / RISQUES : Les risques couverts par le contrat d'assurance sont ceux pour lesquels "
        "un montant d'assurance, une franchise ou une prime d'assurance est écrit au tableau ci-dessous. "
        "Ils sont couverts aux conditions énoncées dans le contrat d'assurance.\n"
        "PRIME\n"
        "\t Chapitre A - RESPONSABILITÉ CIVILE -\n"
        f"Dommages matériels ou dommages corporels causés à d'autres personnes - Montant : "
        f"{protections.get('LiabilityCoverage')}$ {premium.get_premium('liability_coverage_premium')}$\n"
        f"\t Chapitre B - DOMMAGES AUX VÉHICULES ASSURÉS\n"
    )

    # Chapter B text
    protection_with_deductible = protections.property_damage_protections()

    # We construct the text to use using template filling.
    for protection_name in all_property_damage_protection:

        # To extract the proper property damage text, we use the protection damage name written in CamelCase
        # and convert it into snake_case.
        snake_case_protection_name = change_to_snake_case(protection_name)
        base_text = eval(f"{snake_case_protection_name}_base_text")

        if protection_name in protection_with_deductible:
            # If the protection is one with a deductible, thus it need to be written in the protection text and include
            # a premium amount.
            protection_text = eval(f"{snake_case_protection_name}_deductible_template")
            protection_text = protection_text.format(
                protections.get(protection_name), premium.get_premium(f"{protection_name}Premium")
            )
        else:
            # The protection is either 'Include' or 'Exclude' (written in the locale language).
            if protections.is_protected(protection_name):
                # If the protection name is protected, it means it is 'include' (but written in the local language).
                protection_text = "Incluse"
            else:
                # If the protection name is not protected, it means it is 'exclude' (but written in the local language).
                protection_text = "Non couvert"

        text += base_text + " " + protection_text + "\n"

    # We arbitrarily split the item 4 after the chapter B
    text += NEW_PAGE_TAG + "\n"

    # Endorsement text
    endorsement_protections = protections.endorsement_protections()
    for endorsement in endorsement_protections:
        if endorsement.strip("Coverage") in endorsement_with_possible_premium and protections.is_protected(
            f"{endorsement}"
        ):
            text += "Avenant(s) : "
            faq_premium = premium.get_premium(f"{endorsement}Premium")
            endorsement_number = re.findall(r'[0-9]+[AB]*', endorsement)[0].lower()
            text += eval(f"generate_faq_{endorsement_number}_text(faq_premium={faq_premium})")

        elif endorsement.strip("Coverage") in endorsement_without_premium and protections.is_protected(
            f"{endorsement}"
        ):
            text += "Avenant(s) : "
            endorsement_number = re.findall(r'[0-9]+[AB]*', endorsement)[0].lower()
            text += eval(f"generate_faq_{endorsement_number}_text()")

    text += (
        f"\t Programme {FAKE_FIDELITY_PROGRAM_NAME_FR}\n"
        f"F.A.Q. N 41\n"
        f"- Modification aux franchises (Chapitre B) : Incluse\n"
        f"Cet avenant apporte les modifications suivantes aux franchises du chapitre B :\n"
        f"\t - Suppression de la franchise, pour un délit de fuite s'il y a eu un rapport de police.\n"
        f"\t - Suppression de la franchise, pour une perte totale.\n"
        f"\t - Suppression de la franchise, pour une réparation de pare-brise sauf lors de son remplacement.\n"
        f"\t - Si vous êtes victime d'un sinistre qui affecte deux produits ou plus, assurés à "
        f"{FAKE_INSURER_NAME}, vous n'aurez qu'une seule franchise à payer, soit la plus élevée.\n"
    )

    text += "Date d'échéance de prime : selon le mode de paiement convenu\n"

    return text


def generate_premium_ticket(contract_starting_date: str, premium: Premium) -> str:
    text = (
        f"Fait par l'Assureur à Québec {contract_starting_date.lower()}\n"
        f"Sherlock Holmes\n"
        f"Président et chef de la direction\n"
        f"Ceci n'est pas une facture, veuillez vous référer aux documents de la facturation pour "
        f"les montants à payer ou à recevoir\n"
        f"PRIME DU VÉHICULE 1\n"
        f"Catégorie d'assurance :\n"
        f"AUTOMOBILE\n"
        f"PRIME ANNUELLE\n"
        f"{premium.total}$ (excluant taxe)\n"
        f"VOTRE NOUVELLE POLICE 12 MOIS\n"
        f"MONTANT\n"
        f"{premium.total}$ (excluant taxe)\n"
        f"TAXE\n"
        f"{premium.total * 0.09}$\n"
    )  # The Quebec taxes is 9%
    return text


def generate_item_6_text(
    insuree_name: str, insuree_birth_date: str, has_suspension: bool, number_of_claims_past_years: int
) -> str:
    """
    Function to generate the item 6 text for the declaration.

    insuree_name (str): The name of the insuree.
    insuree_birth_date (str): The birthdate of the insuree.
    has_suspension (bool): Either or not the insuree has a suspension.
    number_of_claims_past_years (int): The number of claims the insuree has.

    Return:
        The item 6 text.
    """

    text = (
        "Article 6. DÉCLARATIONS IMPORTANTES POUR L'ANALYSE DU RISQUE\n"
        f"\t Conducteur principal : {insuree_name} Date de naissance : {insuree_birth_date}\n"
    )

    if has_suspension:
        text += (
            "\t Au moins une révocation ou suspension de permis a été déclarée au cours des trois dernières années\n"
        )
    else:
        text += "\t Aucune révocation ou suspension de permis n'ont été déclarées au cours des trois dernières années\n"

    if number_of_claims_past_years > 0:
        text += (
            f"\t {number_of_claims_past_years} sinistre(s) ou réclamation(s) ont été déclarés au cours des "
            f"cinq dernières années\n"
        )
    else:
        text += "\t Aucun sinistre, aucune réclamation n'a été déclaré au cours des cinq dernières années\n"

    return text


def generate_item_7_text(association_rebate: bool, payment_method: str) -> str:
    """
    Function to generate the item 7 text for the declaration.

    association_rebate (bool): Either or not the insuree has an association rebate.
    payment_method (str): The payment method.

    Return:
        The item 7 text.
    """

    text = "Article 7. INFORMATIONS POUR L'ASSURÉ DÉSIGNÉ\n"

    if association_rebate or payment_method == "pre-authorize":
        text += "\t La prime tient comptes des réductions suivantes :\n"
        if association_rebate:
            text += "- En tant que membre/client d'une association, vous avez droit au rabais suivant: 10%.\n"
        if payment_method == "pre-authorize":
            text += "- 2 % pour avoir choisi le Prélèvement préautorisé comme mode de paiement de votre prime\n"

    text += (
        "\t Consentement : Si une autorisation nous a été donnée afin d'obtenir des informations de crédit "
        "pour l'émission du présent contrat, veuillez noter que les renseignements obtenus seront mis à "
        "jour et utilisés pour votre renouvellement et pour le traitement de vos dossiers d'assurances "
        "générales. Ce consentement peut être révoqué en tout temps en nous avisant par écrit.\n"
    )

    return text


def generate_divulgation_text() -> str:
    """
    Function to generate the divulgation text for the declaration.

    Return:
        The divulgation text.
    """
    text = (
        "DIVULGATION\n\n"
        "AVIS CONCERNANT LA PROTECTION DES RENSEIGNEMENTS PERSONNELS\n"
        f"{FAKE_INSURER_NAME} traite de façon confidentielle les renseignements personnels qu'elle détient sur vous.\n"
        f"Objet de votre dossier\n"
        f"Nous recueillons et utilisons les renseignements personnels qui vous concernent dans le but de gérer "
        f"votre dossier d'assurance de dommages.\n"
        f"Sécurité\n"
        f"Vos renseignements personnels sont conservés à nos bureaux et protégés par des standards de sécurité "
        f"élevés. Seuls nos employés, mandataires, partenaires de distribution et fournisseurs de services peuvent "
        f"y avoir accès et ce, uniquement lorsque requis par leurs fonctions, mandats ou contrats.\n"
        f"{FAKE_INSURER_NAME} peut faire affaires avec un (ou des) fournisseur(s) de services basés à "
        f"l'extérieur du Québec. Ainsi, il est possible que certains de vos renseignements personnels détenus par "
        f"{FAKE_INSURER_NAME} puissent être hébergés à l'extérieur du Québec et être régis par les lois applicables à "
        f"des pays ou états étrangers.\n"
        f"Accès et rectification\n"
        f"Pour avoir accès à votre dossier ou en demander la rectification, faites-en la demande à "
        f"l'adresse suivante :\n"
        f"{FAKE_INSURER_NAME}\n"
        f"a/s du Service d'accès à l'information\n"
        f"{FAKE_INSURER_ADDRESS}\n"
        f"Offre de service\n"
        f"Il se peut que {FAKE_INSURER_NAME}, ses filiales et représentants autorisés utilisent vos renseignements "
        f"nominatifs pour vous informer des produits et services susceptibles de vous intéresser. "
        f"Si toutefois vous ne désirez pas recevoir ce type d'information, écrivez-nous à l'adresse ci-dessus.\n"
        f"Pour plus d'informations sur nos pratiques en matière de protection des renseignements personnels,"
        f" consultez notre Énoncé de confidentialité des renseignements personnels sur "
        f"{FAKE_INSURER_WEBSITE}/fr/protection-renseignements-personnels.\n"
        f"Votre agent offre exclusivement les produits de {FAKE_INSURER_NAME} et il ne reçoit aucune commission.\n"
    )
    return text
