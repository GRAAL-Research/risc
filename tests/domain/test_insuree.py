from unittest import TestCase

import datetime

from risc_generator import Insuree


class InsureeTest(TestCase):
    def setUp(self) -> None:
        self.a_sex = "male"
        self.a_name = "name"
        self.a_date_of_birth = datetime.date(year=2020, month=1, day=1)
        self.an_address = "an address"

    def test_givenNoClaimsNoSuspension_whenCanHaveFAQ41_thenReturnTrue(self):
        insured = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=False,
            number_of_claims_past_years=0,
            association_rebate=True,
        )

        self.assertTrue(insured.can_have_faq_41())

    def test_givenAClaimsNoSuspension_whenCanHaveFAQ41_thenReturnFalse(self):
        insured = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=False,
            number_of_claims_past_years=1,
            association_rebate=True,
        )

        self.assertFalse(insured.can_have_faq_41())

    def test_givenNoClaimsASuspension_whenCanHaveFAQ41_thenReturnFalse(self):
        insured = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=True,
            number_of_claims_past_years=0,
            association_rebate=True,
        )

        self.assertFalse(insured.can_have_faq_41())

    def test_givenAClaimsASuspension_whenCanHaveFAQ41_thenReturnFalse(self):
        insured = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=True,
            number_of_claims_past_years=1,
            association_rebate=True,
        )

        self.assertFalse(insured.can_have_faq_41())
