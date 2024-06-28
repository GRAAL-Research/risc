import re

from ..general_header import generate_general_pages_header_text
from ...config import (
    FAKE_INSURER_ADDRESS,
    FAKE_INSURER_NAME,
    FAKE_INSURER_WEBSITE,
    NEW_PAGE_TAG,
    FAKE_FIDELITY_PROGRAM_NAME_EN,
    FAKE_ROADSIDE_PROGRAM_NAME,
)
from ....domain.premium import Premium
from ....domain.protections import Protections
from ....domain.tools import change_to_snake_case

all_property_damage_protection = [
    "PropertyDamageB1Coverage",
    "PropertyDamageB2Coverage",
    "PropertyDamageB3Coverage",
    "PropertyDamageB4Coverage",
]
endorsement_with_possible_premium = ["FAQ20", "FAQ20A", "FAQ33", "FAQ34", "FAQ34AB", "FAQ43"]
endorsement_without_premium = ["FAQ2", "FAQ5A", "FAQ23A", "FAQ27", "FAQ27A"]

# Base property damage text that we use to dynamically append the rest of the text base on the protections.
property_damage_b1_coverage_base_text = "Protection 1: All risks"
property_damage_b2_coverage_base_text = "Protection 2: Risk of collision and rollover"
property_damage_b3_coverage_base_text = "Protection 3: All risks except collision or rollover"
property_damage_b4_coverage_base_text = "Protection 4: Specific risks"

# Template for when the protection specified a deductible and a premium amount
property_damage_b1_coverage_deductible_template = "- Deductible {}$ per claim {}$"
property_damage_b2_coverage_deductible_template = "- Deductible {}$ per claim {}$"
property_damage_b3_coverage_deductible_template = "- Deductible {}$ per claim {}$"
property_damage_b4_coverage_deductible_template = "- Deductible {}$ per claim {}$"


def generate_declaration_header_text(policy_number: str) -> str:
    """
    Function to generate the declaration header text.

    policy_number (str): The policy number.

    Return:
        The declaration header text.
    """
    general_header_text = generate_general_pages_header_text(policy_number=policy_number)
    header = f"{general_header_text}" "DECLARATIONS\n" "ISSUE of your new insurance policy\n"
    return header


def generate_item_1_text(insuree_name: str, insuree_address: str) -> str:
    """
    Function to generate the item 1 text for the declaration.

    insuree_name (str): The name of the insuree.
    insuree_address (str): The address of the insuree.

    Return:
        The item 1 text.
    """
    text = (
        "Item 1. NAME AND ADDRESS OF THE NAMED INSURED*\n"
        f"{insuree_name}\n"
        f"{insuree_address}\n"
        "*The described vehicle is and will be mainly used, stored and parked in the town/city and province shown "
        "in Item 1. If not, the client or the named insured must so declare.\n"
    )
    return text


def generate_item_2_text(contract_start_date: str, contract_end_date: str) -> str:
    """
    Function to generate the item 2 text for the declaration.

    contract_start_date (str): The start date of the contract.
    contract_end_date (str): The end date of the contract.

    Return:
        The item 2 text.
    """
    text = (
        "Item 2. CONTRACT PERIOD\n"
        f"FROM: {contract_start_date}* TO: {contract_end_date}* EXCLUSIVELY\n"
        "*at 12:01 A.M. standard time at the address of the named insured.\n"
    )
    return text


def generate_item_3_text(
    formatted_vehicle_complete_details: str,
    car_ownership: str,
    vehicle_purchase_condition: str,
    car_with_financing: str,
    financing_details: str,
) -> str:
    """
    Function to generate the item 3 text for the declaration.

    formatted_vehicle_complete_details (str): The vehicle complete details in the proper format.
    car_ownership (str): The type of car ownership in the locale language (e.g. Bought/rented).
    vehicle_purchase_condition (str): The condition of the vehicle at purchase in the locale language (e.g. New)
    car_with_financing (Union[None, str]) The type of financing, if any. If None, it means no financing.
    financing_details (str): Financing details, if any.

    Return:
        The item 3 text.
    """
    text = (
        "Item 3. PARTICULARS OF THE DESCRIBED VEHICLE 1\n"
        f"{formatted_vehicle_complete_details} - {car_ownership} {vehicle_purchase_condition}\n"
    )

    if car_with_financing == "creditor":
        text += (
            "Creditor entitled to Chapter B benefits, according to his interest - Subject to the "
            "Q.E.F. endorsement N 23a\n"
            f"{financing_details}\n"
        )
    elif car_with_financing == "lessor":
        text += (
            "Lessor entitled to Chapter B benefits, according to his interest - Subject to the "
            "Q.E.F. endorsement N 5a\n"
            f"{financing_details}\n"
        )

    return text


