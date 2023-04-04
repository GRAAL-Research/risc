import datetime


class Insuree:
    def __init__(
        self,
        sex: str,
        name: str,
        birth_date: datetime.date,
        address: str,
        suspension: bool,
        number_of_claims_past_years: int,
        association_rebate: bool,
    ) -> None:
        self.sex = sex
        self.name = name
        self.birth_date = birth_date
        self.address = address
        self.suspension = suspension
        self.number_of_claims_past_years = number_of_claims_past_years
        self.association_rebate = association_rebate

    def __str__(self) -> str:
        return f"Insured named: {self.name} born the {self.date_of_birth} and living at the address: {self.address}."

    def can_have_faq_41(self) -> bool:
        return self.number_of_claims_past_years == 0 and not self.suspension

    def insuree_is_in_a_rebate_group(self):
        return self.association_rebate

    @property
    def date_of_birth(self) -> str:
        return str(self.birth_date)
