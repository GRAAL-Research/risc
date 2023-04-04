import re
from datetime import datetime, timedelta
from typing import Union

from babel.dates import format_date
from dateutil.relativedelta import relativedelta
from faker import Faker

from .premium import Premium
from ..content import fr, en
from ..domain.insuree import Insuree
from ..domain.protections import Protections
from ..domain.vehicle import Vehicle


class FPQ1Contract:
    def __init__(
        self,
        client_number: str,
        contract_start_date: datetime.date,
        insuree: Insuree,
        vehicle: Vehicle,
        payment_method: str,
        protections: Protections,
        premium: Premium,
        financing: Union[None, str],
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
        super().__init__()
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

        self._dynamic_import_text_generation_method()

        self._dynamic_import_method_endorsement_text_generation()

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

    def car_with_financing(self) -> Union[None, str]:
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

    def _dynamic_import_text_generation_method(self) -> None:
        # pylint: disable=too-many-branches
        """
        Method to dynamically handle the selection of the proper function to generate text in a specific language.
        """

        # Add header_template method
        if "fr" in self.locale:
            header_import = fr.header.generate_header_text
        else:
            header_import = en.header.generate_header_text
        setattr(FPQ1Contract, "generate_header_text", header_import)

        # Add important instructions method
        if "fr" in self.locale:
            important_instructions_import = fr.important_instructions.generate_important_instructions_text
        else:
            important_instructions_import = en.important_instructions.generate_important_instructions_text
        setattr(FPQ1Contract, "generate_important_instructions_text", important_instructions_import)

        # Add declaration method
        if "fr" in self.locale:
            declaration_import = fr.declaration.generate_declaration_text
        else:
            declaration_import = en.declaration.generate_declaration_text
        setattr(FPQ1Contract, "generate_declaration_text", declaration_import)

        # Add cancellation of policy method
        if "fr" in self.locale:
            cancellation_of_policy_import = fr.cancellation_of_policy.generate_cancellation_of_policy_text
        else:
            cancellation_of_policy_import = en.cancellation_of_policy.generate_cancellation_of_policy_text
        setattr(FPQ1Contract, "generate_cancellation_of_policy_text", cancellation_of_policy_import)

        # Add certificates method
        if "fr" in self.locale:
            certificates_import = fr.certificates.generate_certificates_text
        else:
            certificates_import = en.certificates.generate_certificates_text
        setattr(FPQ1Contract, "generate_certificates_text", certificates_import)

        # Add bill method
        if "fr" in self.locale:
            bill_import = fr.bill.generate_bill_text
        else:
            bill_import = en.bill.generate_bill_text
        setattr(FPQ1Contract, "generate_bill_text", bill_import)

        # Add client advantages method
        if "fr" in self.locale:
            client_advantages_import = fr.client_advantages.generate_client_advantages_text
        else:
            client_advantages_import = en.client_advantages.generate_client_advantages_text
        setattr(FPQ1Contract, "generate_client_advantages_text", client_advantages_import)

        # Add FPQ1 method
        if "fr" in self.locale:
            fpq1_method = fr.fpq_1.generate_fpq1_text
        else:
            fpq1_method = en.fpq_1.generate_fpq1_text
        setattr(FPQ1Contract, "generate_fpq1_text", fpq1_method)

    def _dynamic_import_method_endorsement_text_generation(self) -> None:
        # pylint: disable=too-many-locals, too-many-statements
        """
        Dynamically import all the method for the endorsement text generation
        """
        if "fr" in self.locale:
            faq_2_import = fr.endorsements.generate_faq2_endorsement_text
            faq_3_import = fr.endorsements.generate_faq3_endorsement_text
            faq_5a_import = fr.endorsements.generate_faq5a_endorsement_text
            faq_8_import = fr.endorsements.generate_faq8_endorsement_text
            faq_9_import = fr.endorsements.generate_faq9_endorsement_text
            faq_13_import = fr.endorsements.generate_faq13_endorsement_text
            faq_16_import = fr.endorsements.generate_faq16_endorsement_text
            faq_19_import = fr.endorsements.generate_faq19_endorsement_text
            faq_20_import = fr.endorsements.generate_faq20_endorsement_text
            faq_20a_import = fr.endorsements.generate_faq20a_endorsement_text
            faq_23a_import = fr.endorsements.generate_faq23a_endorsement_text
            faq_25_import = fr.endorsements.generate_faq25_endorsement_text
            faq_27_import = fr.endorsements.generate_faq27_endorsement_text
            faq_27a_import = fr.endorsements.generate_faq27a_endorsement_text
            faq_28_import = fr.endorsements.generate_faq28_endorsement_text
            faq_30_import = fr.endorsements.generate_faq30_endorsement_text
            faq_31_import = fr.endorsements.generate_faq31_endorsement_text
            faq_32_import = fr.endorsements.generate_faq32_endorsement_text
            faq_33_import = fr.endorsements.generate_faq33_endorsement_text
            faq_34_import = fr.endorsements.generate_faq34_endorsement_text
            faq_34ab_import = fr.endorsements.generate_faq34ab_endorsement_text
            faq_37ab_import = fr.endorsements.generate_faq37ab_endorsement_text
            faq_40_import = fr.endorsements.generate_faq40_endorsement_text
            faq_41_import = fr.endorsements.generate_faq41_endorsement_text
            faq_43_import = fr.endorsements.generate_faq43_endorsement_text
        else:
            faq_2_import = en.endorsements.generate_faq2_endorsement_text
            faq_3_import = en.endorsements.generate_faq3_endorsement_text
            faq_5a_import = en.endorsements.generate_faq5a_endorsement_text
            faq_8_import = en.endorsements.generate_faq8_endorsement_text
            faq_9_import = en.endorsements.generate_faq9_endorsement_text
            faq_13_import = en.endorsements.generate_faq13_endorsement_text
            faq_16_import = en.endorsements.generate_faq16_endorsement_text
            faq_19_import = en.endorsements.generate_faq19_endorsement_text
            faq_20_import = en.endorsements.generate_faq20_endorsement_text
            faq_20a_import = en.endorsements.generate_faq20a_endorsement_text
            faq_23a_import = en.endorsements.generate_faq23a_endorsement_text
            faq_25_import = en.endorsements.generate_faq25_endorsement_text
            faq_27_import = en.endorsements.generate_faq27_endorsement_text
            faq_27a_import = en.endorsements.generate_faq27a_endorsement_text
            faq_28_import = en.endorsements.generate_faq28_endorsement_text
            faq_30_import = en.endorsements.generate_faq30_endorsement_text
            faq_31_import = en.endorsements.generate_faq31_endorsement_text
            faq_32_import = en.endorsements.generate_faq32_endorsement_text
            faq_33_import = en.endorsements.generate_faq33_endorsement_text
            faq_34_import = en.endorsements.generate_faq34_endorsement_text
            faq_34ab_import = en.endorsements.generate_faq34ab_endorsement_text
            faq_37ab_import = en.endorsements.generate_faq37ab_endorsement_text
            faq_40_import = en.endorsements.generate_faq40_endorsement_text
            faq_41_import = en.endorsements.generate_faq41_endorsement_text
            faq_43_import = en.endorsements.generate_faq43_endorsement_text

        setattr(FPQ1Contract, "generate_faq2_endorsement_text", faq_2_import)
        setattr(FPQ1Contract, "generate_faq3_endorsement_text", faq_3_import)
        setattr(FPQ1Contract, "generate_faq5a_endorsement_text", faq_5a_import)
        setattr(FPQ1Contract, "generate_faq8_endorsement_text", faq_8_import)
        setattr(FPQ1Contract, "generate_faq9_endorsement_text", faq_9_import)
        setattr(FPQ1Contract, "generate_faq13_endorsement_text", faq_13_import)
        setattr(FPQ1Contract, "generate_faq16_endorsement_text", faq_16_import)
        setattr(FPQ1Contract, "generate_faq19_endorsement_text", faq_19_import)
        setattr(FPQ1Contract, "generate_faq20_endorsement_text", faq_20_import)
        setattr(FPQ1Contract, "generate_faq20a_endorsement_text", faq_20a_import)
        setattr(FPQ1Contract, "generate_faq23a_endorsement_text", faq_23a_import)
        setattr(FPQ1Contract, "generate_faq25_endorsement_text", faq_25_import)
        setattr(FPQ1Contract, "generate_faq27_endorsement_text", faq_27_import)
        setattr(FPQ1Contract, "generate_faq27a_endorsement_text", faq_27a_import)
        setattr(FPQ1Contract, "generate_faq28_endorsement_text", faq_28_import)
        setattr(FPQ1Contract, "generate_faq30_endorsement_text", faq_30_import)
        setattr(FPQ1Contract, "generate_faq31_endorsement_text", faq_31_import)
        setattr(FPQ1Contract, "generate_faq32_endorsement_text", faq_32_import)
        setattr(FPQ1Contract, "generate_faq33_endorsement_text", faq_33_import)
        setattr(FPQ1Contract, "generate_faq34_endorsement_text", faq_34_import)
        setattr(FPQ1Contract, "generate_faq34ab_endorsement_text", faq_34ab_import)
        setattr(FPQ1Contract, "generate_faq37a_endorsement_text", faq_37ab_import)  # Same as 37 AB
        setattr(FPQ1Contract, "generate_faq37ab_endorsement_text", faq_37ab_import)
        setattr(FPQ1Contract, "generate_faq40_endorsement_text", faq_40_import)
        setattr(FPQ1Contract, "generate_faq41_endorsement_text", faq_41_import)
        setattr(FPQ1Contract, "generate_faq43_endorsement_text", faq_43_import)

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