# Endorsements with premium <


def generate_faq_20_text(faq_premium: str) -> str:
    """
    Function to generate FAQ20 text with a premium amount
    """
    text = (
        f"Q.E.F. N 20 - Travel Expense (Extended Form) (Chapter B) {faq_premium}$\n"
        "Travel expenses 50$ per day, total limit of 1500$ per claim\n"
        "Other covered expenses during a trip - 750$\n"
    )
    return text


def generate_faq_20a_text(faq_premium: str) -> str:
    """
    Function to generate FAQ20A text with a premium amount
    """
    text = (
        f"Q.E.F. N 20a - Travel Expense (Extended Form) (Chapter B) {faq_premium}$\n"
        "Travel expenses 50$ per day, total limit of 1500$ per claim\n"
        "Other covered expenses during a trip - 750$\n"
    )
    return text


def generate_faq_33_text(faq_premium: str) -> str:
    """
    Function to generate FAQ33 text with a premium amount
    """
    text = (
        "Q.E.F. N 33 - Insurance for roadside assistance expenses\n"
        f"{FAKE_ROADSIDE_PROGRAM_NAME} Roadside Assistance Program, available 24 hours a day, 7 days a week\n"
        "Maximum radius 50 km -\n"
        "In the event of a breakdown, the towing distance is increased to 100 km in the Laurentian Park, "
        "150 km in La Vérendrye Park and 100 km in Gaspésie National Park\n"
        f"Maximum number of events per insurance year 4 {faq_premium}$\n"
        "Limit per breakdown service 60$(1) - For a towing or a stuck vehicle, this limit is increased to 100$(1)\n"
        "Limit per policy year 400$(1)\n"
        "(1) These limits apply only when, on an exceptional basis, towing or breakdown service is not available "
        "through the Roadside Assistance Program\n"
        "See your brochure for all additional services available to you\n"
    )
    return text


def generate_faq_34ab_text(faq_premium: str) -> str:
    """
    Function to generate FAQ34AB text with a premium amount
    """
    text = (
        f"Q.E.F. N 34ab - Accident benefits insurance: {faq_premium}$\n"
        "Division 1: Subdivision A and B - Death and dismemberment benefits: 20000$ principal sum\n"
        "Subdivision C - Reimbursement of medical expenses: 2000$ per person\n"
        "Division 2: Total disability benefits: Not covered\n"
    )
    return text


def generate_faq_34_text(faq_premium: str) -> str:
    """
    Function to generate FAQ34 text with a premium amount
    """
    text = (
        f"Q.E.F. N 34 - Accident benefits insurance: {faq_premium}$\n"
        "Division 1: Subdivision A and B - Death and dismemberment benefits: 20000$ principal sum\n"
        "Subdivision C - Reimbursement of medical expenses: 2000$ per person\n"
        "Division 2: Total disability benefits: Not covered\n"
    )
    return text


def generate_faq_43_text(faq_premium: str) -> str:
    """
    Function to generate FAQ43 text with a premium amount.

    25% of the premium is the FAQ43A and 75% of the premium is the FAQ43E.
    """

    text = (
        f"Q.E.F. N 43a - Change to indemnity (Section B) - Partial loss - New parts "
        f"{round(int(faq_premium) * 0.25)}$\n"
        f"Q.E.F. N 43e - Change to indemnity (Section B) - Total loss - Replacement cost "
        f"{round(int(faq_premium) * 0.75)}$\n"
    )
    return text


# Endorsements with premium >


# Endorsements with no premium <
def generate_faq_2_text() -> str:
    """
    Function to generate FAQ2 text.
    """

    text = (
        "Q.E.F. N 2 - Vehicles of which named insured is not owner and when driven by named drivers "
        "(Section A) Included\n"
    )
    return text


def generate_faq_5a_text() -> str:
    """
    Function to generate FAQ5a text.
    """

    text = "Q.E.F. N 5a - Vehicles leased or under a contract of leasing Included\n"
    return text


def generate_faq_23a_text() -> str:
    """
    Function to generate FAQ23a text.
    """

    text = "Q.E.F. N 23a - Vehicles under financing Included\n"
    return text


def generate_faq_27_text() -> str:
    """
    Function to generate FAQ27 text.
    """

    text = (
        "Q.E.F. N 27 - Civil liability resulting from damage caused to vehicles of which named insured is not owner "
        "(including vehicles provided by an employer) (Section A) - 75000$\n"
        "Vehicles included under described vehicles, trailers or utility trailers\n"
        "Section B2 - $250 deductible and section B3 - $50 deductible\n"
    )
    return text


