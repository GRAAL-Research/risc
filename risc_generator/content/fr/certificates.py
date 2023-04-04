from ..config import (
    CLAIMS_FAKE_PHONE_NUMBER,
    CLAIMS_FAKE_PHONE_NUMBER_1_800,
    GENERAL_FAKE_PHONE_NUMBER_1_800,
    FAKE_INSURER_WEBSITE,
    FAKE_INSURER_NAME,
    NEW_PAGE_TAG,
)
from ..fr_en.back_of_certificates import back_of_certificates_text


def generate_certificates_text(self) -> str:
    text = (
        "Les certiﬁcats d'assurance du véhicule assuré peuvent maintenant être téléchargés dans l'application "
        "Wallet de Apple. Détails au verso.\n"
    )

    if self.protections.is_protected("FAQ27Coverage") or self.protections.is_protected("FAQ27aCoverage"):
        text += (
            f"F.A.Q. N 27 : VOTRE CERTIFICAT POUR VÉHICULE DE LOCATION\n"
            f"Lors de votre prochaine location d'auto, présentez ce certiﬁcat au locateur pour "
            f"éviter des frais additionnels d'assurance. Il est valide au Canada et aux États-Unis "
            f"jusqu'à concurrence de Détails au verso du certiﬁcat.\n"
            f"NUMÉRO DE POLICE / POLICY NUMBER\n\n"
            f"{self.policy_number}\n"
            f"{self.insuree.name}\n"
            f"{self.insuree.address}\n"
            f"DURÉE DU CONTRAT DU "
            f"{self.contract_start_date} AU {self.contract_end_date}\n"
            f"POLICY PERIOD FROM An/Yr M J/D TO An/Yr M J/D\n"
            f"IMPORTANT\n"
            f"AU BESOIN, VEUILLEZ PRÉSENTER CE CERTIFICAT À VOTRE AGENCE DE LOCATION DE VOITURES\n"
            f"IF NECESSARY, PLEASE PRESENT THIS CERTIFICATE TO YOUR AUTOMOBILE RENTAL AGENCY\n"
            f"Vous voulez déclarer un sinistre?\n"
            f"Communiquez avec nous.\n"
            f"Service des sinistres 7 jours/24h :\n"
            f"Local: {CLAIMS_FAKE_PHONE_NUMBER}\n"
            f"Sans frais : {CLAIMS_FAKE_PHONE_NUMBER_1_800}\n"
            f"Service à la clientèle\n"
            f"Sans frais :{GENERAL_FAKE_PHONE_NUMBER_1_800}\n\n"
        )

    text += (
        f"VOICI VOS DEUX CERTIFICATS D'ASSURANCE POUR LE VÉHICULE ASSURÉ\n"
        f"NUMÉRO DE POLICE / POLICY NUMBER\n\n"
        f"{self.policy_number}\n"
        f"{self.insuree.name}\n"
        f"{self.insuree.address}\n"
        f"VÉHICULE ASSURÉ / INSURED VEHICLE\n"
        f"{self.vehicle.format_vehicle_complete_details()}\n"
        f"DURÉE DU CONTRAT DU "
        f"{self.contract_start_date} AU {self.contract_end_date}\n"
        f"POLICY PERIOD FROM An/Yr M J/D TO An/Yr M J/D\n"
        f"Vous voulez déclarer un sinistre?\n"
        f"Communiquez avec nous.\n"
        f"Service des sinistres 7 jours/24h :\n"
        f"Local: {CLAIMS_FAKE_PHONE_NUMBER}\n"
        f"Sans frais : {CLAIMS_FAKE_PHONE_NUMBER_1_800}\n"
        f"Service à la clientèle\n"
        f"Sans frais :{GENERAL_FAKE_PHONE_NUMBER_1_800}\n"
        f"NUMÉRO DE POLICE / POLICY NUMBER\n\n"
        f"{self.policy_number}\n"
        f"{self.insuree.name}\n"
        f"{self.insuree.address}\n"
        f"VÉHICULE ASSURÉ / INSURED VEHICLE\n"
        f"{self.vehicle.format_vehicle_complete_details()}\n"
        f"DURÉE DU CONTRAT DU "
        f"{self.contract_start_date} AU {self.contract_end_date}\n"
        f"POLICY PERIOD FROM An/Yr M J/D TO An/Yr M J/D\n"
        f"Vous voulez déclarer un sinistre?\n"
        f"Communiquez avec nous.\n"
        f"Service des sinistres 7 jours/24h :\n"
        f"Local: {CLAIMS_FAKE_PHONE_NUMBER}\n"
        f"Sans frais : {CLAIMS_FAKE_PHONE_NUMBER_1_800}\n"
        f"Service à la clientèle\n"
        f"Sans frais :{GENERAL_FAKE_PHONE_NUMBER_1_800}\n\n"
        f"{NEW_PAGE_TAG}\n"
        "CERTIFICATS D'ASSURANCE RESPONABILITÉ AUTOMOBILE\n"
        "CONSERVER AVEC VOTRE PERMIS DE CONDUIRE\n"
        f"Pour télécharger vos certiﬁcats dans l'application Wallet (disponible seulement sur iPhone) :\n"
        f"\t1. Connectez-vous à Espace client à partir de votre iPhone, au {FAKE_INSURER_WEBSITE}/espaceclient.\n"
        f"\t2. Dans la section Auto, habitation et véhicules de loisirs, cliquez sur « Obtenir "
        f"un certiﬁcat d'assurance », puis sur « Ajouter à Apple Wallet ».\n"
        f"Vous devrez mettre à jour vos certiﬁcats à chaque renouvellement ou modiﬁcation de votre police "
        f"d'assurance en les téléchargeant de nouveau dans l'application Wallet.\n"
        f"{FAKE_INSURER_NAME} ne peut pas garantir l'acceptation des certiﬁcats en format électronique par "
        f"tous les corps policiers. Assurez-vous de toujours en garder une version papier avec vous.\n\n"
    )

    if self.protections.is_protected("FAQ27Coverage") or self.protections.is_protected("FAQ27aCoverage"):
        text += (
            f"CERTIFICAT D'ASSURANCE POUR LOCATION DE VOITURE\n"
            f"(Valide au Canada et aux États-Unis d'Amérique seulement)\n"
            f"Application particulière de l'avenant F.A.Q. 27 : Responsabilité civile du fait de dommages causés à "
            f"des véhicules dont l'assuré désigné n'est pas propriétaire (incluant les véhicules fournis par un "
            f"employeur).\n"
            f"En cas de vol ou d'endommagement d'un véhicule de location, {FAKE_INSURER_NAME} s'engage "
            f"à rembourser, à l'Assuré ou au propriétaire du véhicule, le montant des dommages réellement encourus "
            f"et dont l'Assuré ou son conjoint s'est rendu responsable en vertu d'un contrat de location, le tout "
            f"jusqu'à concurrence de : 75 000 $\n\n"
            f"CAR RENTAL INSURANCE CERTIFICATE\n"
            f"(Valid only in Canada and the United States of America)\n"
            f"Speciﬁc application of Q.E.F. endorsement B 27 : Civil liability resulting from damage caused to "
            f"vehicles of which named insured is not owner (including vehicles provided by an employer).\n"
            f"In the event of theft or damage to a rental vehicle, {FAKE_INSURER_NAME} "
            f"agrees to refund the Insured or the owner of the vehicle, the amount of damage actually "
            f"incurred and for which the Insured or his/her spouse assumes liability under a rental "
            f"contract, in all up to: $75,000\n"
        )

    # Two certificates
    text += back_of_certificates_text
    text += back_of_certificates_text
    text += NEW_PAGE_TAG + "\n"

    return text
