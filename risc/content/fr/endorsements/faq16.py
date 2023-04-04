from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq16_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Formulaire d'avenant du Québec\n"
        "F.A.Q. N 16\n"
        "Suspension de garanties lors du remisage du véhicule\n"
        "Le titre de l'avenant doit être écrit à la section « Conditions particulières » du contrat "
        "d'assurance. Quant aux informations requises dans l'avenant, elles peuvent être écrites à cette "
        "section ou dans l'avenant même, au choix de l'assureur.\n"
        "Nom de l'assureur : \n"
        "Nom de l'assuré désigné : \n"
        "Avenant à la police d'assurance automobile N : \n"
        "Date de prise d'effet : cet avenant s'applique à partir du à 0 h 01, heure normale "
        "à l'adresse de l'assuré désigné.\n"
        "Date du remisage : à 0 h 01, heure normale à l'adresse de l'assuré désigné\n"
        "Véhicule visé : cet avenant s'applique uniquement au véhicule désigné suivant :\n"
        "(numéro de référence écrit à la section « Conditions particulières » du contrat d'assurance)\n"
        "Description de l'avenant\n"
        "Cet avenant suspend certaines garanties du contrat d'assurance en raison du remisage du véhicule visé.\n"
        "Suspension des garanties\n"
        "L'assuré désigné déclare que le véhicule visé sera retiré de la circulation et remisé à la date du "
        "remisage. Il demande donc qu'à partir de cette date, les garanties suivantes soient suspendues :\n"
        "1. Garanties suspendues au chapitre A\n"
        "Les garanties du chapitre A du contrat d'assurance sont suspendues en ce qui concerne la conduite ou "
        "l'usage des véhicules suivants :\n"
        "\t le véhicule visé;\n"
        "\t tout véhicule dont l'assuré désigné est nouvellement propriétaire qui remplace le véhicule "
        "visé ou qui s'y ajoute;\n"
        "\t tout véhicule de remplacement temporaire qui remplace le véhicule visé.\n"
        "L'assuré désigné continue de bénéficier des autres garanties du chapitre A.\n"
        "2. Garanties suspendues au chapitre B\n"
        "Les garanties des Protections 1 et 2 du chapitre B du contrat d'assurance sont suspendues en ce qui "
        "concerne la conduite des véhicules suivants :\n"
        "\t le véhicule visé;\n"
        "\t tout véhicule dont l'assuré désigné est nouvellement propriétaire qui remplace le véhicule "
        "visé ou qui s'y ajoute;\n"
        "\t tout véhicule de remplacement temporaire qui remplace le véhicule visé.\n"
        "L'assuré désigné continue de bénéficier des autres garanties du chapitre B.\n"
        f"{NEW_PAGE_TAG}\n"
        f"{endorsement_header_text}"
        "Fin de la suspension des garanties\n"
        "Les garanties suspendues sont remises en vigueur à l'une des dates suivantes :\n"
        "\t à la date déterminée par l'assuré désigné, à condition qu'il en ait d'abord informé l'assureur;\n"
        "si aucune date n'est ainsi déterminée, au 1er avril qui suit la date du remisage.\n"
        "Le contrat d'assurance doit être en vigueur pour que les garanties puissent être remises en vigueur.\n"
        "Ristourne\n"
        "L'assuré désigné a droit à une ristourne pour la période de remisage, calculée sur la base suivante :\n"
        "Toutes les autres conditions du contrat d'assurance restent les mêmes.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
