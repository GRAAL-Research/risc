import datetime
from unittest.mock import patch

from risc_generator import Protections
from risc_generator.domain.contract import FPQ1Contract
from tests.domain.contract.contract_base import ContractTestBase

INCLUDE = "include"
EXCLUDE = "exclude"


class ContractTest(ContractTestBase):
    def setUp(self) -> None:
        self.a_protections = Protections(protections=self.a_dict_of_protections)

    @patch("risc_generator.domain.contract.Faker")
    def test_givenAFRContractWithSomeDate_whenFormattedTextDateFrLocale_thenReturnFrDate(self, faker_mock):
        a_year = 2022
        a_month = 1
        a_day = 2

        faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fpq1_contract.formatted_text_date()
        expected = "Le 2 janvier 2022"
        self.assertEqual(expected, actual)

    @patch("risc_generator.domain.contract.Faker")
    def test_givenAContractWithSomeDate_whenFormattedTextDateEnLocale_thenReturnEnDate(self, faker_mock):
        a_year = 2022
        a_month = 1
        a_day = 2

        faker_mock().date_between.return_value = datetime.date(year=a_year, month=a_month, day=a_day)

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = fpq1_contract.formatted_text_date()
        expected = f"January 2, {a_year}"
        self.assertEqual(expected, actual)

    def test_givenAContractWithSomeProtections_whenSTR_thenReturnProperString(self):
        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=self.a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_locale,
        )

        actual = str(fpq1_contract)

        expected = f"FPQ1 contract with the following protections:\n{self.a_protections}"

        self.assertEqual(expected, actual)

    def test_givenAContratWithFAQ5A_whenCarOwnership_thenReturnRentalInLocaleLang(self):
        a_dict_of_protections = self.a_dict_of_protections.copy()
        a_dict_of_protections.update({"FAQ5ACoverage": INCLUDE})
        a_protections = Protections(protections=a_dict_of_protections)

        # FR locale

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

        actual = fpq1_contract.car_ownership()

        expected = "Location"

        self.assertEqual(expected, actual)

        # EN locale
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

        actual = fpq1_contract.car_ownership()

        expected = "Rental"

        self.assertEqual(expected, actual)

    def test_givenAContratWithFAQ23A_whenCarOwnership_thenReturnPurchaseInLocaleLang(self):
        a_dict_of_protections = self.a_dict_of_protections.copy()
        a_dict_of_protections.update({"FAQ23ACoverage": INCLUDE})
        a_protections = Protections(protections=a_dict_of_protections)

        # FR locale

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

        actual = fpq1_contract.car_ownership()

        expected = "Achat"

        self.assertEqual(expected, actual)

        # EN locale
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

        actual = fpq1_contract.car_ownership()

        expected = "Purchase"

        self.assertEqual(expected, actual)

    def test_givenAContratWithoutFAQ23AOrFAQ5A_whenCarOwnership_thenReturnPurchaseInLocaleLang(self):
        a_dict_of_protections = self.a_dict_of_protections.copy()
        a_protections = Protections(protections=a_dict_of_protections)

        # FR locale

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

        actual = fpq1_contract.car_ownership()

        expected = "Achat"

        self.assertEqual(expected, actual)

        # EN locale
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

        actual = fpq1_contract.car_ownership()

        expected = "Purchase"

        self.assertEqual(expected, actual)

    def test_givenAContratWithFAQ5A_whenCarWitFinancing_thenReturnLessor(self):
        a_dict_of_protections = self.a_dict_of_protections.copy()
        a_dict_of_protections.update({"FAQ5ACoverage": INCLUDE})
        a_protections = Protections(protections=a_dict_of_protections)

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

        actual = fpq1_contract.car_with_financing()

        expected = "lessor"

        self.assertEqual(expected, actual)

    def test_givenAContratWithFAQ23A_whenCarWitFinancing_thenReturnCreditor(self):
        a_dict_of_protections = self.a_dict_of_protections.copy()
        a_dict_of_protections.update({"FAQ23ACoverage": INCLUDE})
        a_protections = Protections(protections=a_dict_of_protections)

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

        actual = fpq1_contract.car_with_financing()

        expected = "creditor"

        self.assertEqual(expected, actual)

    def test_givenAContratWithoutFAQ5AOrFAQ23A_whenCarWitFinancing_thenReturnNone(self):
        a_dict_of_protections = self.a_dict_of_protections.copy()
        a_protections = Protections(protections=a_dict_of_protections)

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

        actual = fpq1_contract.car_with_financing()

        expected = None

        self.assertEqual(expected, actual)
