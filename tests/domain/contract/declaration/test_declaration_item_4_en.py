# pylint: disable=too-many-locals

from risc_generator import Protections, FPQ1Contract, Premium
from risc_generator.content import en
from tests.domain.contract.contract_base import ContractTestBase

INCLUDE = "include"
EXCLUDE = "exclude"


class ContractDeclarationTest(ContractTestBase):
    def test_givenAENContractLiabilityOnly_whenGenerateItem4Text_thenReturnProperENText(self):
        a_liability_coverage_premium = 1
        protection_premiums = {"LiabilityCoveragePremium": a_liability_coverage_premium}
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": EXCLUDE,
            "PropertyDamageB2Coverage": EXCLUDE,
            "PropertyDamageB3Coverage": EXCLUDE,
            "PropertyDamageB4Coverage": EXCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDELITY"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Item 4. COVERAGE / PERILS: The perils covered by the insurance contract are those for which an amount "
            "of insurance, a deductible or an insurance premium is shown in the table below. Coverage is subject to "
            "the conditions set out in the insurance contract.\n"
            "PREMIUM\n"
            "\t Section A - CIVIL LIABILITY -\n"
            f"Property damage or bodily injury to another person - Amount of insurance: 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Section B - DAMAGE TO INSURED VEHICLES\n"
            "Protection 1: All risks Excluded\n"
            "Protection 2: Risk of collision and rollover Excluded\n"
            "Protection 3: All risks except collision or rollover Excluded\n"
            "Protection 4: Specific risks Excluded\n"
            f"{a_new_page}\n"
            f"\t {fidelity_program_name} program\n"
            f"Q.E.F. N 41\n"
            f"- Change to deductibles (Section B): Included\n"
            f"This endorsement makes the following changes to the deductible amounts under Section B\n"
            f"\t - No deductible to pay in the case of a hit-and-run offence if a police report was issued.\n"
            f"\t - No deductible to pay in the case of a total loss.\n"
            f"\t - No deductible to pay in the case of a windshield repair except in the case of a windshield "
            f"replacement.\n "
            f"\t - Should you incur a loss that affects two or more insurance products insured at "
            f"{a_insurer_name}, you will have but one deductible to pay, the highest applicable.\n"
            "Premium due date: according to the agreed terms of payment\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractLiabilityWithB1_whenGenerateItem4Text_thenReturnProperENText(self):
        a_liability_coverage_premium = 1
        a_b1_premium = 2
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB1CoveragePremium": a_b1_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": 250,
            "PropertyDamageB2Coverage": EXCLUDE,
            "PropertyDamageB3Coverage": EXCLUDE,
            "PropertyDamageB4Coverage": EXCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDELITY"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Item 4. COVERAGE / PERILS: The perils covered by the insurance contract are those for which an amount "
            "of insurance, a deductible or an insurance premium is shown in the table below. Coverage is subject to "
            "the conditions set out in the insurance contract.\n"
            "PREMIUM\n"
            "\t Section A - CIVIL LIABILITY -\n"
            f"Property damage or bodily injury to another person - Amount of insurance: 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Section B - DAMAGE TO INSURED VEHICLES\n"
            "Protection 1: All risks - Deductible 250$ per claim 2$\n"
            "Protection 2: Risk of collision and rollover Excluded\n"
            "Protection 3: All risks except collision or rollover Excluded\n"
            "Protection 4: Specific risks Excluded\n"
            f"{a_new_page}\n"
            f"\t {fidelity_program_name} program\n"
            f"Q.E.F. N 41\n"
            f"- Change to deductibles (Section B): Included\n"
            f"This endorsement makes the following changes to the deductible amounts under Section B\n"
            f"\t - No deductible to pay in the case of a hit-and-run offence if a police report was issued.\n"
            f"\t - No deductible to pay in the case of a total loss.\n"
            f"\t - No deductible to pay in the case of a windshield repair except in the case of a windshield "
            f"replacement.\n "
            f"\t - Should you incur a loss that affects two or more insurance products insured at "
            f"{a_insurer_name}, you will have but one deductible to pay, the highest applicable.\n"
            "Premium due date: according to the agreed terms of payment\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractLiabilityWithB2B3_whenGenerateItem4Text_thenReturnProperENText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDELITY"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Item 4. COVERAGE / PERILS: The perils covered by the insurance contract are those for which an amount "
            "of insurance, a deductible or an insurance premium is shown in the table below. Coverage is subject to "
            "the conditions set out in the insurance contract.\n"
            "PREMIUM\n"
            "\t Section A - CIVIL LIABILITY -\n"
            f"Property damage or bodily injury to another person - Amount of insurance: 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Section B - DAMAGE TO INSURED VEHICLES\n"
            "Protection 1: All risks Included\n"
            "Protection 2: Risk of collision and rollover - Deductible 250$ per claim 2$\n"
            "Protection 3: All risks except collision or rollover - Deductible 250$ per claim 3$\n"
            "Protection 4: Specific risks Excluded\n"
            f"{a_new_page}\n"
            f"\t {fidelity_program_name} program\n"
            f"Q.E.F. N 41\n"
            f"- Change to deductibles (Section B): Included\n"
            f"This endorsement makes the following changes to the deductible amounts under Section B\n"
            f"\t - No deductible to pay in the case of a hit-and-run offence if a police report was issued.\n"
            f"\t - No deductible to pay in the case of a total loss.\n"
            f"\t - No deductible to pay in the case of a windshield repair except in the case of a windshield "
            f"replacement.\n "
            f"\t - Should you incur a loss that affects two or more insurance products insured at "
            f"{a_insurer_name}, you will have but one deductible to pay, the highest applicable.\n"
            "Premium due date: according to the agreed terms of payment\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractLiabilityWithB2B4_whenGenerateItem4Text_thenReturnProperENText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b4_premium = 3
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB4CoveragePremium": a_b4_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": EXCLUDE,
            "PropertyDamageB4Coverage": 250,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDELITY"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Item 4. COVERAGE / PERILS: The perils covered by the insurance contract are those for which an amount "
            "of insurance, a deductible or an insurance premium is shown in the table below. Coverage is subject to "
            "the conditions set out in the insurance contract.\n"
            "PREMIUM\n"
            "\t Section A - CIVIL LIABILITY -\n"
            f"Property damage or bodily injury to another person - Amount of insurance: 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Section B - DAMAGE TO INSURED VEHICLES\n"
            "Protection 1: All risks Included\n"
            "Protection 2: Risk of collision and rollover - Deductible 250$ per claim 2$\n"
            "Protection 3: All risks except collision or rollover Excluded\n"
            "Protection 4: Specific risks - Deductible 250$ per claim 3$\n"
            f"{a_new_page}\n"
            f"\t {fidelity_program_name} program\n"
            f"Q.E.F. N 41\n"
            f"- Change to deductibles (Section B): Included\n"
            f"This endorsement makes the following changes to the deductible amounts under Section B\n"
            f"\t - No deductible to pay in the case of a hit-and-run offence if a police report was issued.\n"
            f"\t - No deductible to pay in the case of a total loss.\n"
            f"\t - No deductible to pay in the case of a windshield repair except in the case of a windshield "
            f"replacement.\n "
            f"\t - Should you incur a loss that affects two or more insurance products insured at "
            f"{a_insurer_name}, you will have but one deductible to pay, the highest applicable.\n"
            "Premium due date: according to the agreed terms of payment\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractWithEndorsementFAQ33_whenGenerateItem4Text_thenReturnProperENText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ33CoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ33Coverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDELITY"
        a_new_page = "<###NEW_PAGE###>"
        a_roadside_program_name = "ABC"

        expected = (
            "Item 4. COVERAGE / PERILS: The perils covered by the insurance contract are those for which an amount "
            "of insurance, a deductible or an insurance premium is shown in the table below. Coverage is subject to "
            "the conditions set out in the insurance contract.\n"
            "PREMIUM\n"
            "\t Section A - CIVIL LIABILITY -\n"
            f"Property damage or bodily injury to another person - Amount of insurance: 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Section B - DAMAGE TO INSURED VEHICLES\n"
            "Protection 1: All risks Included\n"
            "Protection 2: Risk of collision and rollover - Deductible 250$ per claim 2$\n"
            "Protection 3: All risks except collision or rollover - Deductible 250$ per claim 3$\n"
            "Protection 4: Specific risks Excluded\n"
            f"{a_new_page}\n"
            "Endorsement(s): Q.E.F. N 33 - Insurance for roadside assistance expenses\n"
            f"{a_roadside_program_name} Roadside Assistance Program, available 24 hours a day, 7 days a week\n"
            "Maximum radius 50 km -\n"
            f"In the event of a breakdown, the towing distance is increased to 100 km in the Laurentian Park, "
            "150 km in La Vérendrye Park and 100 km in Gaspésie National Park\n"
            f"Maximum number of events per insurance year 4 4$\n"
            "Limit per breakdown service 60$(1) - For a towing or a stuck vehicle, this limit is increased to 100$(1)\n"
            "Limit per policy year 400$(1)\n"
            "(1) These limits apply only when, on an exceptional basis, towing or breakdown service is not available "
            "through the Roadside Assistance Program\n"
            "See your brochure for all additional services available to you\n"
            f"\t {fidelity_program_name} program\n"
            f"Q.E.F. N 41\n"
            f"- Change to deductibles (Section B): Included\n"
            f"This endorsement makes the following changes to the deductible amounts under Section B\n"
            f"\t - No deductible to pay in the case of a hit-and-run offence if a police report was issued.\n"
            f"\t - No deductible to pay in the case of a total loss.\n"
            f"\t - No deductible to pay in the case of a windshield repair except in the case of a windshield "
            f"replacement.\n "
            f"\t - Should you incur a loss that affects two or more insurance products insured at "
            f"{a_insurer_name}, you will have but one deductible to pay, the highest applicable.\n"
            "Premium due date: according to the agreed terms of payment\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractWithEndorsementFAQ20A_whenGenerateItem4Text_thenReturnProperENText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ20ACoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ20ACoverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDELITY"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Item 4. COVERAGE / PERILS: The perils covered by the insurance contract are those for which an amount "
            "of insurance, a deductible or an insurance premium is shown in the table below. Coverage is subject to "
            "the conditions set out in the insurance contract.\n"
            "PREMIUM\n"
            "\t Section A - CIVIL LIABILITY -\n"
            f"Property damage or bodily injury to another person - Amount of insurance: 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Section B - DAMAGE TO INSURED VEHICLES\n"
            "Protection 1: All risks Included\n"
            "Protection 2: Risk of collision and rollover - Deductible 250$ per claim 2$\n"
            "Protection 3: All risks except collision or rollover - Deductible 250$ per claim 3$\n"
            "Protection 4: Specific risks Excluded\n"
            f"{a_new_page}\n"
            "Endorsement(s): Q.E.F. N 20a - Travel Expense (Extended Form) (Chapter B) 4$\n"
            "Travel expenses 50$ per day, total limit of 1500$ per claim\n"
            "Other covered expenses during a trip - 750$\n"
            f"\t {fidelity_program_name} program\n"
            f"Q.E.F. N 41\n"
            f"- Change to deductibles (Section B): Included\n"
            f"This endorsement makes the following changes to the deductible amounts under Section B\n"
            f"\t - No deductible to pay in the case of a hit-and-run offence if a police report was issued.\n"
            f"\t - No deductible to pay in the case of a total loss.\n"
            f"\t - No deductible to pay in the case of a windshield repair except in the case of a windshield "
            f"replacement.\n "
            f"\t - Should you incur a loss that affects two or more insurance products insured at "
            f"{a_insurer_name}, you will have but one deductible to pay, the highest applicable.\n"
            "Premium due date: according to the agreed terms of payment\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractWithEndorsementFAQ20_whenGenerateItem4Text_thenReturnProperENText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ20CoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ20Coverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDELITY"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Item 4. COVERAGE / PERILS: The perils covered by the insurance contract are those for which an amount "
            "of insurance, a deductible or an insurance premium is shown in the table below. Coverage is subject to "
            "the conditions set out in the insurance contract.\n"
            "PREMIUM\n"
            "\t Section A - CIVIL LIABILITY -\n"
            f"Property damage or bodily injury to another person - Amount of insurance: 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Section B - DAMAGE TO INSURED VEHICLES\n"
            "Protection 1: All risks Included\n"
            "Protection 2: Risk of collision and rollover - Deductible 250$ per claim 2$\n"
            "Protection 3: All risks except collision or rollover - Deductible 250$ per claim 3$\n"
            "Protection 4: Specific risks Excluded\n"
            f"{a_new_page}\n"
            "Endorsement(s): Q.E.F. N 20 - Travel Expense (Extended Form) (Chapter B) 4$\n"
            "Travel expenses 50$ per day, total limit of 1500$ per claim\n"
            "Other covered expenses during a trip - 750$\n"
            f"\t {fidelity_program_name} program\n"
            f"Q.E.F. N 41\n"
            f"- Change to deductibles (Section B): Included\n"
            f"This endorsement makes the following changes to the deductible amounts under Section B\n"
            f"\t - No deductible to pay in the case of a hit-and-run offence if a police report was issued.\n"
            f"\t - No deductible to pay in the case of a total loss.\n"
            f"\t - No deductible to pay in the case of a windshield repair except in the case of a windshield "
            f"replacement.\n "
            f"\t - Should you incur a loss that affects two or more insurance products insured at "
            f"{a_insurer_name}, you will have but one deductible to pay, the highest applicable.\n"
            "Premium due date: according to the agreed terms of payment\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractWithEndorsementFAQ34_whenGenerateItem4Text_thenReturnProperENText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ34CoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ34Coverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDELITY"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Item 4. COVERAGE / PERILS: The perils covered by the insurance contract are those for which an amount "
            "of insurance, a deductible or an insurance premium is shown in the table below. Coverage is subject to "
            "the conditions set out in the insurance contract.\n"
            "PREMIUM\n"
            "\t Section A - CIVIL LIABILITY -\n"
            f"Property damage or bodily injury to another person - Amount of insurance: 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Section B - DAMAGE TO INSURED VEHICLES\n"
            "Protection 1: All risks Included\n"
            "Protection 2: Risk of collision and rollover - Deductible 250$ per claim 2$\n"
            "Protection 3: All risks except collision or rollover - Deductible 250$ per claim 3$\n"
            "Protection 4: Specific risks Excluded\n"
            f"{a_new_page}\n"
            "Endorsement(s): Q.E.F. N 34 - Accident benefits insurance: 4$\n"
            "Division 1: Subdivision A and B - Death and dismemberment benefits: 20000$ principal sum\n"
            "Subdivision C - Reimbursement of medical expenses: 2000$ per person\n"
            "Division 2: Total disability benefits: Not covered\n"
            f"\t {fidelity_program_name} program\n"
            f"Q.E.F. N 41\n"
            f"- Change to deductibles (Section B): Included\n"
            f"This endorsement makes the following changes to the deductible amounts under Section B\n"
            f"\t - No deductible to pay in the case of a hit-and-run offence if a police report was issued.\n"
            f"\t - No deductible to pay in the case of a total loss.\n"
            f"\t - No deductible to pay in the case of a windshield repair except in the case of a windshield "
            f"replacement.\n "
            f"\t - Should you incur a loss that affects two or more insurance products insured at "
            f"{a_insurer_name}, you will have but one deductible to pay, the highest applicable.\n"
            "Premium due date: according to the agreed terms of payment\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractWithEndorsementFAQ34AB_whenGenerateItem4Text_thenReturnProperENText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ34ABCoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ34ABCoverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDELITY"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Item 4. COVERAGE / PERILS: The perils covered by the insurance contract are those for which an amount "
            "of insurance, a deductible or an insurance premium is shown in the table below. Coverage is subject to "
            "the conditions set out in the insurance contract.\n"
            "PREMIUM\n"
            "\t Section A - CIVIL LIABILITY -\n"
            f"Property damage or bodily injury to another person - Amount of insurance: 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Section B - DAMAGE TO INSURED VEHICLES\n"
            "Protection 1: All risks Included\n"
            "Protection 2: Risk of collision and rollover - Deductible 250$ per claim 2$\n"
            "Protection 3: All risks except collision or rollover - Deductible 250$ per claim 3$\n"
            "Protection 4: Specific risks Excluded\n"
            f"{a_new_page}\n"
            "Endorsement(s): Q.E.F. N 34ab - Accident benefits insurance: 4$\n"
            "Division 1: Subdivision A and B - Death and dismemberment benefits: 20000$ principal sum\n"
            "Subdivision C - Reimbursement of medical expenses: 2000$ per person\n"
            "Division 2: Total disability benefits: Not covered\n"
            f"\t {fidelity_program_name} program\n"
            f"Q.E.F. N 41\n"
            f"- Change to deductibles (Section B): Included\n"
            f"This endorsement makes the following changes to the deductible amounts under Section B\n"
            f"\t - No deductible to pay in the case of a hit-and-run offence if a police report was issued.\n"
            f"\t - No deductible to pay in the case of a total loss.\n"
            f"\t - No deductible to pay in the case of a windshield repair except in the case of a windshield "
            f"replacement.\n "
            f"\t - Should you incur a loss that affects two or more insurance products insured at "
            f"{a_insurer_name}, you will have but one deductible to pay, the highest applicable.\n"
            "Premium due date: according to the agreed terms of payment\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractWithEndorsementFAQ43_whenGenerateItem4Text_thenReturnProperENText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ43CoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ43Coverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDELITY"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Item 4. COVERAGE / PERILS: The perils covered by the insurance contract are those for which an amount "
            "of insurance, a deductible or an insurance premium is shown in the table below. Coverage is subject to "
            "the conditions set out in the insurance contract.\n"
            "PREMIUM\n"
            "\t Section A - CIVIL LIABILITY -\n"
            f"Property damage or bodily injury to another person - Amount of insurance: 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Section B - DAMAGE TO INSURED VEHICLES\n"
            "Protection 1: All risks Included\n"
            "Protection 2: Risk of collision and rollover - Deductible 250$ per claim 2$\n"
            "Protection 3: All risks except collision or rollover - Deductible 250$ per claim 3$\n"
            "Protection 4: Specific risks Excluded\n"
            f"{a_new_page}\n"
            "Endorsement(s): Q.E.F. N 43a - Change to indemnity (Section B) - Partial loss - New parts 1$\n"
            "Q.E.F. N 43e - Change to indemnity (Section B) - Total loss - Replacement cost 3$\n"
            f"\t {fidelity_program_name} program\n"
            f"Q.E.F. N 41\n"
            f"- Change to deductibles (Section B): Included\n"
            f"This endorsement makes the following changes to the deductible amounts under Section B\n"
            f"\t - No deductible to pay in the case of a hit-and-run offence if a police report was issued.\n"
            f"\t - No deductible to pay in the case of a total loss.\n"
            f"\t - No deductible to pay in the case of a windshield repair except in the case of a windshield "
            f"replacement.\n "
            f"\t - Should you incur a loss that affects two or more insurance products insured at "
            f"{a_insurer_name}, you will have but one deductible to pay, the highest applicable.\n"
            "Premium due date: according to the agreed terms of payment\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractWithEndorsementFAQ2_whenGenerateItem4Text_thenReturnProperENText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ2CoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ2Coverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDELITY"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Item 4. COVERAGE / PERILS: The perils covered by the insurance contract are those for which an amount "
            "of insurance, a deductible or an insurance premium is shown in the table below. Coverage is subject to "
            "the conditions set out in the insurance contract.\n"
            "PREMIUM\n"
            "\t Section A - CIVIL LIABILITY -\n"
            f"Property damage or bodily injury to another person - Amount of insurance: 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Section B - DAMAGE TO INSURED VEHICLES\n"
            "Protection 1: All risks Included\n"
            "Protection 2: Risk of collision and rollover - Deductible 250$ per claim 2$\n"
            "Protection 3: All risks except collision or rollover - Deductible 250$ per claim 3$\n"
            "Protection 4: Specific risks Excluded\n"
            f"{a_new_page}\n"
            "Endorsement(s): Q.E.F. N 2 - Vehicles of which named insured is not owner and when driven by named "
            "drivers (Section A) Included\n"
            f"\t {fidelity_program_name} program\n"
            f"Q.E.F. N 41\n"
            f"- Change to deductibles (Section B): Included\n"
            f"This endorsement makes the following changes to the deductible amounts under Section B\n"
            f"\t - No deductible to pay in the case of a hit-and-run offence if a police report was issued.\n"
            f"\t - No deductible to pay in the case of a total loss.\n"
            f"\t - No deductible to pay in the case of a windshield repair except in the case of a windshield "
            f"replacement.\n "
            f"\t - Should you incur a loss that affects two or more insurance products insured at "
            f"{a_insurer_name}, you will have but one deductible to pay, the highest applicable.\n"
            "Premium due date: according to the agreed terms of payment\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractWithEndorsementFAQ5A_whenGenerateItem4Text_thenReturnProperENText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ5ACoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ5ACoverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDELITY"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Item 4. COVERAGE / PERILS: The perils covered by the insurance contract are those for which an amount "
            "of insurance, a deductible or an insurance premium is shown in the table below. Coverage is subject to "
            "the conditions set out in the insurance contract.\n"
            "PREMIUM\n"
            "\t Section A - CIVIL LIABILITY -\n"
            f"Property damage or bodily injury to another person - Amount of insurance: 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Section B - DAMAGE TO INSURED VEHICLES\n"
            "Protection 1: All risks Included\n"
            "Protection 2: Risk of collision and rollover - Deductible 250$ per claim 2$\n"
            "Protection 3: All risks except collision or rollover - Deductible 250$ per claim 3$\n"
            "Protection 4: Specific risks Excluded\n"
            f"{a_new_page}\n"
            "Endorsement(s): Q.E.F. N 5a - Vehicles leased or under a contract of leasing Included\n"
            f"\t {fidelity_program_name} program\n"
            f"Q.E.F. N 41\n"
            f"- Change to deductibles (Section B): Included\n"
            f"This endorsement makes the following changes to the deductible amounts under Section B\n"
            f"\t - No deductible to pay in the case of a hit-and-run offence if a police report was issued.\n"
            f"\t - No deductible to pay in the case of a total loss.\n"
            f"\t - No deductible to pay in the case of a windshield repair except in the case of a windshield "
            f"replacement.\n "
            f"\t - Should you incur a loss that affects two or more insurance products insured at "
            f"{a_insurer_name}, you will have but one deductible to pay, the highest applicable.\n"
            "Premium due date: according to the agreed terms of payment\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractWithEndorsementFAQ23A_whenGenerateItem4Text_thenReturnProperENText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ23ACoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ23ACoverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDELITY"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Item 4. COVERAGE / PERILS: The perils covered by the insurance contract are those for which an amount "
            "of insurance, a deductible or an insurance premium is shown in the table below. Coverage is subject to "
            "the conditions set out in the insurance contract.\n"
            "PREMIUM\n"
            "\t Section A - CIVIL LIABILITY -\n"
            f"Property damage or bodily injury to another person - Amount of insurance: 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Section B - DAMAGE TO INSURED VEHICLES\n"
            "Protection 1: All risks Included\n"
            "Protection 2: Risk of collision and rollover - Deductible 250$ per claim 2$\n"
            "Protection 3: All risks except collision or rollover - Deductible 250$ per claim 3$\n"
            "Protection 4: Specific risks Excluded\n"
            f"{a_new_page}\n"
            "Endorsement(s): Q.E.F. N 23a - Vehicles under financing Included\n"
            f"\t {fidelity_program_name} program\n"
            f"Q.E.F. N 41\n"
            f"- Change to deductibles (Section B): Included\n"
            f"This endorsement makes the following changes to the deductible amounts under Section B\n"
            f"\t - No deductible to pay in the case of a hit-and-run offence if a police report was issued.\n"
            f"\t - No deductible to pay in the case of a total loss.\n"
            f"\t - No deductible to pay in the case of a windshield repair except in the case of a windshield "
            f"replacement.\n "
            f"\t - Should you incur a loss that affects two or more insurance products insured at "
            f"{a_insurer_name}, you will have but one deductible to pay, the highest applicable.\n"
            "Premium due date: according to the agreed terms of payment\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractWithEndorsementFAQ27_whenGenerateItem4Text_thenReturnProperENText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ27CoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ27Coverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDELITY"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Item 4. COVERAGE / PERILS: The perils covered by the insurance contract are those for which an amount "
            "of insurance, a deductible or an insurance premium is shown in the table below. Coverage is subject to "
            "the conditions set out in the insurance contract.\n"
            "PREMIUM\n"
            "\t Section A - CIVIL LIABILITY -\n"
            f"Property damage or bodily injury to another person - Amount of insurance: 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Section B - DAMAGE TO INSURED VEHICLES\n"
            "Protection 1: All risks Included\n"
            "Protection 2: Risk of collision and rollover - Deductible 250$ per claim 2$\n"
            "Protection 3: All risks except collision or rollover - Deductible 250$ per claim 3$\n"
            "Protection 4: Specific risks Excluded\n"
            f"{a_new_page}\n"
            "Endorsement(s): Q.E.F. N 27 - Civil liability resulting from damage caused to vehicles of "
            "which named insured is not owner (including vehicles provided by an employer) (Section A) - 75000$\n"
            "Vehicles included under described vehicles, trailers or utility trailers\n"
            "Section B2 - $250 deductible and section B3 - $50 deductible\n"
            f"\t {fidelity_program_name} program\n"
            f"Q.E.F. N 41\n"
            f"- Change to deductibles (Section B): Included\n"
            f"This endorsement makes the following changes to the deductible amounts under Section B\n"
            f"\t - No deductible to pay in the case of a hit-and-run offence if a police report was issued.\n"
            f"\t - No deductible to pay in the case of a total loss.\n"
            f"\t - No deductible to pay in the case of a windshield repair except in the case of a windshield "
            f"replacement.\n "
            f"\t - Should you incur a loss that affects two or more insurance products insured at "
            f"{a_insurer_name}, you will have but one deductible to pay, the highest applicable.\n"
            "Premium due date: according to the agreed terms of payment\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractWithEndorsementFAQ27a_whenGenerateItem4Text_thenReturnProperENText(self):
        a_liability_coverage_premium = 1
        a_b2_premium = 2
        a_b3_premium = 3
        a_faq_premium = 4
        protection_premiums = {
            "LiabilityCoveragePremium": a_liability_coverage_premium,
            "PropertyDamageB2CoveragePremium": a_b2_premium,
            "PropertyDamageB3CoveragePremium": a_b3_premium,
            "FAQ27ACoveragePremium": a_faq_premium,
        }
        a_premium = Premium(**protection_premiums)

        a_dict_of_protections = {
            "LiabilityCoverage": 1000000,
            "PropertyDamageB1Coverage": INCLUDE,
            "PropertyDamageB2Coverage": 250,
            "PropertyDamageB3Coverage": 250,
            "PropertyDamageB4Coverage": EXCLUDE,
            "FAQ27ACoverage": INCLUDE,
        }
        a_protections = Protections(protections=a_dict_of_protections)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_4_text(
            protections=fpq1_contract.protections, premium=fpq1_contract.premium
        )

        a_insurer_name = "Assureur"
        fidelity_program_name = "FIDELITY"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "Item 4. COVERAGE / PERILS: The perils covered by the insurance contract are those for which an amount "
            "of insurance, a deductible or an insurance premium is shown in the table below. Coverage is subject to "
            "the conditions set out in the insurance contract.\n"
            "PREMIUM\n"
            "\t Section A - CIVIL LIABILITY -\n"
            f"Property damage or bodily injury to another person - Amount of insurance: 1000000$ "
            f"{a_liability_coverage_premium}$\n"
            "\t Section B - DAMAGE TO INSURED VEHICLES\n"
            "Protection 1: All risks Included\n"
            "Protection 2: Risk of collision and rollover - Deductible 250$ per claim 2$\n"
            "Protection 3: All risks except collision or rollover - Deductible 250$ per claim 3$\n"
            "Protection 4: Specific risks Excluded\n"
            f"{a_new_page}\n"
            "Endorsement(s): Q.E.F. N 27a - Civil liability resulting from damage caused to vehicles of which named "
            "insured is not owner (including vehicles provided by an employer) (Section A) - 75000$\n"
            "Vehicles included under described vehicles, trailers or utility trailers\n"
            "Section B2 - $250 deductible and section B3 - $50 deductible\n"
            f"\t {fidelity_program_name} program\n"
            f"Q.E.F. N 41\n"
            f"- Change to deductibles (Section B): Included\n"
            f"This endorsement makes the following changes to the deductible amounts under Section B\n"
            f"\t - No deductible to pay in the case of a hit-and-run offence if a police report was issued.\n"
            f"\t - No deductible to pay in the case of a total loss.\n"
            f"\t - No deductible to pay in the case of a windshield repair except in the case of a windshield "
            f"replacement.\n "
            f"\t - Should you incur a loss that affects two or more insurance products insured at "
            f"{a_insurer_name}, you will have but one deductible to pay, the highest applicable.\n"
            "Premium due date: according to the agreed terms of payment\n"
        )

        self.assertEqual(expected, actual)
