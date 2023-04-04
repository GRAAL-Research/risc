from ..config import (
    GENERAL_FAKE_PHONE_NUMBER_1_800,
    NEW_PAGE_TAG,
    FAKE_FIDELITY_PROGRAM_NAME_FR,
    FAKE_ROADSIDE_ASSISTANCE_PHONE_NUMBER,
    FAKE_ROADSIDE_PROGRAM_NAME,
)


def generate_important_instructions_text(self) -> str:
    important_instructions = (
        f"INSTRUCTIONS IMPORTANTES\n\n"
        f"{self.formatted_text_date()}\n"
        f"Vous trouverez ci-dessous des instructions concernant des éléments très "
        f"importants de votre police d'assurance et nous vous recommandons de les "
        f"lire attentivement et d'y donner suite s'il y a lieu.\n\n"
    )

    fidelity = (
        f"Programme {FAKE_FIDELITY_PROGRAM_NAME_FR}\n\n"
        f"Parce que votre fidélité nous tient à coeur, nous sommes heureux de vous offrir des privilèges "
        f"qui s'accumulent en même temps que vos années de fidélité, grâce à notre programme "
        f"{FAKE_FIDELITY_PROGRAM_NAME_FR}. Voici le détail de vos privilèges, "
        f"que vous trouverez également dans votre Espace client.\n"
        f"Votre fidélité reconnue: Nouveau client\n"
        f"Vos privilèges:\n"
        f"\t Offres exclusives chez nos partenaires\n"
        f"\t Assistance juridique\n"
        f"\t Service d'aide psychologique\n"
    )

    if self.protections.is_protected("FAQ41Coverage"):
        fidelity += "\t Congé de franchise en cas de perte totale ou de délit de fuite (auto)\n"

    fidelity += (
        "Cette liste représente l'ensemble des privilèges associés à votre fidélité reconnue. "
        "Veuillez noter que les nouveaux privilèges seront disponibles au "
        "moment du renouvellement de chacune des polices d'assurance détenues par un "
        "membre de votre maisonnée. Référez-vous aux Conditions "
        "particulières de vos divers contrats d'assurance détenus chez "
        "nous pour connaître le détail des protections applicables.\n"
    )

    if (
        self.protections.is_protected("FAQ33Coverage")
        or self.protections.is_protected("FAQ5ACoverage")
        or self.protections.is_protected("FAQ23ACoverage")
    ):
        notice_to_the_insuree = "Avis à l'assuré\n"
    else:
        notice_to_the_insuree = ""

    if self.protections.is_protected("FAQ33Coverage"):
        notice_to_the_insuree += (
            f"POLICE AUTOMOBILE N {self.policy_number}\n"
            f"Vous avez opté pour {FAKE_ROADSIDE_PROGRAM_NAME} assistance routière, qui vous procure des services de "
            f"dépannage partout au Canada et aux États-Unis, 24 heures sur 24, "
            f"365 jours par année.\n"
            f"Ainsi, trois semaines après la date de prise d'effet de l'avenant F.A.Q. N 33 "
            f"Assurance des frais de dépannage, vous recevrez une trousse pour "
            f"chaque véhicule admissible, contenant entre autres votre carte d'adhérent ainsi "
            f"que votre guide de l'usager.\n"
            f"Dès que l'avenant F.A.Q. N 33 entrera en vigueur, vous pourrez bénéficier de ce "
            f"service même si vous n'avez pas reçu votre trousse {FAKE_ROADSIDE_PROGRAM_NAME} "
            f"assistance routière. En cas de besoin, il vous suffira de composer le "
            f"{FAKE_ROADSIDE_ASSISTANCE_PHONE_NUMBER} (24 heures sur 24, 7 jours sur 7) et de mentionner le numéro de "
            f"police du véhicule couvert au préposé.\n"
        )

    if self.protections.is_protected("FAQ5ACoverage") or self.protections.is_protected("FAQ23ACoverage"):
        if self.protections.is_protected("FAQ5ACoverage"):
            creditor_type = "locateur"
        else:
            creditor_type = "créancier"
        notice_to_the_insuree += (
            f"POLICE AUTOMOBILE N {self.policy_number} - Véhicule 1 : "
            f"{self.vehicle.format_vehicle_make_model_year_details()}\n"
            f"Nous joignons une copie de votre police à remettre à votre {creditor_type}, "
            f"s'il la demande. Elle se trouve à la toute fin du présent envoi.\n"
        )

    actions_to_take = (
        f"\nActions à entreprendre\n\n"
        f"Assurance auto\n"
        f"\t Détachez et conservez avec vous vos certificats d'assurance.\n"
        f"\t Détachez et conservez avec votre permis de conduire le certificat "
        f"d'assurance pour location de voiture. Vous éviterez ainsi de débourser les frais "
        f"d'assurance additionnels auprès de l'agence de location.\n"
        f"\t Veuillez prendre connaissance de la section Conditions particulières de votre police "
        f"d'assurance automobile du Québec, afin de vous assurer que vos couvertures répondent "
        f"bien à vos besoins.\n"
        f"\t N'hésitez pas à joindre le service à la clientèle au "
        f"{GENERAL_FAKE_PHONE_NUMBER_1_800} pour toute question relative à votre contrat.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    text = important_instructions + fidelity + notice_to_the_insuree + NEW_PAGE_TAG + "\n" + actions_to_take

    return text
