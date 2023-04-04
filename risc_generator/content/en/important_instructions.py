from ..config import (
    GENERAL_FAKE_PHONE_NUMBER_1_800,
    NEW_PAGE_TAG,
    FAKE_ROADSIDE_ASSISTANCE_PHONE_NUMBER,
    FAKE_ROADSIDE_PROGRAM_NAME,
    FAKE_FIDELITY_PROGRAM_NAME_EN,
)


def generate_important_instructions_text(self) -> str:
    important_instructions = (
        "IMPORTANT INSTRUCTIONS\n\n"
        f"{self.formatted_text_date()}\n"
        "Please find hereafter instructions on very important parts of your insurance policy; we suggest that you "
        "read them carefully and take any required action, if necessary.\n\n"
    )

    fidelity = (
        f"{FAKE_FIDELITY_PROGRAM_NAME_EN} Program\n\n"
        "Because we appreciate your loyalty, we're pleased to offer you privileges that accumulate with your years "
        f"of loyalty, thanks to our {FAKE_FIDELITY_PROGRAM_NAME_EN} Program. Here are the details regarding your "
        "privileges, which you can also find in your Client Centre.\n"
        "Your recognized loyalty: New client\n"
        "Your privileges:\n"
        "\t Exclusive partner offers\n"
        "\t Legal assistance\n"
        "\t Psychological assistance service\n"
    )

    if self.protections.is_protected("FAQ41Coverage"):
        fidelity += "\t No deductible to pay in the case of a total loss or hit-and-run (auto)\n"

    fidelity += (
        "This list contains all the privileges associated with your recognized loyalty. Please note that the "
        "new privileges will be available at the renewal of each insurance policy held by a member of your "
        "household. Please see the Declarations or Coverage Summary Page(s) of your various insurance contracts held "
        "with us to learn more about applicable coverage details.\n"
    )

    if (
        self.protections.is_protected("FAQ33Coverage")
        or self.protections.is_protected("FAQ5ACoverage")
        or self.protections.is_protected("FAQ23ACoverage")
    ):
        notice_to_the_insuree = "Notice to the insured\n"
    else:
        notice_to_the_insuree = ""

    if self.protections.is_protected("FAQ33Coverage"):
        notice_to_the_insuree += (
            f"AUTOMOBILE POLICY No {self.policy_number}\n"
            f"You have chosen {FAKE_ROADSIDE_PROGRAM_NAME} Roadside Assistance, which provides you with 24-hour "
            "roadside assistance throughout Canada and the United States, 365 days a year.\n"
            "Therefore, three weeks after the effective date of the Q.E.F. endorsement N 33 Roadside Assistance "
            "Coverage, you will receive a kit for each eligible vehicle, including your membership card and your "
            "user's guide.\n"
            "As soon as the endorsement Q.E.F. N 33 comes into effect, you will be able to benefit from "
            f"this service even if you have not received your {FAKE_ROADSIDE_PROGRAM_NAME} roadside assistance kit."
            f"In case of need, simply call {FAKE_ROADSIDE_ASSISTANCE_PHONE_NUMBER} (24 hours a day, 7 days a week) "
            "and mention the policy number of the covered vehicle to the agent.\n"
        )

    if self.protections.is_protected("FAQ5ACoverage") or self.protections.is_protected("FAQ23ACoverage"):
        if self.protections.is_protected("FAQ5ACoverage"):
            creditor_type = "locator"
        else:
            creditor_type = "creditor"
        notice_to_the_insuree += (
            f"AUTOMOBILE POLICY No {self.policy_number} - Vehicle 1 : "
            f"{self.vehicle.format_vehicle_make_model_year_details()}\n"
            f"We are enclosing a copy of your policy to give to your {creditor_type}, "
            "if requested. It is included at the very end of this mailing.\n"
        )

    actions_to_take = (
        "\nActions Required\n\n"
        "Automobile insurance\n"
        "\t Detach and keep your insurance certificates with you.\n"
        "\t Detach and keep the automobile rental certificate with your driver's licence. This way, you will avoid "
        "paying additional insurance fees to the car rental agency.\n"
        "\t Please read the Coverage Summary section of your Quebec automobile insurance contract to ensure that "
        "your coverages are well-suited to your needs.\n"
        f"\t Don't hesitate to contact customer service at {GENERAL_FAKE_PHONE_NUMBER_1_800} for any questions "
        "regarding your contract.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    text = important_instructions + fidelity + notice_to_the_insuree + NEW_PAGE_TAG + "\n" + actions_to_take

    return text
