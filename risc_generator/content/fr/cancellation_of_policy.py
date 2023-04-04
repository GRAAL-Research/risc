from .general_header import generate_general_pages_header_text
from ..config import GENERAL_FAKE_PHONE_NUMBER_1_800, NEW_PAGE_TAG, GENERAL_FAKE_PHONE_NUMBER


def generate_cancellation_of_policy_text(self):
    general_header_text = generate_general_pages_header_text(policy_number=self.policy_number)

    text = (
        f"{general_header_text}"
        "RÉSILIATION DE LA POLICE\n"
        "Ne pas utiliser cette formule si votre police couvre plusieurs "
        "véhicules et qu'un seul doit être résilié. "
        "Veuillez communiquer avec le service à la clientèle au numéro inscrit ci-dessous.\n"
        f"AVANT DE RÉSILIER communiquez avec le service à la clientèle au {GENERAL_FAKE_PHONE_NUMBER} ou "
        f"{GENERAL_FAKE_PHONE_NUMBER_1_800}; ceci pourrait vous éviter de perdre certains avantages.\n"
        f"Je demande la résiliation complète de la police numéro {self.policy_number}, "
        "de ses avenants, de ses renouvellements et s'il y a lieu, le remboursement de la prime "
        "non acquise à compter du : ______________      ______________      ______________\n"
        "(Année) (Mois) (Jour)\n"
        "Signature :  ____________________________________________________________   "
        "Date : _____________     _____________     _____________\n"
        "(Assuré) (Année) (Mois) (Jour)\n"
        "Signature :  ____________________________________________________________   "
        "Date : _____________     _____________     _____________\n"
        "(Assuré additionnel) (Année) (Mois) (Jour)\n"
        "Signature :  ____________________________________________________________   "
        "Date : _____________     _____________     _____________\n "
        "(Assuré additionnel) (Année) (Mois) (Jour)\n"
        "Raison de l'annulation :  _____________________________________________  "
        "Nouvel assureur :  ________________________________________\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