def generate_faq_27a_text() -> str:
    """
    Function to generate FAQ27a text.
    """

    text = (
        "Q.E.F. N 27a - Civil liability resulting from damage caused to vehicles of which named insured is not owner "
        "(including vehicles provided by an employer) (Section A) - 75000$\n"
        "Vehicles included under described vehicles, trailers or utility trailers\n"
        "Section B2 - $250 deductible and section B3 - $50 deductible\n"
    )
    return text


# Endorsements with no premium >
def generate_item_4_text(protections: Protections, premium: Premium) -> str:
    """
    Function to generate the item 4 text for the declaration.

    protections (Protections): The protections.
    premium (Premium): The premiums.

    Return:
        The item 4 text.
    """

    text = (
        "Item 4. COVERAGE / PERILS: The perils covered by the insurance contract are those for which an amount "
        "of insurance, a deductible or an insurance premium is shown in the table below. Coverage is subject to "
        "the conditions set out in the insurance contract.\n"
        "PREMIUM\n"
        "\t Section A - CIVIL LIABILITY -\n"
        f"Property damage or bodily injury to another person - Amount of insurance: "
        f"{protections.get('LiabilityCoverage')}$ {premium.get_premium('liability_coverage_premium')}$\n"
        f"\t Section B - DAMAGE TO INSURED VEHICLES\n"
    )

    # Chapter B text
    protection_with_deductible = protections.property_damage_protections()

    # We construct the text to use using template filling.
    for protection_name in all_property_damage_protection:

        # To extract the proper property damage text, we use the protection damage name written in CamelCase
        # and convert it into snake_case.
        snake_case_protection_name = change_to_snake_case(protection_name)
        base_text = eval(f"{snake_case_protection_name}_base_text")

        if protection_name in protection_with_deductible:
            # If the protection is one with a deductible, thus it need to be written in the protection text and include
            # a premium amount.
            protection_text = eval(f"{snake_case_protection_name}_deductible_template")
            protection_text = protection_text.format(
                protections.get(protection_name), premium.get_premium(f"{protection_name}Premium")
            )
        else:
            # The protection is either 'Include' or 'Exclude' (written in the locale language).
            if protections.is_protected(protection_name):
                # If the protection name is protected, it means it is 'include' (but written in the local language).
                protection_text = "Included"
            else:
                # If the protection name is not protected, it means it is 'exclude' (but written in the local language).
                protection_text = "Excluded"

        text += base_text + " " + protection_text + "\n"

    # We arbitrarily split the item 4 after the chapter B
    text += NEW_PAGE_TAG + "\n"

    # Endorsement text
    endorsement_protections = protections.endorsement_protections()
    for endorsement in endorsement_protections:
        if endorsement.strip("Coverage") in endorsement_with_possible_premium and protections.is_protected(
            f"{endorsement}"
        ):
            text += "Endorsement(s): "
            faq_premium = premium.get_premium(f"{endorsement}Premium")
            endorsement_number = re.findall(r'[0-9]+[AB]*', endorsement)[0].lower()
            text += eval(f"generate_faq_{endorsement_number}_text(faq_premium={faq_premium})")

        elif endorsement.strip("Coverage") in endorsement_without_premium and protections.is_protected(
            f"{endorsement}"
        ):
            text += "Endorsement(s): "
            endorsement_number = re.findall(r'[0-9]+[AB]*', endorsement)[0].lower()
            text += eval(f"generate_faq_{endorsement_number}_text()")

    text += (
        f"\t {FAKE_FIDELITY_PROGRAM_NAME_EN} program\n"
        f"Q.E.F. N 41\n"
        f"- Change to deductibles (Section B): Included\n"
        f"This endorsement makes the following changes to the deductible amounts under Section B\n"
        f"\t - No deductible to pay in the case of a hit-and-run offence if a police report was issued.\n"
        f"\t - No deductible to pay in the case of a total loss.\n"
        f"\t - No deductible to pay in the case of a windshield repair except in the case of a windshield "
        f"replacement.\n "
        f"\t - Should you incur a loss that affects two or more insurance products insured at "
        f"{FAKE_INSURER_NAME}, you will have but one deductible to pay, the highest applicable.\n"
    )

    text += "Premium due date: according to the agreed terms of payment\n"

    return text


