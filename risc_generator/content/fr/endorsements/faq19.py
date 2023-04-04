from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq19_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Formulaire d'avenant du Québec\n"
        "F.A.Q. N 19\n"
        "Limitation de l'indemnité\n"
        "(Chapitre B)\n"
        "Le titre de l'avenant doit être écrit à la section « Conditions particulières » du contrat "
        "d'assurance. Quant aux informations requises dans l'avenant, elles peuvent être écrites à "
        "cette section ou dans l'avenant même, au choix de l'assureur.\n"
        "Nom de l'assureur : \n"
        "Nom de l'assuré désigné : \n"
        "Avenant à la police d'assurance automobile N :\n"
        "Date de prise d'effet : cet avenant s'applique à partir du à 0 h 01, heure normale "
        "à l'adresse de l'assuré désigné.\n"
        "Véhicule visé : cet avenant s'applique uniquement au véhicule désigné suivant :\n"
        "(numéro de référence écrit à la section « Conditions particulières » du contrat d'assurance)\n"
        "Description de l'avenant\n"
        "Cet avenant limite l'indemnité payable du chapitre B du contrat d'assurance au moins élevé des "
        "montants suivants :\n"
        "\t la « valeur au jour du sinistre » du véhicule visé.\n"
        "\t $.\n"
        "Toutes les autres conditions du contrat d'assurance restent les mêmes.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
