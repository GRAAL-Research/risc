from risc_generator import Protections, FPQ1Contract
from tests.domain.contract.contract_base import ContractTestBase


class ContractCancellationOfPolicyTest(ContractTestBase):
    def test_givenAFRContract_whenGenerateCancellationOfPolicyText_thenReturnProperFRText(self):
        a_protections = Protections(protections=self.a_dict_of_protections.copy())

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fpq1_contract.generate_cancellation_of_policy_text()

        a_general_phone_number = "123 456-7890"
        a_general_phone_number_1_800 = "1 800 123-4567"
        a_policy_number = "1234567-001"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "POLICE D'ASSURANCE AUTOMOBILE DU QUÉBEC\n"
            "F.P.Q. N 1 - FORMULAIRE DES PROPRIÉTAIRES\n"
            f"Numéro de police : {a_policy_number}\n\n"
            "RÉSILIATION DE LA POLICE\n"
            "Ne pas utiliser cette formule si votre police couvre plusieurs véhicules et qu'un seul doit être résilié. "
            "Veuillez communiquer avec le service à la clientèle au numéro inscrit ci-dessous.\n"
            f"AVANT DE RÉSILIER communiquez avec le service à la clientèle au {a_general_phone_number} ou "
            f"{a_general_phone_number_1_800}; ceci pourrait vous éviter de perdre certains avantages.\n"
            f"Je demande la résiliation complète de la police numéro {a_policy_number}, de ses avenants, de ses "
            f"renouvellements et s'il y a lieu, le remboursement de la prime non acquise à compter du : "
            f"______________      ______________      ______________\n"
            f"(Année) (Mois) (Jour)\n"
            f"Signature :  ____________________________________________________________   "
            f"Date : _____________     _____________     _____________\n"
            f"(Assuré) (Année) (Mois) (Jour)\n"
            f"Signature :  ____________________________________________________________   "
            f"Date : _____________     _____________     _____________\n"
            f"(Assuré additionnel) (Année) (Mois) (Jour)\n"
            f"Signature :  ____________________________________________________________   "
            f"Date : _____________     _____________     _____________\n "
            f"(Assuré additionnel) (Année) (Mois) (Jour)\n"
            f"Raison de l'annulation :  _____________________________________________  "
            f"Nouvel assureur :  ________________________________________\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContract_whenGenerateCancellationOfPolicyText_thenReturnProperENText(self):
        a_protections = Protections(protections=self.a_dict_of_protections.copy())

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = fpq1_contract.generate_cancellation_of_policy_text()

        a_general_phone_number = "123 456-7890"
        a_general_phone_number_1_800 = "1 800 123-4567"
        a_policy_number = "1234567-001"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "QUEBEC AUTOMOBILE INSURANCE POLICY\n"
            "Q.P.F. B 1 - OWNER'S FORM\n"
            f"Policy Number: {a_policy_number}\n\n"
            f"CANCELLATION OF POLICY\n"
            f"If your policy covers several vehicles and coverage for only one of them must be cancelled, "
            f"do not use this form.\n"
            f"Please contact Customer Service at the number listed below.\n"
            f"BEFORE CANCELLING contact Customer Service at {a_general_phone_number} or "
            f"{a_general_phone_number_1_800}, this could avoid you losing some of your advantages.\n"
            f"I hereby request the full cancellation of policy number {a_policy_number}, "
            f"its endorsements, its renewals and if applicable, the reimbursement of any unearned premium effective: "
            f"______________      ______________      ______________\n"
            f"(Year) (Month) (Day)\n"
            f"Signature :  ____________________________________________________________   "
            f"Date : _____________     _____________     _____________\n"
            f"(Insured) (Year) (Month) (Day)\n"
            f"Signature :  ____________________________________________________________   "
            f"Date : _____________     _____________     _____________\n"
            f"(Additional Insured) (Year) (Month) (Day)\n"
            f"Signature :  ____________________________________________________________   "
            f"Date : _____________     _____________     _____________\n "
            f"(Additional Insured) (Year) (Month) (Day)\n"
            f"Reason of cancellation:  _____________________________________________  "
            f"New insurer:  ________________________________________\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)
