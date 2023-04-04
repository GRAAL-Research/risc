from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq31_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Quebec Endorsement Form\n"
        "Q.E.F. N 31\n"
        "Equipment not owned by the named insured\n"
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
        "Endorsement description\n"
        "This endorsement extends coverage under the insurance contract to the following "
        "equipment not owned by the named insured:\n"
        "Application\n"
        "The equipment must be normally attached to the specified vehicle. In addition, "
        "the named insured must have the care, custody or control of such equipment.\n"
        "1. Section A\n"
        "Coverage under Section A is extended to the financial consequences that an "
        "insured person may incur if held civilly liable for damage caused to another person "
        "and resulting from the equipment described above.\n"
        "2. Section B\n"
        "Coverage under Section B as applicable to the specified vehicle is extended to:\n"
        "\t direct and accidental damage caused to the equipment described above;\n"
        "\t the disappearance of such equipment.\n"
        "For Section B, the indemnity will be payable up to the ''actual cash value'' of the "
        "equipment, subject to a maximum of   $ Payment will be made jointly to the named "
        "insured and  , to the extent of their respective interests.\n"
        "All other conditions of the insurance contract remain the same.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
