from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq20_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Formulaire d'avenant du Québec\n"
        "F.A.Q. N 20\n"
        "Frais de déplacement\n"
        "(Chapitre B)\n"
        "Le titre de l'avenant doit être écrit à la section « Conditions particulières » du contrat "
        "d'assurance. Quant aux informations requises dans l'avenant, elles peuvent être écrites à "
        "cette section ou dans l'avenant même, au choix de l'assureur.\n"
        "Nom de l'assureur :  \n"
        "Nom de l'assuré désigné :  \n"
        "Avenant à la police d'assurance automobile N :  \n"
        "Date de prise d'effet : cet avenant s'applique à partir du  à 0 h 01, heure normale "
        "à l'adresse de l'assuré désigné.\n"
        "Prime d'assurance additionnelle à payer :\n"
        "\t Montants à payer :  \n"
        "\t Date limite pour payer :  \n"
        "Véhicule visé : cet avenant s'applique uniquement au véhicule désigné suivant :\n"
        "(numéro de référence écrit à la section « Conditions particulières » du contrat d'assurance)\n"
        "Description de l'avenant\n"
        "Cet avenant étend les garanties du chapitre B du contrat d'assurance, en remplaçant le texte de la "
        "garantie additionnelle 4.1 intitulée « Frais de déplacement en cas de vol d'un véhicule assuré », "
        "par le texte ci-dessous.\n"
        "Cet avenant s'applique uniquement au véhicule visé et seulement si la valeur des dommages subis par "
        "le véhicule visé est supérieure à la franchise applicable au sinistre qui les a causés.\n"
        "« 4.1 Frais de déplacement\n"
        "4.1.1 Description des frais de déplacement\n"
        "Si l'assuré désigné ne peut plus utiliser le véhicule assuré en raison d'un sinistre couvert, "
        "l'assureur lui rembourse les frais suivants :\n"
        "\t les frais de location pour un véhicule de remplacement temporaire;\n"
        "\t les frais de taxi;\n"
        "\t les frais de transport en commun.\n"
        "Sur production des reçus de paiement, ces frais sont remboursés jusqu'à un montant maximum "
        "de $ par jour et de $ par sinistre et par véhicule assuré.\n"
        "Ces montants ne peuvent pas être inférieurs aux montants qui étaient écrits à la garantie "
        "additionnelle 4.1 du contrat d'assurance.\n"
        f"{NEW_PAGE_TAG}\n"
        f"{endorsement_header_text}"
        "4.1.2 Application de la garantie\n"
        "Si le véhicule assuré a été volé en entier, cette garantie s'applique uniquement aux frais engagés "
        "à partir de 0 h 01 le lendemain de la déclaration de vol à la police ou à l'assureur.\n"
        "Pour tous les autres sinistres couverts, cette garantie s'applique uniquement aux frais engagés :\n"
        "\t dès le moment où le véhicule assuré ne peut plus rouler en raison des dommages qu'il a subis; ou\n"
        "\t s'il est encore en état de rouler malgré les dommages subis, dès le moment où il est "
        "confié à un réparateur.\n"
        "Les frais sont remboursables malgré l'expiration du contrat d'assurance depuis le sinistre.\n"
        "Ces frais cessent d'être remboursés :\n"
        "\t lorsque le véhicule assuré est remplacé ou réparé; ou\n"
        "\t lorsqu'une entente sur le règlement du sinistre est conclue avant que le véhicule "
        "assuré soit remplacé ou réparé. »\n"
        "Toutes les autres conditions du contrat d'assurance restent les mêmes.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
