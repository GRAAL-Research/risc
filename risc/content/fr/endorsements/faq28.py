from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq28_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Formulaire d'avenant du Québec\n"
        "F.A.Q. N 28\n"
        "Restriction de garanties pour les conducteurs désignés\n"
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
        "Cet avenant restreint les garanties du contrat d'assurance lorsque le véhicule visé est, au "
        "moment du sinistre, conduit ou utilisé par :  (nom du conducteur désigné)\n"
        "Dans un tel cas, seuls sont couverts les risques suivants, ou ceux écrits spécifiquement pour cet avenant "
        "à la section « Conditions particulières » du contrat d'assurance :\n"
        "GARANTIES | RISQUES | MONTANT D'ASSURANCE ET FRANCHISES | COUVERT/NON COUVERT\n"
        "Chapitre A : Responsabilité civile | Dommages matériels ou dommages corporels causés à "
        "d'autres personnes | Montant d'assurance :  $ |  $\n"
        "Chapitre B : Dommages aux véhicules assurés | Protection 1 : « Tous risques », Protection 2 : "
        "Risques de collision et de renversement, Protection 3 : Tous les risques sauf collision ou renversement, "
        "Protection 4 : Risques spécifiques | Franchise par sinistre : $ $ $ $ |      \n"
        "Toutes les autres conditions du contrat d'assurance restent les mêmes.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
