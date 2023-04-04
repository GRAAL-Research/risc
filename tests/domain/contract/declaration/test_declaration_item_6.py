from risc_generator import FPQ1Contract, Insuree
from risc_generator.content import fr, en
from tests.domain.contract.contract_base import ContractTestBase

INCLUDE = "include"
EXCLUDE = "exclude"


class ContractDeclarationTest(ContractTestBase):
    def test_givenAFRContractInsureeNoSuspensionOrClaims_whenGenerateItem6Text_thenReturnProperFRText(self):
        a_suspension = False
        a_number_of_claims_past_years = 0
        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=a_suspension,
            number_of_claims_past_years=a_number_of_claims_past_years,
            association_rebate=self.a_association_rebate,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_6_text(
            insuree_name=fpq1_contract.insuree.name,
            insuree_birth_date=fpq1_contract.insuree.date_of_birth,
            has_suspension=fpq1_contract.insuree.suspension,
            number_of_claims_past_years=fpq1_contract.insuree.number_of_claims_past_years,
        )

        a_insuree_name = "A Name"
        a_insuree_birth_date = "2020-01-01"

        expected = (
            "Article 6. DÉCLARATIONS IMPORTANTES POUR L'ANALYSE DU RISQUE\n"
            f"\t Conducteur principal : {a_insuree_name} Date de naissance : {a_insuree_birth_date}\n"
            "\t Aucune révocation ou suspension de permis n'ont été déclarées au cours des trois dernières années\n"
            "\t Aucun sinistre, aucune réclamation n'a été déclaré au cours des cinq dernières années\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractInsureeWithASuspensionButNoClaims_whenGenerateItem6Text_thenReturnProperFRText(self):
        a_suspension = True
        a_number_of_claims_past_years = 0
        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=a_suspension,
            number_of_claims_past_years=a_number_of_claims_past_years,
            association_rebate=self.a_association_rebate,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_6_text(
            insuree_name=fpq1_contract.insuree.name,
            insuree_birth_date=fpq1_contract.insuree.date_of_birth,
            has_suspension=fpq1_contract.insuree.suspension,
            number_of_claims_past_years=fpq1_contract.insuree.number_of_claims_past_years,
        )

        a_insuree_name = "A Name"
        a_insuree_birth_date = "2020-01-01"

        expected = (
            "Article 6. DÉCLARATIONS IMPORTANTES POUR L'ANALYSE DU RISQUE\n"
            f"\t Conducteur principal : {a_insuree_name} Date de naissance : {a_insuree_birth_date}\n"
            "\t Au moins une révocation ou suspension de permis a été déclarée au cours des trois dernières années\n"
            "\t Aucun sinistre, aucune réclamation n'a été déclaré au cours des cinq dernières années\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractInsureeWithoutASuspensionButWithClaims_whenGenerateItem6Text_thenReturnProperFRText(self):
        a_suspension = False
        a_number_of_claims_past_years = 2
        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=a_suspension,
            number_of_claims_past_years=a_number_of_claims_past_years,
            association_rebate=self.a_association_rebate,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_6_text(
            insuree_name=fpq1_contract.insuree.name,
            insuree_birth_date=fpq1_contract.insuree.date_of_birth,
            has_suspension=fpq1_contract.insuree.suspension,
            number_of_claims_past_years=fpq1_contract.insuree.number_of_claims_past_years,
        )

        a_insuree_name = "A Name"
        a_insuree_birth_date = "2020-01-01"

        expected = (
            "Article 6. DÉCLARATIONS IMPORTANTES POUR L'ANALYSE DU RISQUE\n"
            f"\t Conducteur principal : {a_insuree_name} Date de naissance : {a_insuree_birth_date}\n"
            "\t Aucune révocation ou suspension de permis n'ont été déclarées au cours des trois dernières années\n"
            "\t 2 sinistre(s) ou réclamation(s) ont été déclarés au cours des cinq dernières années\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractInsureeWithASuspensionAndClaims_whenGenerateItem6Text_thenReturnProperFRText(self):
        a_suspension = True
        a_number_of_claims_past_years = 2
        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=a_suspension,
            number_of_claims_past_years=a_number_of_claims_past_years,
            association_rebate=self.a_association_rebate,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_6_text(
            insuree_name=fpq1_contract.insuree.name,
            insuree_birth_date=fpq1_contract.insuree.date_of_birth,
            has_suspension=fpq1_contract.insuree.suspension,
            number_of_claims_past_years=fpq1_contract.insuree.number_of_claims_past_years,
        )

        a_insuree_name = "A Name"
        a_insuree_birth_date = "2020-01-01"

        expected = (
            "Article 6. DÉCLARATIONS IMPORTANTES POUR L'ANALYSE DU RISQUE\n"
            f"\t Conducteur principal : {a_insuree_name} Date de naissance : {a_insuree_birth_date}\n"
            "\t Au moins une révocation ou suspension de permis a été déclarée au cours des trois dernières années\n"
            "\t 2 sinistre(s) ou réclamation(s) ont été déclarés au cours des cinq dernières années\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractInsureeNoSuspensionOrClaims_whenGenerateItem6Text_thenReturnProperENText(self):
        a_suspension = False
        a_number_of_claims_past_years = 0
        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=a_suspension,
            number_of_claims_past_years=a_number_of_claims_past_years,
            association_rebate=self.a_association_rebate,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_6_text(
            insuree_name=fpq1_contract.insuree.name,
            insuree_birth_date=fpq1_contract.insuree.date_of_birth,
            has_suspension=fpq1_contract.insuree.suspension,
            number_of_claims_past_years=fpq1_contract.insuree.number_of_claims_past_years,
        )

        a_insuree_name = "A Name"
        a_insuree_birth_date = "2020-01-01"

        expected = (
            "Item 6. IMPORTANT STATEMENTS FOR ANALYZING THE RISK\n"
            f"\t Main driver: {a_insuree_name} Date of birth: {a_insuree_birth_date}\n"
            "\t No revocation or suspension of licence has been reported over the past three years\n"
            "\t No loss or claim has been reported over the past five years\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractInsureeWithASuspensionButNoClaims_whenGenerateItem6Text_thenReturnProperENText(self):
        a_suspension = True
        a_number_of_claims_past_years = 0
        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=a_suspension,
            number_of_claims_past_years=a_number_of_claims_past_years,
            association_rebate=self.a_association_rebate,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_6_text(
            insuree_name=fpq1_contract.insuree.name,
            insuree_birth_date=fpq1_contract.insuree.date_of_birth,
            has_suspension=fpq1_contract.insuree.suspension,
            number_of_claims_past_years=fpq1_contract.insuree.number_of_claims_past_years,
        )

        a_insuree_name = "A Name"
        a_insuree_birth_date = "2020-01-01"

        expected = (
            "Item 6. IMPORTANT STATEMENTS FOR ANALYZING THE RISK\n"
            f"\t Main driver: {a_insuree_name} Date of birth: {a_insuree_birth_date}\n"
            "\t At least one revocation or suspension of licence has been reported over the past three years\n"
            "\t No loss or claim has been reported over the past five years\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractInsureeWithoutASuspensionButWithClaims_whenGenerateItem6Text_thenReturnProperENText(self):
        a_suspension = False
        a_number_of_claims_past_years = 2
        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=a_suspension,
            number_of_claims_past_years=a_number_of_claims_past_years,
            association_rebate=self.a_association_rebate,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_6_text(
            insuree_name=fpq1_contract.insuree.name,
            insuree_birth_date=fpq1_contract.insuree.date_of_birth,
            has_suspension=fpq1_contract.insuree.suspension,
            number_of_claims_past_years=fpq1_contract.insuree.number_of_claims_past_years,
        )

        a_insuree_name = "A Name"
        a_insuree_birth_date = "2020-01-01"

        expected = (
            "Item 6. IMPORTANT STATEMENTS FOR ANALYZING THE RISK\n"
            f"\t Main driver: {a_insuree_name} Date of birth: {a_insuree_birth_date}\n"
            "\t No revocation or suspension of licence has been reported over the past three years\n"
            "\t 2 loss or claim has been reported over the past five years\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractInsureeWithASuspensionAndClaims_whenGenerateItem6Text_thenReturnProperENText(self):
        a_suspension = True
        a_number_of_claims_past_years = 2
        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=a_suspension,
            number_of_claims_past_years=a_number_of_claims_past_years,
            association_rebate=self.a_association_rebate,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_6_text(
            insuree_name=fpq1_contract.insuree.name,
            insuree_birth_date=fpq1_contract.insuree.date_of_birth,
            has_suspension=fpq1_contract.insuree.suspension,
            number_of_claims_past_years=fpq1_contract.insuree.number_of_claims_past_years,
        )

        a_insuree_name = "A Name"
        a_insuree_birth_date = "2020-01-01"

        expected = (
            "Item 6. IMPORTANT STATEMENTS FOR ANALYZING THE RISK\n"
            f"\t Main driver: {a_insuree_name} Date of birth: {a_insuree_birth_date}\n"
            "\t At least one revocation or suspension of licence has been reported over the past three years\n"
            "\t 2 loss or claim has been reported over the past five years\n"
        )

        self.assertEqual(expected, actual)
