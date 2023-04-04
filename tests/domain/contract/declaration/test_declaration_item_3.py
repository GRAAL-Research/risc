from risc_generator import Protections, FPQ1Contract, Premium, Vehicle
from risc_generator.content import fr, en
from tests.domain.contract.contract_base import ContractTestBase

INCLUDE = "include"
EXCLUDE = "exclude"


class ContractDeclarationTest(ContractTestBase):
    def test_givenAFRContractNewBoughtCar_whenGenerateItem3Text_thenReturnProperFRText(self):
        a_protections = Protections(protections=self.a_dict_of_protections)
        a_premium_amount = 1
        protection_premiums = {
            "LiabilityPremium": a_premium_amount,
            "PropertyDamageB2CoveragePremium": a_premium_amount,
            "PropertyDamageB3CoveragePremium": a_premium_amount,
            "FAQ20ACoveragePremium": a_premium_amount,
            "FAQ33CoveragePremium": a_premium_amount,
            "FAQ34CoveragePremium": a_premium_amount,
            "FAQ43CoveragePremium": a_premium_amount,
        }

        a_premium = Premium(**protection_premiums)

        a_vehicle = Vehicle(
            year=self.a_year,
            make=self.a_maker,
            model=self.a_model,
            vin=self.a_vin,
            purchase_condition="neuf",
            electric_vehicle=False,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_3_text(
            formatted_vehicle_complete_details=fpq1_contract.vehicle.format_vehicle_complete_details(
                with_text="Numéro de série"
            ),
            car_ownership=fpq1_contract.car_ownership(),
            vehicle_purchase_condition=fpq1_contract.vehicle.purchase_condition,
            car_with_financing=fpq1_contract.car_with_financing(),
            financing_details=fpq1_contract.financing,
        )

        an_insured_car = "AMaker - AModel - 2020 - Numéro de série 1234567890 - Achat neuf"

        expected = "Article 3. CARACTÉRISTIQUES DU VÉHICULE DÉSIGNÉ 1\n" f"{an_insured_car}\n"

        self.assertEqual(expected, actual)

    def test_givenAFRContractUsedBoughtCar_whenGenerateItem3Text_thenReturnProperFRText(self):
        a_protections = Protections(protections=self.a_dict_of_protections)
        a_premium_amount = 1
        protection_premiums = {
            "LiabilityPremium": a_premium_amount,
            "PropertyDamageB2CoveragePremium": a_premium_amount,
            "PropertyDamageB3CoveragePremium": a_premium_amount,
            "FAQ20ACoveragePremium": a_premium_amount,
            "FAQ33CoveragePremium": a_premium_amount,
            "FAQ34CoveragePremium": a_premium_amount,
            "FAQ43CoveragePremium": a_premium_amount,
        }

        a_premium = Premium(**protection_premiums)

        a_vehicle = Vehicle(
            year=self.a_year,
            make=self.a_maker,
            model=self.a_model,
            vin=self.a_vin,
            purchase_condition="usagé",
            electric_vehicle=False,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_3_text(
            formatted_vehicle_complete_details=fpq1_contract.vehicle.format_vehicle_complete_details(
                with_text="Numéro de série"
            ),
            car_ownership=fpq1_contract.car_ownership(),
            vehicle_purchase_condition=fpq1_contract.vehicle.purchase_condition,
            car_with_financing=fpq1_contract.car_with_financing(),
            financing_details=fpq1_contract.financing,
        )

        an_insured_car = "AMaker - AModel - 2020 - Numéro de série 1234567890 - Achat usagé"

        expected = "Article 3. CARACTÉRISTIQUES DU VÉHICULE DÉSIGNÉ 1\n" f"{an_insured_car}\n"

        self.assertEqual(expected, actual)

    def test_givenAFRContractNewLoanedCar_whenGenerateItem3Text_thenReturnProperFRText(self):
        a_dict_of_protections = self.a_dict_of_protections.copy()
        a_dict_of_protections.update({"FAQ5ACoverage": INCLUDE})
        a_protections = Protections(protections=a_dict_of_protections)
        a_premium_amount = 1
        protection_premiums = {
            "LiabilityPremium": a_premium_amount,
            "PropertyDamageB2CoveragePremium": a_premium_amount,
            "PropertyDamageB3CoveragePremium": a_premium_amount,
            "FAQ20ACoveragePremium": a_premium_amount,
            "FAQ33CoveragePremium": a_premium_amount,
            "FAQ34CoveragePremium": a_premium_amount,
            "FAQ43CoveragePremium": a_premium_amount,
        }

        a_premium = Premium(**protection_premiums)

        a_vehicle = Vehicle(
            year=self.a_year,
            make=self.a_maker,
            model=self.a_model,
            vin=self.a_vin,
            purchase_condition="neuf",
            electric_vehicle=False,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_3_text(
            formatted_vehicle_complete_details=fpq1_contract.vehicle.format_vehicle_complete_details(
                with_text="Numéro de série"
            ),
            car_ownership=fpq1_contract.car_ownership(),
            vehicle_purchase_condition=fpq1_contract.vehicle.purchase_condition,
            car_with_financing=fpq1_contract.car_with_financing(),
            financing_details=fpq1_contract.financing,
        )

        an_insured_car = "AMaker - AModel - 2020 - Numéro de série 1234567890 - Location neuf"
        a_creditor_details = "A Bank An Address for The Bank"

        expected = (
            "Article 3. CARACTÉRISTIQUES DU VÉHICULE DÉSIGNÉ 1\n"
            f"{an_insured_car}\n"
            "Locateur qui a droit aux indemnités du chapitre B, selon son intérêt - Sujet à l'avenant F.A.Q. N 5a\n"
            f"{a_creditor_details}\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractNewCreditorCar_whenGenerateItem3Text_thenReturnProperFRText(self):
        a_dict_of_protections = self.a_dict_of_protections.copy()
        a_dict_of_protections.update({"FAQ23ACoverage": INCLUDE})
        a_protections = Protections(protections=a_dict_of_protections)
        a_premium_amount = 1
        protection_premiums = {
            "LiabilityPremium": a_premium_amount,
            "PropertyDamageB2CoveragePremium": a_premium_amount,
            "PropertyDamageB3CoveragePremium": a_premium_amount,
            "FAQ20ACoveragePremium": a_premium_amount,
            "FAQ33CoveragePremium": a_premium_amount,
            "FAQ34CoveragePremium": a_premium_amount,
            "FAQ43CoveragePremium": a_premium_amount,
        }

        a_premium = Premium(**protection_premiums)

        a_vehicle = Vehicle(
            year=self.a_year,
            make=self.a_maker,
            model=self.a_model,
            vin=self.a_vin,
            purchase_condition="neuf",
            electric_vehicle=False,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fr.declaration_articles.generate_item_3_text(
            formatted_vehicle_complete_details=fpq1_contract.vehicle.format_vehicle_complete_details(
                with_text="Numéro de série"
            ),
            car_ownership=fpq1_contract.car_ownership(),
            vehicle_purchase_condition=fpq1_contract.vehicle.purchase_condition,
            car_with_financing=fpq1_contract.car_with_financing(),
            financing_details=fpq1_contract.financing,
        )

        an_insured_car = "AMaker - AModel - 2020 - Numéro de série 1234567890 - Achat neuf"
        a_creditor_details = "A Bank An Address for The Bank"

        expected = (
            "Article 3. CARACTÉRISTIQUES DU VÉHICULE DÉSIGNÉ 1\n"
            f"{an_insured_car}\n"
            "Créancier qui a droit aux indemnités du chapitre B, selon son intérêt - Sujet à l'avenant F.A.Q. N 23a\n"
            f"{a_creditor_details}\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractNewBoughtCar_whenGenerateItem3Text_thenReturnProperENText(self):
        a_protections = Protections(protections=self.a_dict_of_protections)
        a_premium_amount = 1
        protection_premiums = {
            "LiabilityPremium": a_premium_amount,
            "PropertyDamageB2CoveragePremium": a_premium_amount,
            "PropertyDamageB3CoveragePremium": a_premium_amount,
            "FAQ20ACoveragePremium": a_premium_amount,
            "FAQ33CoveragePremium": a_premium_amount,
            "FAQ34CoveragePremium": a_premium_amount,
            "FAQ43CoveragePremium": a_premium_amount,
        }

        a_premium = Premium(**protection_premiums)

        a_vehicle = Vehicle(
            year=self.a_year,
            make=self.a_maker,
            model=self.a_model,
            vin=self.a_vin,
            purchase_condition="new",
            electric_vehicle=False,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_3_text(
            formatted_vehicle_complete_details=fpq1_contract.vehicle.format_vehicle_complete_details(
                with_text="Serial number"
            ),
            car_ownership=fpq1_contract.car_ownership(),
            vehicle_purchase_condition=fpq1_contract.vehicle.purchase_condition,
            car_with_financing=fpq1_contract.car_with_financing(),
            financing_details=fpq1_contract.financing,
        )

        an_insured_car = "AMaker - AModel - 2020 - Serial number 1234567890 - Purchase new"

        expected = "Item 3. PARTICULARS OF THE DESCRIBED VEHICLE 1\n" f"{an_insured_car}\n"

        self.assertEqual(expected, actual)

    def test_givenAENContractUsedBoughtCar_whenGenerateItem3Text_thenReturnProperENText(self):
        a_protections = Protections(protections=self.a_dict_of_protections)
        a_premium_amount = 1
        protection_premiums = {
            "LiabilityPremium": a_premium_amount,
            "PropertyDamageB2CoveragePremium": a_premium_amount,
            "PropertyDamageB3CoveragePremium": a_premium_amount,
            "FAQ20ACoveragePremium": a_premium_amount,
            "FAQ33CoveragePremium": a_premium_amount,
            "FAQ34CoveragePremium": a_premium_amount,
            "FAQ43CoveragePremium": a_premium_amount,
        }

        a_premium = Premium(**protection_premiums)

        a_vehicle = Vehicle(
            year=self.a_year,
            make=self.a_maker,
            model=self.a_model,
            vin=self.a_vin,
            purchase_condition="used",
            electric_vehicle=False,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_3_text(
            formatted_vehicle_complete_details=fpq1_contract.vehicle.format_vehicle_complete_details(
                with_text="Serial number"
            ),
            car_ownership=fpq1_contract.car_ownership(),
            vehicle_purchase_condition=fpq1_contract.vehicle.purchase_condition,
            car_with_financing=fpq1_contract.car_with_financing(),
            financing_details=fpq1_contract.financing,
        )

        an_insured_car = "AMaker - AModel - 2020 - Serial number 1234567890 - Purchase used"

        expected = "Item 3. PARTICULARS OF THE DESCRIBED VEHICLE 1\n" f"{an_insured_car}\n"

        self.assertEqual(expected, actual)

    def test_givenAENContractNewLoanedCar_whenGenerateItem3Text_thenReturnProperENText(self):
        a_dict_of_protections = self.a_dict_of_protections.copy()
        a_dict_of_protections.update({"FAQ5ACoverage": INCLUDE})
        a_protections = Protections(protections=a_dict_of_protections)
        a_premium_amount = 1
        protection_premiums = {
            "LiabilityPremium": a_premium_amount,
            "PropertyDamageB2CoveragePremium": a_premium_amount,
            "PropertyDamageB3CoveragePremium": a_premium_amount,
            "FAQ20ACoveragePremium": a_premium_amount,
            "FAQ33CoveragePremium": a_premium_amount,
            "FAQ34CoveragePremium": a_premium_amount,
            "FAQ43CoveragePremium": a_premium_amount,
        }

        a_premium = Premium(**protection_premiums)

        a_vehicle = Vehicle(
            year=self.a_year,
            make=self.a_maker,
            model=self.a_model,
            vin=self.a_vin,
            purchase_condition="new",
            electric_vehicle=False,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_3_text(
            formatted_vehicle_complete_details=fpq1_contract.vehicle.format_vehicle_complete_details(
                with_text="Serial number"
            ),
            car_ownership=fpq1_contract.car_ownership(),
            vehicle_purchase_condition=fpq1_contract.vehicle.purchase_condition,
            car_with_financing=fpq1_contract.car_with_financing(),
            financing_details=fpq1_contract.financing,
        )

        an_insured_car = "AMaker - AModel - 2020 - Serial number 1234567890 - Rental new"
        a_creditor_details = "A Bank An Address for The Bank"

        expected = (
            "Item 3. PARTICULARS OF THE DESCRIBED VEHICLE 1\n"
            f"{an_insured_car}\n"
            "Lessor entitled to Chapter B benefits, according to his interest - Subject to the "
            "Q.E.F. endorsement N 5a\n"
            f"{a_creditor_details}\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractNewCreditorCar_whenGenerateItem3Text_thenReturnProperENText(self):
        a_dict_of_protections = self.a_dict_of_protections.copy()
        a_dict_of_protections.update({"FAQ23ACoverage": INCLUDE})
        a_protections = Protections(protections=a_dict_of_protections)
        a_premium_amount = 1
        protection_premiums = {
            "LiabilityPremium": a_premium_amount,
            "PropertyDamageB2CoveragePremium": a_premium_amount,
            "PropertyDamageB3CoveragePremium": a_premium_amount,
            "FAQ20ACoveragePremium": a_premium_amount,
            "FAQ33CoveragePremium": a_premium_amount,
            "FAQ34CoveragePremium": a_premium_amount,
            "FAQ43CoveragePremium": a_premium_amount,
        }

        a_premium = Premium(**protection_premiums)

        a_vehicle = Vehicle(
            year=self.a_year,
            make=self.a_maker,
            model=self.a_model,
            vin=self.a_vin,
            purchase_condition="new",
            electric_vehicle=False,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=a_protections,
            premium=a_premium,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = en.declaration_articles.generate_item_3_text(
            formatted_vehicle_complete_details=fpq1_contract.vehicle.format_vehicle_complete_details(
                with_text="Serial number"
            ),
            car_ownership=fpq1_contract.car_ownership(),
            vehicle_purchase_condition=fpq1_contract.vehicle.purchase_condition,
            car_with_financing=fpq1_contract.car_with_financing(),
            financing_details=fpq1_contract.financing,
        )

        an_insured_car = "AMaker - AModel - 2020 - Serial number 1234567890 - Purchase new"
        a_creditor_details = "A Bank An Address for The Bank"

        expected = (
            "Item 3. PARTICULARS OF THE DESCRIBED VEHICLE 1\n"
            f"{an_insured_car}\n"
            "Creditor entitled to Chapter B benefits, according to his interest - Subject to the "
            "Q.E.F. endorsement N 23a\n"
            f"{a_creditor_details}\n"
        )

        self.assertEqual(expected, actual)
