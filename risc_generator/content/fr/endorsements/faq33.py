from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq33_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Formulaire d'avenant du Québec\n"
        "F.A.Q. N 33\n"
        "Assurance pour les frais d'assistance routière\n"
        "Le titre de l'avenant doit être écrit à la section « Conditions particulières » du contrat "
        "d'assurance. Quant aux informations requises dans l'avenant, elles peuvent être écrites à "
        "cette section ou dans l'avenant même, au choix de l'assureur.\n"
        "Nom de l'assureur : \n"
        "Nom de l'assuré désigné : \n"
        "Avenant à la police d'assurance automobile N :\n"
        "Date de prise d'effet : cet avenant s'applique à partir du à 0 h 01, heure normale "
        "à l'adresse de l'assuré désigné.\n"
        "Prime d'assurance additionnelle à payer :\n"
        "\t Montants à payer :  \n"
        "\t Date limite pour payer :  \n"
        "Véhicule visé : cet avenant s'applique uniquement au véhicule désigné suivant :\n"
        "(numéro de référence écrit à la section « Conditions particulières » du contrat d'assurance)\n"
        "Description de l'avenant\n"
        "Cet avenant prévoit que les frais d'assistance routière décrits ci-dessous et engagés pour le "
        "véhicule visé seront remboursés par l'assureur.\n"
        "Frais d'assistance routière\n"
        "Les frais d'assistance routière couverts sont les suivants :\n"
        "\t le changement d'une roue;\n"
        "\t le déverrouillage des portières;\n"
        "\t la livraison d'essence, jusqu'à 10 litres;\n"
        "\t le remorquage dans un rayon de  kilomètres (minimum de 25 km);\n"
        "\t le survoltage de la batterie.\n"
        "Les réparations mécaniques, ainsi que les pièces et les fournitures utilisées pour réparer "
        "le véhicule visé, ne sont pas couvertes par cet avenant.\n"
        "Limitations\n"
        "\t  $ par événement occasionnant des frais d'assistance routière.\n"
        "\t  $ par année d'assurance.\n"
        "\t  événements par année d'assurance.\n"
        "Demande de remboursement\n"
        "L'assuré désigné doit justifier sa demande de remboursement en remettant à l'assureur "
        "les factures payées relatives aux frais d'assistance routière.\n"
        "Toutes les autres conditions du contrat d'assurance restent les mêmes.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
