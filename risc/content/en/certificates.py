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
        "The insured vehicle's insurance certificates can now be downloaded into the Apple Wallet application. "
        "Details on the back.\n"
    )

    if self.protections.is_protected("FAQ27Coverage") or self.protections.is_protected("FAQ27aCoverage"):
        text += (
            f"Q.E.F. N 27 : YOUR RENTAL VEHICLE INSURANCE CERTIFICATE\n"
            f"The next time you rent a car, show this certificate to the rental agent to avoid paying additional "
            f"insurance fees. It's valid in Canada and the United States up to a maximum of "
            f"Details on back of the certificate.\n"
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
            f"Need to file an insurance claim?\n"
            f"Contact us.\n"
            f"Claims Department open 24/7\n"
            f"Local: {CLAIMS_FAKE_PHONE_NUMBER}\n"
            f"Toll free: {CLAIMS_FAKE_PHONE_NUMBER_1_800}\n"
            f"Customer Service\n"
            f"Toll free:{GENERAL_FAKE_PHONE_NUMBER_1_800}\n\n"
        )

    text += (
        f"HERE ARE YOUR TWO INSURANCE CERTIFICATES FOR THE INSURED VEHICLE\n"
        f"NUMÉRO DE POLICE / POLICY NUMBER\n\n"
        f"{self.policy_number}\n"
        f"{self.insuree.name}\n"
        f"{self.insuree.address}\n"
        f"VÉHICULE ASSURÉ / INSURED VEHICLE\n"
        f"{self.vehicle.format_vehicle_complete_details()}\n"
        f"DURÉE DU CONTRAT DU "
        f"{self.contract_start_date} AU {self.contract_end_date}\n"
        f"POLICY PERIOD FROM An/Yr M J/D TO An/Yr M J/D\n"
        f"Need to file an insurance claim?\n"
        f"Contact us.\n"
        f"Claims Department open 24/7\n"
        f"Local: {CLAIMS_FAKE_PHONE_NUMBER}\n"
        f"Toll free: {CLAIMS_FAKE_PHONE_NUMBER_1_800}\n"
        f"Customer Service\n"
        f"Toll free:{GENERAL_FAKE_PHONE_NUMBER_1_800}\n"
        f"NUMÉRO DE POLICE / POLICY NUMBER\n\n"
        f"{self.policy_number}\n"
        f"{self.insuree.name}\n"
        f"{self.insuree.address}\n"
        f"VÉHICULE ASSURÉ / INSURED VEHICLE\n"
        f"{self.vehicle.format_vehicle_complete_details()}\n"
        f"DURÉE DU CONTRAT DU "
        f"{self.contract_start_date} AU {self.contract_end_date}\n"
        f"POLICY PERIOD FROM An/Yr M J/D TO An/Yr M J/D\n"
        f"Need to file an insurance claim?\n"
        f"Contact us.\n"
        f"Claims Department open 24/7\n"
        f"Local: {CLAIMS_FAKE_PHONE_NUMBER}\n"
        f"Toll free: {CLAIMS_FAKE_PHONE_NUMBER_1_800}\n"
        f"Customer Service\n"
        f"Toll free:{GENERAL_FAKE_PHONE_NUMBER_1_800}\n\n"
        f"{NEW_PAGE_TAG}\n"
        "CANADA INTER-PROVINCE\n"
        "MOTOR VEHICLE LIABILITY INSURANCE CARD\n"
        "Keep with your driver's licence\n"
        f"To download your certificate into the Apple Wallet application (available on iPhone only):\n"
        f"\t1. Log in to the Client Centre from your phone at {FAKE_INSURER_WEBSITE}/clientcentre.\n"
        f"\t2. In the Home, auto and leisure vehicles section, click on ''Get an insurance certificate'', then"
        f"''Add to Apple Wallet''.\n"
        f"You will have to update your certificates at each renewal of, or change to, your insurance policy by "
        f"downloading it again to the Apple Wallet application.\n"
        f"{FAKE_INSURER_NAME} cannot guarantee that the electronic version of the certificates will be accepted by "
        f"all police forces. Make sure you always have a paper version on hand.\n\n"
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
