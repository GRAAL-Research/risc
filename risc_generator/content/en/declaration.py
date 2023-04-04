from .declaration_articles.items import (
    generate_declaration_header_text,
    generate_item_1_text,
    generate_item_2_text,
    generate_item_3_text,
    generate_item_4_text,
    generate_item_6_text,
    generate_item_7_text,
    generate_divulgation_text,
    generate_premium_ticket,
)
from ..config import NEW_PAGE_TAG


def generate_declaration_text(self) -> str:
    header = generate_declaration_header_text(policy_number=self.policy_number)

    item_1 = generate_item_1_text(insuree_name=self.insuree.name, insuree_address=self.insuree.address)

    item_2 = generate_item_2_text(
        contract_start_date=self.contract_start_date, contract_end_date=self.contract_end_date
    )

    item_3 = generate_item_3_text(
        formatted_vehicle_complete_details=self.vehicle.format_vehicle_complete_details(with_text="Numéro de série"),
        car_ownership=self.car_ownership(),
        vehicle_purchase_condition=self.vehicle.purchase_condition,
        car_with_financing=self.car_with_financing(),
        financing_details=self.financing,
    )

    item_4 = generate_item_4_text(protections=self.protections, premium=self.premium)
    premium_ticket = generate_premium_ticket(contract_starting_date=str(self.contract_start_date), premium=self.premium)

    item_6 = generate_item_6_text(
        insuree_name=self.insuree.name,
        insuree_birth_date=self.insuree.date_of_birth,
        has_suspension=self.insuree.suspension,
        number_of_claims_past_years=self.insuree.number_of_claims_past_years,
    )

    item_7 = generate_item_7_text(
        association_rebate=self.insuree.association_rebate, payment_method=self.payment_method
    )

    divulgation = generate_divulgation_text()

    text = (
        header
        + item_1
        + item_2
        + item_3
        + item_4
        + NEW_PAGE_TAG
        + "\n"
        + premium_ticket
        + NEW_PAGE_TAG
        + "\n"
        + item_6
        + item_7
        + NEW_PAGE_TAG
        + "\n"
        + divulgation
        + NEW_PAGE_TAG
        + "\n"
    )

    return text
