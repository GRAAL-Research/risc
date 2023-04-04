from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq23a_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Quebec Endorsement Form\n"
        "Q.E.F. N 23a\n"
        "Notice to creditor\n"
        "(Section B)\n"
        "The endorsement heading must be entered in the ''Declarations'' section of the insurance contract\n"
        "Name of insurer: \n"
        "Named insured: \n"
        "Name of creditor:  \n"
        "Address of creditor:  \n"
        "Endorsement to automobile insurance policy N: \n"
        "Effective date: This endorsement will apply from  at 12:01 A.M. "
        "standard time at the address of the named insured.\n"
        "Specified vehicle: This endorsement will apply only to the following described vehicle:\n"
        "(reference number shown in the ''Declarations'' section of the insurance contract)\n"
        "Endorsement description\n"
        "This endorsement changes Section B of the insurance contract by adding the following obligation:\n"
        "\t The insurer must give the creditor notice at least 15 days before cancelling or "
        "changing any coverage under Section B.\n"
        "\t The insurer is required to do so only if cancelling or changing the coverage is "
        "prejudicial to the creditor.\n"
        "All other conditions of the insurance contract remain the same.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
