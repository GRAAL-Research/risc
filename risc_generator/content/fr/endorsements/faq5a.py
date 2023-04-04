from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq5a_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Formulaire d'avenant du Québec\n"
        "F.A.Q. N 5a\n"
        "Véhicules loués ou pris en crédit-bail\n"
        "Modifications\n"
        "lorsque le propriétaire et un locataire ou crédit-preneur\n"
        "sont désignés comme assurés\n"
        "Le titre de l'avenant doit être écrit à la section « Conditions particulières » du contrat d'assurance.\n"
        "Nom de l'assureur : \n"
        "Nom de l'assuré désigné : \n"
        "Avenant à la police d'assurance automobile N :\n"
        "Date de prise d'effet : cet avenant s'applique à partir du à 0 h 01, heure normale "
        "à l'adresse de l'assuré désigné.\n"
        "Véhicule visé : cet avenant s'applique uniquement au véhicule désigné suivant :\n"
        "(numéro de référence écrit à la section « Conditions particulières » du contrat d'assurance)\n"
        "Description de l'avenant\n"
        "Cet avenant modifie le contrat d'assurance :\n"
        "\t lorsque le véhicule visé est loué ou pris en crédit-bail; et\n"
        "\t lorsque le propriétaire et un locataire ou crédit-preneur de ce véhicule sont désignés comme "
        "assurés au contrat d'assurance.\n"
        "L'expression « assuré désigné » est alors remplacée par « locataire désigné » ou, selon le cas, "
        "par « crédit-preneur désigné », dans la définition des « véhicules assurés » suivants :\n"
        "\t Véhicule dont l'assuré désigné est nouvellement propriétaire.\n"
        "\t Véhicule de remplacement temporaire.\n"
        "\t Véhicule dont l'assuré désigné n'est pas propriétaire.\n"
        "\t Remorque ou semi-remorque dont l'assuré désigné est propriétaire.\n"
        "\t Remorque ou semi-remorque dont l'assuré désigné n'est pas propriétaire et qui est "
        "utilisée avec un véhicule assuré au contrat d'assurance.\n"
        "Toutes les autres conditions du contrat d'assurance restent les mêmes.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
