from ..config import (
    GENERAL_FAKE_PHONE_NUMBER,
    GENERAL_FAKE_PHONE_NUMBER_1_800,
    FAKE_FAX_PHONE_NUMBER,
    FAKE_EMAIL,
    CLAIMS_FAKE_PHONE_NUMBER,
    CLAIMS_FAKE_PHONE_NUMBER_1_800,
    FAKE_LEGAL_HELP_PHONE_NUMBER,
    FAKE_INSURER_ADDRESS,
    FAKE_INSURER_WEBSITE,
    NEW_PAGE_TAG,
)


def generate_header_text(self) -> str:
    content_text = (
        f"{self.formatted_text_date()}\n\n\n"
        f"ISSUE\n"
        f"Client N: {self.client_number}\n"
        f"Policy / Term:\n"
        f"{self.policy} / 12 month\n\n"
        f"ALWAYS BY YOUR SIDE FOR YOUR INSURANCE\n\n"
        f"Please find enclosed your insurance documents.\n"
        f"We recommend that you read them carefully to ensure that they are correct.\n"
        f"If an Important Instructions page is included with these documents, please read through it carefully "
        f"because it contains crucial information regarding your coverage.\n"
        f"Feel free to contact us if you have any questions or comments.\n\n"
        f"CONTACT US\n"
        f"Customer Service\n"
        f"{GENERAL_FAKE_PHONE_NUMBER}\n"
        f"{GENERAL_FAKE_PHONE_NUMBER_1_800}\n"
        f"Fax: {FAKE_FAX_PHONE_NUMBER}\n"
        f"{FAKE_EMAIL}\n"
        f"8 a.m. to 8 p.m.\n"
        f"Monday to Friday\n"
        f"8:30 a.m. to 4 p.m., Saturday\n"
        f"Claims\n"
        f"{CLAIMS_FAKE_PHONE_NUMBER}\n"
        f"{CLAIMS_FAKE_PHONE_NUMBER_1_800}\n"
        f"24/7 emergency\n"
        f"Legal Assistance\n"
        f"{FAKE_LEGAL_HELP_PHONE_NUMBER}\n"
        f"8:30 a.m. to 7 p.m.\n"
        f"Monday to Thursday\n"
        f"8:30 a.m. to 5 p.m., Friday\n"
        f"Your branch\n"
        f"{FAKE_INSURER_ADDRESS}\n"
        f"8:30 a.m. to 5 p.m.\n"
        f"Monday to Friday\n"
        f"{FAKE_INSURER_WEBSITE}\n"
    )
    if self.payment_method == "bill":
        # Case where payment is a bill, thus it include a billing section in the TDM
        content_text += (
            f"Your Insurance Documents\n"
            f"(Table of Contents)\n"
            f"Important Instructions\n"
            f"Automobile Insurance\n"
            f"Policy number: {self.policy}\n"
            f"{self.vehicle.format_vehicle_make_year_details()}\n"
            f"Insurance Certificates\n"
            f"(Documents to be kept on file)\n"
            f"Invoice\n"
            f"Client Advantages\n"
            f"(Description of your client benefits)\n"
            f"Wording and Endorsements\n"
            f"{NEW_PAGE_TAG}\n"
            f"{NEW_PAGE_TAG}\n"  # An empty page
        )
    else:
        # Case where payment is pre-authorized, thus no billing in the documents.
        content_text += (
            f"Your Insurance Documents\n"
            f"(Table of Contents)\n"
            f"Important Instructions\n"
            f"Automobile Insurance\n"
            f"Policy number: {self.policy}\n"
            f"{self.vehicle.format_vehicle_make_year_details()}\n"
            f"Insurance Certificates\n"
            f"(Documents to be kept on file)\n"
            f"Client Advantages\n"
            f"(Description of your client benefits)\n"
            f"Wording and Endorsements\n"
            f"{NEW_PAGE_TAG}\n"
            f"{NEW_PAGE_TAG}\n"  # An empty page
        )
    return content_text
