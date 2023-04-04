from .general_header import generate_general_pages_header_text
from ..config import GENERAL_FAKE_PHONE_NUMBER_1_800, GENERAL_FAKE_PHONE_NUMBER, NEW_PAGE_TAG


def generate_cancellation_of_policy_text(self):
    general_header_text = generate_general_pages_header_text(policy_number=self.policy_number)
    general_header_text += "CANCELLATION OF POLICY\n"

    text = (
        f"{general_header_text}"
        "If your policy covers several vehicles and coverage for only one of them must be cancelled, do not use this "
        "form.\n"
        "Please contact Customer Service at the number listed below.\n"
        f"BEFORE CANCELLING contact Customer Service at {GENERAL_FAKE_PHONE_NUMBER} or "
        f"{GENERAL_FAKE_PHONE_NUMBER_1_800}, this could avoid you losing some of your advantages.\n"
        f"I hereby request the full cancellation of policy number {self.policy_number}, "
        "its endorsements, its renewals and if applicable, the reimbursement of any unearned premium effective: "
        "______________      ______________      ______________\n"
        "(Year) (Month) (Day)\n"
        "Signature :  ____________________________________________________________   "
        "Date : _____________     _____________     _____________\n"
        "(Insured) (Year) (Month) (Day)\n"
        "Signature :  ____________________________________________________________   "
        "Date : _____________     _____________     _____________\n"
        "(Additional Insured) (Year) (Month) (Day)\n"
        "Signature :  ____________________________________________________________   "
        "Date : _____________     _____________     _____________\n "
        "(Additional Insured) (Year) (Month) (Day)\n"
        "Reason of cancellation:  _____________________________________________  "
        "New insurer:  ________________________________________\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
