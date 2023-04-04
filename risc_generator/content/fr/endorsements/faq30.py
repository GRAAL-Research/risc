from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq30_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Formulaire d'avenant du Québec\n"
        "F.A.Q. N 30\n"
        "Restriction des garanties pour certains équipements et matériel fixés au véhicule\n"
        "(Chapitre A)\n"
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
        "Sous réserve de la Loi sur l'assurance automobile, cet avenant restreint les garanties du chapitre A du "
        "contrat d'assurance en y ajoutant l'exclusion suivante :\n"
        "\t Sont exclues les conséquences financières que peut subir la personne assurée lorsqu'elle "
        "est civilement responsable de dommages occasionnés par l'équipement ou le matériel suivant - ou "
        "leurs accessoires - pendant qu'ils sont fixés au véhicule visé :\n"
        "(Caractéristiques de l'équipement ou du matériel)\n"
        "Pour que l'exclusion ci-dessus s'applique :\n"
        "\t les dommages doivent être occasionnés pendant que l'équipement, le matériel ou leurs "
        "accessoires se trouvent sur les lieux de leur utilisation; et\n"
        "\t la responsabilité civile de la personne assurée doit découler du fait qu'elle est "
        "propriétaire de l'équipement, du matériel ou de leurs accessoires, ou du fait de leur usage ou de "
        "leur fonctionnement.\n"
        "Toutes les autres conditions du contrat d'assurance restent les mêmes.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
