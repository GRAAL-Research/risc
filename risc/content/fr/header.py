from ..config import (
    GENERAL_FAKE_PHONE_NUMBER,
    GENERAL_FAKE_PHONE_NUMBER_1_800,
    FAKE_FAX_PHONE_NUMBER,
    FAKE_EMAIL,
    CLAIMS_FAKE_PHONE_NUMBER,
    CLAIMS_FAKE_PHONE_NUMBER_1_800,
    FAKE_LEGAL_HELP_PHONE_NUMBER,
    FAKE_INSURER_ADDRESS,
    FAKE_INSURER_WEBSITE,
    NEW_PAGE_TAG,
)


def generate_header_text(self) -> str:
    content_text = (
        f"{self.formatted_text_date()}\n\n\n"
        f"ÉMISSION\n"
        f"Numéro client: {self.client_number}\n"
        f"Police / Durée du terme:\n"
        f"{self.policy} / 12 mois\n\n"
        f"JAMAIS SEUL POUR VOS ASSURANCES\n\n"
        f"Vous trouverez vos documents d'assurance aux pages suivantes.\n"
        f"Nous vous suggérons de les lire attentivement afin de vous assurer qu'ils sont conformes.\n"
        f"Si une page Instructions importantes fait partie de ces documents, veuillez y porter une attention "
        f"particulière, puisqu'elle comporte des renseignements essentiels au sujet de vos protections.\n"
        f"N'hésitez pas à communiquer avec nous pour toute question ou commentaire.\n\n"
        f"NOUS JOINDRE\n"
        f"Service à la clientèle\n"
        f"{GENERAL_FAKE_PHONE_NUMBER}\n"
        f"{GENERAL_FAKE_PHONE_NUMBER_1_800}\n"
        f"Télécopieur: {FAKE_FAX_PHONE_NUMBER}\n"
        f"{FAKE_EMAIL}\n"
        f"8 h à 20 h du lundi au vendredi\n"
        f"8 h 30 à 16 h le samedi\n"
        f"Réclamations\n"
        f"{CLAIMS_FAKE_PHONE_NUMBER}\n"
        f"{CLAIMS_FAKE_PHONE_NUMBER_1_800}\n"
        f"Urgence 7 jours/24 heures\n"
        f"Assistance juridique\n"
        f"{FAKE_LEGAL_HELP_PHONE_NUMBER}\n"
        f"8 h 30 à 19 h du lundi au jeudi\n"
        f"8 h 30 à 17 h le vendredi\n"
        f"Votre succursale\n"
        f"{FAKE_INSURER_ADDRESS}\n"
        f"8 h 30 à 17 h du lundi au vendredi\n"
        f"{FAKE_INSURER_WEBSITE}\n"
    )
    if self.payment_method == "facture":
        # Case where payment is a bill, thus it include a billing section in the TDM
        content_text += (
            f"Vos documents d'assurance\n"
            f"(Table des matières)\n"
            f"Instructions importantes\n"
            f"Assurance automobile\n"
            f"Numéro police: {self.policy}\n"
            f"{self.vehicle.format_vehicle_make_year_details()}\n"
            f"Certificats d'assurance\n"
            f"(Documents à conserver)\n"
            f"Facturation\n"
            f"Avantages Client\n"
            f"(Description de vos bénéfices client)\n"
            f"Libellés et avenants\n"
            f"{NEW_PAGE_TAG}\n"
            f"{NEW_PAGE_TAG}\n"  # An empty page
        )
    else:
        # Case where payment is pre-authorized, thus no billing in the documents.
        content_text += (
            f"Vos documents d'assurance\n"
            f"(Table des matières)\n"
            f"Instructions importantes\n"
            f"Assurance automobile\n"
            f"Numéro police: {self.policy}\n"
            f"{self.vehicle.format_vehicle_make_year_details()}\n"
            f"Certificats d'assurance\n"
            f"(Documents à conserver)\n"
            f"Avantages Client\n"
            f"(Description de vos bénéfices client)\n"
            f"Libellés et avenants\n"
            f"{NEW_PAGE_TAG}\n"
            f"{NEW_PAGE_TAG}\n"  # An empty page
        )
    return content_text