def generate_premium_ticket(contract_starting_date: str, premium: Premium) -> str:
    text = (
        f"Prepared by the Insurer in Quebec City on {contract_starting_date}\n"
        f"Sherlock Holmes\n"
        f"President and chief executive officer\n"
        f"This is not an invoice. Please refer to the billing documents"
        f"for information on the amounts payable or receivable\n"
        f"PREMIUM VEHICLE 1\n"
        f"Class of insurance:\n"
        f"AUTOMOBILE\n"
        f"ANNUAL PREMIUM\n"
        f"{premium.total}$ (excluding tax)\n"
        f"YOUR NEW 12-MONTH POLICY\n"
        f"MONTANT\n"
        f"{premium.total}$ (excluding tax)\n"
        f"TAX\n"
        f"{premium.total * 0.09}$\n"
    )  # The Quebec taxes is 9%
    return text


def generate_item_6_text(
    insuree_name: str, insuree_birth_date: str, has_suspension: bool, number_of_claims_past_years: int
) -> str:
    """
    Function to generate the item 6 text for the declaration.

    insuree_name (str): The name of the insuree.
    insuree_birth_date (str): The birthdate of the insuree.
    has_suspension (bool): Either or not the insuree has a suspension.
    number_of_claims_past_years (int): The number of claims the insuree has.

    Return:
        The item 6 text.
    """
    text = (
        "Item 6. IMPORTANT STATEMENTS FOR ANALYZING THE RISK\n"
        f"\t Main driver: {insuree_name} Date of birth: {insuree_birth_date}\n"
    )

    if has_suspension:
        text += "\t At least one revocation or suspension of licence has been reported over the past three years\n"
    else:
        text += "\t No revocation or suspension of licence has been reported over the past three years\n"

    if number_of_claims_past_years > 0:
        text += f"\t {number_of_claims_past_years} loss or claim has been reported over the past five years\n"
    else:
        text += "\t No loss or claim has been reported over the past five years\n"

    return text


def generate_item_7_text(association_rebate: bool, payment_method: str) -> str:
    """
    Function to generate the item 7 text for the declaration.

    association_rebate (bool): Either or not the insuree has an association rebate.
    payment_method (str): The payment method.

    Return:
        The item 7 text.
    """

    text = "Item 7. INFORMATION FOR THE NAMED INSURED\n"

    if association_rebate or payment_method == "pre-authorize":
        text += "\t The premium takes into account the following discounts:\n"
        if association_rebate:
            text += "- As a member/customer of an association, you are eligible for the following discount: 10%.\n"
        if payment_method == "pre-authorize":
            text += "- 2% for choosing Pre-authorized payment as your premium payment method\n"

    text += (
        "\t Consent:If authorization has been granted for us to obtain credit information for the purposes of "
        "issuing this contract, please note that the information obtained will be updated and used for renewing "
        "your contract and for processing your property and casualty insurance files. This consent can be revoked "
        "at any time by notifying us in writing.\n"
    )

    return text


def generate_divulgation_text() -> str:
    """
    Function to generate the divulgation text for the declaration.

    Return:
        The divulgation text.
    """

    text = (
        "DISCLOSURE\n\n"
        "NOTICE CONCERNING THE PROTECTION OF PERSONAL INFORMATION\n"
        f"{FAKE_INSURER_NAME} protects the confidentiality of your personal information.\n"
        f"PURPOSE OF YOUR FILE\n"
        f"We collect and use your personal information to manage your Property and Casualty insurance file.\n"
        f"SECURITY\n"
        f"Your personal information is stored at our offices and protected by high security measures. Only our "
        f"employees, mandataries, distribution partners and service providers may access your personal information, "
        f"and solely when such access is required to perform their duties, carry out their mandate or fulfill "
        f"their service contract.\n"
        f"{FAKE_INSURER_NAME} may do business with one or more service providers based outside of Quebec. "
        f"It is therefore possible that some of your personal information held by "
        f"{FAKE_INSURER_NAME} may be stored outside of Quebec and governed by the laws of foreign "
        f"countries or states.\n"
        f"ACCESS AND CORRECTION\n"
        f"To access your file or make a correction to it, send your request in writing to the following address:\n"
        f"{FAKE_INSURER_NAME}\n"
        f"c/o Access to Information Service\n"
        f"{FAKE_INSURER_ADDRESS}\n"
        f"SERVICE OFFERING\n"
        f"{FAKE_INSURER_NAME}, its subsidiaries and their authorized representatives may use your personal "
        f"information to inform you of products and services that may be of interest to you. If, however, "
        f"you do not wish to receive this type of information, please write to us at the address above.\n"
        f"For more information about our personal information protection practices, refer to our personal "
        f"information protection statement at {FAKE_INSURER_WEBSITE}/en/personal-information-protection.\n"
        f"Your agent offers {FAKE_INSURER_NAME} products on an exclusive basis and does not receive any commission.\n"
    )
    return text
