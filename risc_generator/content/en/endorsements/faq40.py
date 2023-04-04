from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq40_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Quebec Endorsement Form\n"
        "Q.E.F. N 40\n"
        "Fire deductible\n"
        "(Section B)\n"
        "The endorsement heading must be entered in the ''Declarations'' section of the insurance contract\n"
        "Name of insurer: \n"
        "Named insured: \n"
        "Endorsement to automobile insurance policy N:\n"
        "Effective date: This endorsement will apply from  at 12:01 A.M. "
        "standard time at the address of the named insured.\n"
        "Specified vehicle: This endorsement will apply only to the following described vehicle:\n"
        "(reference number shown in the ''Declarations'' section of the insurance contract)\n"
        "Endorsement description\n"
        "This endorsement changes Article 7, Section B of the insurance contract as follows: The "
        "deductible for Protection 1, 3 or 4 will apply in the event of a fire.\n"
        "All other conditions of the insurance contract remain the same.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
