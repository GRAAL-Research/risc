from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq25_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Quebec Endorsement Form\n"
        "Q.E.F. N 25\n"
        "Changes to the Declarations\n"
        "The endorsement heading must be entered in the ''Declarations'' section of the insurance contract."
        "Details required for the endorsement may be entered in the ''Declarations'' section or in the endorsement"
        "itself, at the insurer's option.\n"
        "Name of insurer: \n"
        "Named insured: \n"
        "Endorsement to automobile insurance policy N: \n"
        "Effective date: This endorsement will apply from  at 12:01 A.M. "
        "standard time at the address of the named insured.\n"
        "Specified vehicle: This endorsement will apply only to the following described vehicle:\n"
        "(reference number shown in the ''Declarations'' section of the insurance contract)\n"
        "This endorsement may not be used in any way to change the standard wording of the "
        "insurance contract approved by the Autorité des marchés financiers.\n"
        "Endorsement description\n"
        "This endorsement makes the following changes to the details entered in the ''Declarations'' "
        "section of the insurance contract\n"
        "\n"
        "All other conditions of the insurance contract remain the same.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
