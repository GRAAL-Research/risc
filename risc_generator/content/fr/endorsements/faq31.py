from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq31_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Formulaire d'avenant du Québec\n"
        "F.A.Q. N 31\n"
        "Équipement n'appartenant pas à l'assuré désigné\n"
        "Le titre de l'avenant doit être écrit à la section « Conditions particulières » du contrat "
        "d'assurance. Quant aux informations requises dans l'avenant, elles peuvent être écrites à "
        "cette section ou dans l'avenant même, au choix de l'assureur.\n"
        "Nom de l'assureur : \n"
        "Nom de l'assuré désigné : \n"
        "Avenant à la police d'assurance automobile N : \n"
        "Date de prise d'effet : cet avenant s'applique à partir du à 0 h 01, heure normale "
        "à l'adresse de l'assuré désigné.\n"
        "Véhicule visé : cet avenant s'applique uniquement au véhicule désigné suivant :\n"
        "(numéro de référence écrit à la section « Conditions particulières » du contrat d'assurance)\n"
        "Description de l'avenant\n"
        "Cet avenant étend les garanties du contrat d'assurance à l'équipement suivant, dont "
        "l'assuré désigné n'est pas propriétaire :\n"
        "Conditions d'application\n"
        "L'équipement doit être normalement fixé au véhicule visé. De plus, l'assuré désigné doit "
        "avoir un pouvoir de direction ou de gestion sur cet équipement, ou en avoir la garde.\n"
        "1. Application au chapitre A\n"
        "La garantie du chapitre A est étendue aux conséquences financières que peut "
        "subir la personne assurée lorsqu'elle est civilement responsable d'un dommage causé à une "
        "autre personne du fait de l'équipement décrit ci-dessus.\n"
        "2. Application au chapitre B\n"
        "La garantie du chapitre B applicable au véhicule visé est étendue :\n"
        "\t aux dommages directs et accidentels causés à l'équipement décrit ci-dessus;\n"
        "\t à la disparition de cet équipement.\n"
        "Pour le chapitre B, l'indemnité est payable jusqu'à concurrence de la « valeur au jour du "
        "sinistre » de l'équipement et pour un montant maximum de $. Elle est payable "
        "conjointement à l'assuré désigné et à  selon leurs intérêts respectifs.\n"
        "Toutes les autres conditions du contrat d'assurance restent les mêmes.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
