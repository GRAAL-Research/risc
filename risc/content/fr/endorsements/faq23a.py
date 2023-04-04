from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq23a_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Formulaire d'avenant du Québec\n"
        "F.A.Q. N 23a\n"
        "Préavis au créancier\n"
        "(Chapitre B)\n"
        "Le titre de l'avenant doit être écrit à la section « Conditions particulières » du contrat d'assurance.\n"
        "Nom de l'assureur : \n"
        "Nom de l'assuré désigné : \n"
        "Nom du créancier :  \n"
        "Adresse du créancier :  \n"
        "Avenant à la police d'assurance automobile N : \n"
        "Date de prise d'effet : cet avenant s'applique à partir du à 0 h 01, heure normale "
        "à l'adresse de l'assuré désigné.\n"
        "Véhicule visé : cet avenant s'applique uniquement au véhicule désigné suivant :\n"
        "(numéro de référence écrit à la section « Conditions particulières » du contrat d'assurance)\n"
        "Description de l'avenant\n"
        "Cet avenant modifie le chapitre B du contrat d'assurance en y ajoutant l'obligation suivante :\n"
        "\t L'assureur doit donner au créancier un préavis d'au moins 15 jours avant de résilier ou de "
        "modifier une garantie du chapitre B.\n"
        "\t Il doit le faire seulement si le fait de résilier ou de modifier la garantie désavantage le "
        "créancier.\n"
        "Toutes les autres conditions du contrat d'assurance restent les mêmes.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
