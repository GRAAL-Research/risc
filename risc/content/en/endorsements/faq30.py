from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq30_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Quebec Endorsement Form\n"
        "Q.E.F. N 30\n"
        "Limitation of coverage for equipment and machinery attached to vehicle\n"
        "(Section A)\n"
        "The endorsement heading must be entered in the ''Declarations'' section of the insurance contract."
        "Details required for the endorsement may be entered in the ''Declarations'' section or in the endorsement"
        "itself, at the insurer's option.\n"
        "Name of insurer: \n"
        "Named insured: \n"
        "Endorsement to automobile insurance policy N:\n"
        "Effective date: This endorsement will apply from  at 12:01 A.M. "
        "standard time at the address of the named insured.\n"
        "Specified vehicle: This endorsement will apply only to the following described vehicle:\n"
        "(reference number shown in the ''Declarations'' section of the insurance contract)\n"
        "Endorsement description\n"
        "Subject to the Automobile Insurance Act, this endorsement limits coverage "
        "under Section A of the insurance contract by adding the following exclusion:\n"
        "\t Coverage will not be provided for the financial consequences that an insured "
        "person may incur if held civilly liable for damage caused by the following "
        "equipment or machinery, or accessories thereof, when mounted on or attached to the specified vehicle:\n"
        " \n"
        "(description of equipment or machinery)\n"
        "For the above exclusion to apply:\n"
        "\t damage must be caused while the equipment or machinery, or accessories thereof, "
        "are at the site of their use; and\n"
        "\t the insured person's civil liability must result from his or her owning the "
        "equipment or machinery, or accessories thereof, or from their use or their operation.\n"
        "All other conditions of the insurance contract remain the same.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
