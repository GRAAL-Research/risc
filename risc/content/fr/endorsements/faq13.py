from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq13_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Formulaire d'avenant du Québec\n"
        "F.A.Q. N 13c\n"
        "Restriction de la Protection 3 pour les vitres du véhicule\n"
        "(Chapitre B)\n"
        "Le titre de l'avenant doit être écrit à la section « Conditions particulières » du contrat d'assurance.\n"
        "Nom de l'assureur : \n"
        "Nom de l'assuré désigné : \n"
        "Avenant à la police d'assurance automobile N :\n"
        "Date de prise d'effet : cet avenant s'applique à partir du à 0 h 01, heure normale "
        "à l'adresse de l'assuré désigné.\n"
        "Véhicule visé : cet avenant s'applique uniquement au véhicule désigné suivant :\n"
        "(numéro de référence écrit à la section « Conditions particulières » du contrat d'assurance)\n"
        "Description de l'avenant\n"
        "Cet avenant restreint la Protection 3 du chapitre B du contrat d'assurance en excluant les "
        "dommages occasionnés aux vitres du véhicule visé, sauf s'ils sont occasionnés par :\n"
        "\t l'atterrissage forcé ou la chute d'un aéronef ou d'une partie de cet appareil;\n"
        "\t la crue des eaux;\n"
        "\t l'échouement, la submersion, l'incendie, le déraillement ou la collision de tout véhicule terrestre "
        "ou bateau servant à transporter le véhicule visé;\n"
        "\t les émeutes;\n"
        "\t les explosions;\n"
        "\t la foudre;\n"
        "\t la grêle;\n"
        "\t l'incendie;\n"
        "\t les mouvements populaires;\n"
        "\t les tempêtes de vent;\n"
        "\t les tentatives de vol;\n"
        "\t les tremblements de terre;\n"
        "\t le vol.\n"
        "Toutes les autres conditions du contrat d'assurance restent les mêmes.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
