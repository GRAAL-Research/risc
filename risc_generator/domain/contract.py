import inspect
import re
from datetime import date, timedelta
from types import MethodType

from babel.dates import format_date
from dateutil.relativedelta import relativedelta
from faker import Faker

from ..content import en, fr
from ..domain.insuree import Insuree
from ..domain.protections import Protections
from ..domain.vehicle import Vehicle
from .premium import Premium

_SECTION_GENERATORS = (
    "generate_header_text",
    "generate_important_instructions_text",
    "generate_declaration_text",
    "generate_cancellation_of_policy_text",
    "generate_certificates_text",
    "generate_bill_text",
    "generate_client_advantages_text",
    "generate_fpq1_text",
)

_ENDORSEMENT_GENERATORS = tuple(
    f"generate_faq{faq}_endorsement_text"
    for faq in (
        "2",
        "3",
        "5a",
        "8",
        "9",
        "13",
        "16",
        "19",
        "20",
        "20a",
        "23a",
        "25",
        "27",
        "27a",
        "28",
        "30",
        "31",
        "32",
        "33",
        "34",
        "34ab",
        "37ab",
        "40",
        "41",
        "43",
    )
)


class FPQ1Contract:
    def __init__(
        self,
        client_number: str,
        contract_start_date: date,
        insuree: Insuree,
        vehicle: Vehicle,
        payment_method: str,
        protections: Protections,
        premium: Premium,
        financing: None | str,
        locale: str,
    ):
        """
        A FPQ1 contract.

        client_number (str): A unique client number.
        start_date (datetime.date): Date the contract start (the coverage).
        header_contract_date (datetime.date): Date the contract was printed.
        insuree (Insuree): Insuree of the contract.
        vehicle (Vehicle): The vehicle details.
        payment_method (str): The type of payment method. Either 'pre-authorize' or 'bill'.
        protections (Protections): The protections.
        premium (Premium): A premium base on the protections and the insuree of the contract.
        locale (str): The locale language setting to use for simulation. Can either be `'fr_CA'` or `'en_CA'`.
        """
        self.locale = locale
        if self.locale == "fr_CA":
            self.ownership_rental = "Location"
            self.ownership_purchase = "Achat"
        else:
            self.ownership_rental = "Rental"
            self.ownership_purchase = "Purchase"

        self.client_number = client_number
        self.contract_start_date = contract_start_date

        # Date the paperwork is printed:
        # A contract cannot be legally dated more than 90 days before the start of the contract.
        # Thus, the paperwork with the contract cannot be date more than 90 days before the contract start date.
        # To do so, we cannot use self.date_faker.date_between(start_date=-90d) since it will create a start date
        # 90 days before today (the time the Python script is run) rather than 90 days before the contract start date.
        # The following code was taken from the date_between date_parsing function.
        # Namely, this code does a timedelta of minus 90 days init with a dict plus the contract_start_date.
        # Thus, it will randomly select a date of at most 90 days before the start of the contract.
        contract_paperwork_date = contract_start_date + timedelta(**{"days": -90})
        date_faker = Faker(locale=self.locale)
        header_contract_date = date_faker.date_between(start_date=contract_paperwork_date, end_date=contract_start_date)

        self.header_contract_date = header_contract_date
        self.contract_end_date = contract_start_date + relativedelta(years=1)
        self.insuree = insuree
        self.vehicle = vehicle

        self.payment_method = payment_method

        self.protections = protections

        self.premium = premium

        self.financing = financing

        self.policy = "001"  # We set it to 1 since we assume (for now) only new clients
        self.policy_number = f"{self.client_number}-{self.policy}"

        self._bind_language_text_generators()

    def formatted_text_date(self) -> str:
        """
        Method to format the date in a text format in the locale language

        Return:
            The date in a text format.
        """
        prefix = ""
        if "fr" in self.locale:
            prefix = "Le "
        return prefix + format_date(self.header_contract_date, format='long', locale=self.locale)

    def car_ownership(self) -> str:
        """
        Method to get the car ownership type (rental or purchase) in the locale language.

        Return:
            The car ownership.
        """
        if self.protections.is_protected("FAQ5ACoverage"):
            # The car is a rental one since this endorsement is use for rented car
            car_ownership = self.ownership_rental
        else:
            # The car was purchase (with or without a creditor)
            car_ownership = self.ownership_purchase
        return car_ownership

    def car_with_financing(self) -> None | str:
        """
        Method to evaluate if the car is financed with a creditor (e.g. protections include a FAQ23a coverage)
        or a lessor (e.g. protections include a FAQ5a coverage).

        Return:
            A none if no financing or a string of the financing type (e.g. `'creditor'` or `'lessor'`).
        """
        if self.protections.is_protected("FAQ23ACoverage"):
            return_value = 'creditor'
        elif self.protections.is_protected("FAQ5ACoverage"):
            return_value = 'lessor'
        else:
            return_value = None
        return return_value

    def __str__(self):
        return f"FPQ1 contract with the following protections:\n{str(self.protections)}"

    __repr__ = __str__

    def _bind_language_text_generators(self) -> None:
        """
        Bind the text generation functions of the contract language to this instance.

        The generators are bound on the instance (not on the class) so that contracts in different languages can
        coexist: creating a French contract must not change the text of an English contract created before.
        """
        language_content = fr if "fr" in self.locale else en
        for method_name in _SECTION_GENERATORS + _ENDORSEMENT_GENERATORS:
            generator = getattr(language_content, method_name)
            # Generators that read the contract take it as ``self``; the others only return static text.
            if "self" in inspect.signature(generator).parameters:
                generator = MethodType(generator, self)
            setattr(self, method_name, generator)
        # The FAQ 37A endorsement shares the FAQ 37AB text.
        self.generate_faq37a_endorsement_text = self.generate_faq37ab_endorsement_text

    def generate_contract_text(self) -> str:
        """
        Generate contract text.

        Return:
            The contract text.
        """

        header_text = self.generate_header_text()

        important_instructions = self.generate_important_instructions_text()

        declarations = self.generate_declaration_text()

        cancellation_of_policy = self.generate_cancellation_of_policy_text()

        bill = self.generate_bill_text()

        certificates = self.generate_certificates_text()

        client_advantages = self.generate_client_advantages_text()

        fpq1_amf_text = self.generate_fpq1_text()

        endorsements = self.generate_endorsements_text()

        contract_text = (
            header_text
            + important_instructions
            + declarations
            + cancellation_of_policy
            + bill
            + certificates
            + client_advantages
            + fpq1_amf_text
            + endorsements
        )

        return contract_text

    def generate_endorsements_text(self) -> str:
        """
        Method to generate the endorsements of the protections.

        Return:
            The endorsement text.
        """
        text = ""
        for endorsement in self.protections.endorsement_protections():
            endorsement_name = re.findall(r'FAQ[0-9]+[AB]*', endorsement)[0].lower()
            endorsement_text = getattr(self, f"generate_{endorsement_name}_endorsement_text")()
            text += endorsement_text + "\n"

        return text
