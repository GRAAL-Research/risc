from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq8_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Quebec Endorsement Form\n"
        "Q.E.F. N 8\n"
        "Deductible for property damage\n"
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
        "This endorsement changes Section A of the insurance contract by adding a deductible "
        "for property damage caused by the specified vehicle:\n"
        "\t A maximum deductible amount of  $ per loss.\n"
        "\t A maximum deductible amount of  $ per loss, when the vehicle is used to  .\n"
        "Agreement by named insured\n"
        "When the insurer pays an indemnity for property damage, the named insured agrees to reimburse "
        "the insurer for up to the deductible amount.\n"
        "Reimbursement must be made by the named insured as soon as the insurer pays the indemnity.\n"
        "Rights of insurer\n"
        "In respect of the deductible, the insurer will be entitled to:\n"
        "\t act as it wishes with regard to any investigation, transaction or settlement;\n"
        "\t authorize the named insured to enter into a transaction or a settlement with another "
        "person that has suffered property damage and indemnify that person. However, the total "
        "amount agreed upon further to the transaction or settlement must not exceed the deductible amount.\n"
        "All other conditions of the insurance contract remain the same.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
