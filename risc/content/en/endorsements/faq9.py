from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq9_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Quebec Endorsement Form\n"
        "Q.E.F. N 9\n"
        "Marine risk exclusion for amphibious vehicles\n"
        "Modifications\n"
        "The endorsement heading must be entered in the ''Declarations'' section of the insurance contract\n"
        "Name of insurer: \n"
        "Named insured: \n"
        "Endorsement to automobile insurance policy N:\n"
        "Effective date: This endorsement will apply from  at 12:01 A.M. "
        "standard time at the address of the named insured.\n"
        "Specified vehicle: This endorsement will apply only to the following described vehicle:\n"
        "(reference number shown in the ''Declarations'' section of the insurance contract)\n"
        "Endorsement description\n"
        "An amphibious vehicle is a vehicle designed or modified to:\n"
        "\t travel on land, and\n"
        "\t be used in or upon water\n"
        "If the specified vehicle is an amphibious vehicle, this endorsement excludes "
        "coverage under the insurance contract for loss occurring while it is used in or "
        "upon water or while it is being launched into or landed therefrom.\n"
        "All other conditions of the insurance contract remain the same.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
