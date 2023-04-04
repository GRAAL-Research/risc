from risc_generator import FPQ1Contract, Insuree
from risc_generator.content import fr, en
from tests.domain.contract.contract_base import ContractTestBase

INCLUDE = "include"
EXCLUDE = "exclude"


class ContractDeclarationTest(ContractTestBase):
    def test_givenAFRContractNoRebates_whenGenerateItem7Text_thenReturnProperFRText(self):
        a_association_rebate = False
        payment_method = "bill"

        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=self.a_suspension,
            number_of_claims_past_years=self.a_number_of_claims_past_years,
            association_rebate=a_association_rebate,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=payment_method,
            protections=self.a_protections,
            premium=self.a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_7_text(
            association_rebate=fpq1_contract.insuree.association_rebate, payment_method=fpq1_contract.payment_method
        )

        expected = (
            "Article 7. INFORMATIONS POUR L'ASSURÉ DÉSIGNÉ\n"
            "\t Consentement : Si une autorisation nous a été donnée afin d'obtenir des informations de crédit "
            "pour l'émission du présent contrat, veuillez noter que les renseignements obtenus seront mis à "
            "jour et utilisés pour votre renouvellement et pour le traitement de vos dossiers d'assurances "
            "générales. Ce consentement peut être révoqué en tout temps en nous avisant par écrit.\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractWithAssociationRebate_whenGenerateItem7Text_thenReturnProperFRText(self):
        a_association_rebate = True
        payment_method = "bill"

        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=self.a_suspension,
            number_of_claims_past_years=self.a_number_of_claims_past_years,
            association_rebate=a_association_rebate,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=payment_method,
            protections=self.a_protections,
            premium=self.a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_7_text(
            association_rebate=fpq1_contract.insuree.association_rebate, payment_method=fpq1_contract.payment_method
        )

        expected = (
            "Article 7. INFORMATIONS POUR L'ASSURÉ DÉSIGNÉ\n"
            "\t La prime tient comptes des réductions suivantes :\n"
            "- En tant que membre/client d'une association, vous avez droit au rabais suivant: 10%.\n"
            "\t Consentement : Si une autorisation nous a été donnée afin d'obtenir des informations de crédit "
            "pour l'émission du présent contrat, veuillez noter que les renseignements obtenus seront mis à "
            "jour et utilisés pour votre renouvellement et pour le traitement de vos dossiers d'assurances "
            "générales. Ce consentement peut être révoqué en tout temps en nous avisant par écrit.\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractWithPaymentRebate_whenGenerateItem7Text_thenReturnProperFRText(self):
        a_association_rebate = False
        payment_method = "pre-authorize"

        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=self.a_suspension,
            number_of_claims_past_years=self.a_number_of_claims_past_years,
            association_rebate=a_association_rebate,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=payment_method,
            protections=self.a_protections,
            premium=self.a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_7_text(
            association_rebate=fpq1_contract.insuree.association_rebate, payment_method=fpq1_contract.payment_method
        )

        expected = (
            "Article 7. INFORMATIONS POUR L'ASSURÉ DÉSIGNÉ\n"
            "\t La prime tient comptes des réductions suivantes :\n"
            "- 2 % pour avoir choisi le Prélèvement préautorisé comme mode de paiement de votre prime\n"
            "\t Consentement : Si une autorisation nous a été donnée afin d'obtenir des informations de crédit "
            "pour l'émission du présent contrat, veuillez noter que les renseignements obtenus seront mis à "
            "jour et utilisés pour votre renouvellement et pour le traitement de vos dossiers d'assurances "
            "générales. Ce consentement peut être révoqué en tout temps en nous avisant par écrit.\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractWithAssociationAndPaymentRebate_whenGenerateItem7Text_thenReturnProperFRText(self):
        a_association_rebate = True
        payment_method = "pre-authorize"

        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=self.a_suspension,
            number_of_claims_past_years=self.a_number_of_claims_past_years,
            association_rebate=a_association_rebate,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=payment_method,
            protections=self.a_protections,
            premium=self.a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_7_text(
            association_rebate=fpq1_contract.insuree.association_rebate, payment_method=fpq1_contract.payment_method
        )

        expected = (
            "Article 7. INFORMATIONS POUR L'ASSURÉ DÉSIGNÉ\n"
            "\t La prime tient comptes des réductions suivantes :\n"
            "- En tant que membre/client d'une association, vous avez droit au rabais suivant: 10%.\n"
            "- 2 % pour avoir choisi le Prélèvement préautorisé comme mode de paiement de votre prime\n"
            "\t Consentement : Si une autorisation nous a été donnée afin d'obtenir des informations de crédit "
            "pour l'émission du présent contrat, veuillez noter que les renseignements obtenus seront mis à "
            "jour et utilisés pour votre renouvellement et pour le traitement de vos dossiers d'assurances "
            "générales. Ce consentement peut être révoqué en tout temps en nous avisant par écrit.\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractNoRebates_whenGenerateItem7Text_thenReturnProperENText(self):
        a_association_rebate = False
        payment_method = "bill"

        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=self.a_suspension,
            number_of_claims_past_years=self.a_number_of_claims_past_years,
            association_rebate=a_association_rebate,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=payment_method,
            protections=self.a_protections,
            premium=self.a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_7_text(
            association_rebate=fpq1_contract.insuree.association_rebate, payment_method=fpq1_contract.payment_method
        )

        expected = (
            "Item 7. INFORMATION FOR THE NAMED INSURED\n"
            "\t Consent:If authorization has been granted for us to obtain credit information for the purposes of "
            "issuing this contract, please note that the information obtained will be updated and used for renewing "
            "your contract and for processing your property and casualty insurance files. This consent can be revoked "
            "at any time by notifying us in writing.\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractWithAssociationRebate_whenGenerateItem7Text_thenReturnProperENText(self):
        a_association_rebate = True
        payment_method = "bill"

        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=self.a_suspension,
            number_of_claims_past_years=self.a_number_of_claims_past_years,
            association_rebate=a_association_rebate,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=payment_method,
            protections=self.a_protections,
            premium=self.a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_7_text(
            association_rebate=fpq1_contract.insuree.association_rebate, payment_method=fpq1_contract.payment_method
        )

        expected = (
            "Item 7. INFORMATION FOR THE NAMED INSURED\n"
            "\t The premium takes into account the following discounts:\n"
            "- As a member/customer of an association, you are eligible for the following discount: 10%.\n"
            "\t Consent:If authorization has been granted for us to obtain credit information for the purposes of "
            "issuing this contract, please note that the information obtained will be updated and used for renewing "
            "your contract and for processing your property and casualty insurance files. This consent can be revoked "
            "at any time by notifying us in writing.\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractWithPaymentRebate_whenGenerateItem7Text_thenReturnProperENText(self):
        a_association_rebate = False
        payment_method = "pre-authorize"

        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=self.a_suspension,
            number_of_claims_past_years=self.a_number_of_claims_past_years,
            association_rebate=a_association_rebate,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=payment_method,
            protections=self.a_protections,
            premium=self.a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_7_text(
            association_rebate=fpq1_contract.insuree.association_rebate, payment_method=fpq1_contract.payment_method
        )

        expected = (
            "Item 7. INFORMATION FOR THE NAMED INSURED\n"
            "\t The premium takes into account the following discounts:\n"
            "- 2% for choosing Pre-authorized payment as your premium payment method\n"
            "\t Consent:If authorization has been granted for us to obtain credit information for the purposes of "
            "issuing this contract, please note that the information obtained will be updated and used for renewing "
            "your contract and for processing your property and casualty insurance files. This consent can be revoked "
            "at any time by notifying us in writing.\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractWithAssociationAndPaymentRebate_whenGenerateItem7Text_thenReturnProperENText(self):
        a_association_rebate = True
        payment_method = "pre-authorize"

        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=self.a_suspension,
            number_of_claims_past_years=self.a_number_of_claims_past_years,
            association_rebate=a_association_rebate,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=payment_method,
            protections=self.a_protections,
            premium=self.a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_7_text(
            association_rebate=fpq1_contract.insuree.association_rebate, payment_method=fpq1_contract.payment_method
        )

        expected = (
            "Item 7. INFORMATION FOR THE NAMED INSURED\n"
            "\t The premium takes into account the following discounts:\n"
            "- As a member/customer of an association, you are eligible for the following discount: 10%.\n"
            "- 2% for choosing Pre-authorized payment as your premium payment method\n"
            "\t Consent:If authorization has been granted for us to obtain credit information for the purposes of "
            "issuing this contract, please note that the information obtained will be updated and used for renewing "
            "your contract and for processing your property and casualty insurance files. This consent can be revoked "
            "at any time by notifying us in writing.\n"
        )

        self.assertEqual(expected, actual)
