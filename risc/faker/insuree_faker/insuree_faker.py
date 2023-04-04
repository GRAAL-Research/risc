from faker import Faker

from ...domain.insuree import Insuree
from ...faker.insuree_faker.association_rebate_faker import (
    association_rebate_faker,
)
from ...faker.insuree_faker.claims_faker import ClaimsFaker
from ...faker.insuree_faker.driver_license_suspension_faker import (
    DriverLicenseSuspensionFaker,
)
from ...faker.insuree_faker.sex_faker import SexFaker


class InsureeFaker:
    def __init__(self, locale: str) -> None:
        """
        locale (str): The locale language setting to use for simulation. Can either be `'fr_CA'` or `'en_CA'`.
        """
        self.sex_faker = SexFaker(locale=locale)
        self.name_faker = Faker(locale=locale)
        self.date_of_birth_faker = Faker(locale=locale)
        self.address_faker = Faker(locale=locale)

        self.suspension_faker = DriverLicenseSuspensionFaker()
        self.claims_faker = ClaimsFaker()
        self.association_rebate_group_faker = association_rebate_faker

    def insuree(self) -> Insuree:
        """
        Method to fake an insuree.

        Return:
            An insuree in the locale language.
        """
        sex = self.sex_faker.gender()

        if sex == self.sex_faker.gender_1:
            # Gender 1 is either 'male' or 'homme' depending on the locale.
            name = self.name_faker.name_male()
        else:
            name = self.name_faker.name_female()

        date_of_birth = self.date_of_birth_faker.date_of_birth(minimum_age=16, maximum_age=95)

        address = self.address_faker.address()

        suspension = self.suspension_faker.suspension()

        number_of_claims_past_five_years = self.claims_faker.claims(number_of_years=5)

        association_rebate = self.association_rebate_group_faker()

        return Insuree(
            sex=sex,
            name=name,
            birth_date=date_of_birth,
            address=address,
            suspension=suspension,
            number_of_claims_past_years=number_of_claims_past_five_years,
            association_rebate=association_rebate,
        )
