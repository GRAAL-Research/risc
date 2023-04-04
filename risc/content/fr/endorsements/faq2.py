from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq2_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Formulaire d'avenant du Québec\n"
        "F.A.Q. N 2\n"
        "Conduite de véhicules dont l'assuré désigné n'est pas propriétaire par des conducteurs désignés\n"
        "(Chapitre A)\n"
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
        "Description de l'avenant\n"
        "Cet avenant étend les garanties du chapitre A du contrat d'assurance en ajoutant le paragraphe "
        "suivant à l'article 2 intitulé « Véhicules assurés » :\n"
        "« tout véhicule assimilable à   et conduit, au moment du "
        "sinistre, par l'une des personnes suivantes :\n"
        "NOM | ÂGE | LIEN AVEC L'ASSURÉ DÉSIGNÉ\n"
        "1. | | \n"
        "2. | | \n"
        "3. | | \n"
        "4. | | \n"
        "Pour que ce véhicule soit considéré comme un « véhicule assuré » au chapitre A, "
        "les conditions suivantes doivent être respectées :\n"
        "1. Au moment du sinistre, le véhicule n'est pas conduit dans le cadre d'une "
        "activité professionnelle de garagiste.\n"
        "2. Le véhicule n'a pas comme propriétaire ou usager fréquent les personnes suivantes :\n"
        "\t l'assuré désigné ou toute personne ayant le même domicile que lui;\n"
        "\t toute personne désignée dans le tableau ci-dessus ou toute personne ayant le même "
        "domicile qu'elle.\n"
        f"{NEW_PAGE_TAG}\n"
        f"{endorsement_header_text}"
        "3. Le véhicule n'est pas fourni par un employeur :\n"
        "\t de l'assuré désigné ou de toute personne ayant le même domicile que lui;\n"
        "\t d'une personne désignée dans le tableau ci-dessus ou de toute personne ayant le même "
        "domicile qu'elle.\n"
        "4. Le véhicule n'est pas affecté :\n"
        "\t à l'usage de taxi, d'autobus ou d'autocar;\n"
        "\t à la livraison commerciale.»\n"
        "Toutes les autres conditions du contrat d'assurance restent les mêmes.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
