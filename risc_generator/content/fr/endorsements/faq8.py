from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq8_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Formulaire d'avenant du Québec\n"
        "F.A.Q. N 8\n"
        "Franchise pour les dommages matériels\n"
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
        "Cet avenant modifie le chapitre A du contrat d'assurance en y ajoutant une franchise pour les "
        "dommages matériels causés par le véhicule visé :\n"
        "\t Une franchise d'un montant maximum de  $ par sinistre.\n"
        "\t Une franchise d'un montant maximum de  $ par sinistre, lorsque le véhicule est utilisé pour .\n"
        "Engagement de l'assuré désigné\n"
        "Lorsque l'assureur paie une indemnité pour des dommages matériels, l'assuré désigné "
        "s'engage à rembourser l'assureur jusqu'à concurrence du montant de la franchise.\n"
        "Le montant à rembourser est exigible de l'assuré désigné dès que l'assureur paie l'indemnité.\n"
        "Droits de l'assureur\n"
        "À l'égard de la franchise, l'assureur a le droit :\n"
        "\t d'agir comme il le veut en matière d'enquête, de transaction ou de règlement;\n"
        "\t d'autoriser l'assuré désigné à conclure une transaction ou un règlement avec "
        "toute autre personne qui a subi un dommage matériel et à indemniser cette "
        "personne. Par contre, le total des montants convenus à la suite de la "
        "transaction ou du règlement ne doit pas dépasser le montant de la franchise.\n"
        "Toutes les autres conditions du contrat d'assurance restent les mêmes.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
