from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq32_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Formulaire d'avenant du Québec\n"
        "F.A.Q. N 32\n"
        "Véhicules à but uniquement récréatif\n"
        "Le titre de l'avenant doit être écrit à la section « Conditions particulières » du contrat d'assurance.\n"
        "Nom de l'assureur : \n"
        "Nom de l'assuré désigné : \n"
        "Avenant à la police d'assurance automobile N : \n"
        "Date de prise d'effet : cet avenant s'applique à partir du à 0 h 01, heure normale "
        "à l'adresse de l'assuré désigné.\n"
        "Véhicule visé : cet avenant s'applique uniquement au véhicule désigné suivant :\n"
        "(numéro de référence écrit à la section « Conditions particulières » du contrat d'assurance)\n"
        "Description de l'avenant\n"
        "Cet avenant modifie le contrat d'assurance pour le véhicule automobile à but uniquement récréatif qui :\n"
        "\t est expressément désigné à l'article 3 de la section « Conditions particulières » du contrat "
        "d'assurance; ou\n"
        "\t fait partie des « véhicules assurés » du contrat d'assurance.\n"
        "Véhicule automobile à but uniquement récréatif\n"
        "Un « véhicule automobile à but uniquement récréatif » vise, entre autres, tout véhicule "
        "automobile qui est ou non de fabrication commerciale, et qui est assimilable :\n"
        "\t aux « dune buggies »;\n"
        "\t aux mini-motos;\n"
        "\t aux mini-voitures;\n"
        "\t aux motoneiges; et\n"
        "aux véhicules automobiles tout-terrain.\n"
        "Description des modifications\n"
        "1. Chapitre A : le paragraphe E. de l'article 2. intitulé « Véhicules assurés » est remplacé "
        "par le paragraphe suivant :\n"
        "« E. Sauf si elle est désignée à la section « Conditions particulières », toute remorque "
        "(qu'elle appartienne ou non à l'assuré désigné) utilisée avec un véhicule automobile "
        "à but uniquement récréatif qui est :\n"
        "\t du même type que celui désigné à la section « Conditions particulières »; et\n"
        "\t couvert par le contrat d'assurance. »\n"
        "2. Conditions générales : le paragraphe a) de l'article 7. intitulé « Usages interdits "
        "d'un véhicule assuré » est remplacé par le paragraphe suivant :\n"
        "« a) Elles ne sont pas autorisées à conduire par la loi; »\n"
        f"{NEW_PAGE_TAG}\n"
        f"{endorsement_header_text}"
        "3. Les expressions « véhicule automobile » et « véhicule automobile utilisé à des "
        "fins personnelles » sont remplacées partout dans le contrat d'assurance par l'expression suivante :\n"
        "« véhicule automobile à but uniquement récréatif du même type que celui désigné à la section "
        "« Conditions particulières » ».\n"
        "Toutes les autres conditions du contrat d'assurance restent les mêmes.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
