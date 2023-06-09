from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq20_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Quebec Endorsement Form\n"
        "Q.E.F. N 20\n"
        "Travel expenses\n"
        "(Section B)\n"
        "The endorsement heading must be entered in the ''Declarations'' section of the insurance contract."
        "Details required for the endorsement may be entered in the ''Declarations'' section or in the endorsement"
        "itself, at the insurer's option.\n"
        "Name of insurer:  \n"
        "Named insured:  \n"
        "Endorsement to automobile insurance policy N:  \n"
        "Effective date: This endorsement will apply from at 12:01 A.M. "
        "standard time at the address of the named insured.\n"
        "Additional insurance premium payable:\n"
        "\t Amount payable:  \n"
        "\t Due date:  \n"
        "Specified vehicle: This endorsement will apply only to the following described vehicle:\n"
        "(reference number shown in the ''Declarations'' section of the insurance contract)\n"
        "Endorsement description\n"
        "This endorsement extends coverage under Section B of the insurance contract by replacing "
        "the wording of Article 4.1, ''Travel expenses due to theft of insured vehicle'' with "
        "the wording below.\n"
        "This endorsement will apply only to the specified vehicle and only if the value of "
        "damage to the specified vehicle is greater than the deductible amount applicable "
        "to the loss that caused the damage.\n"
        "''4.1 Travel expenses\n"
        "4.1.1 Description of travel expenses\n"
        "If the named insured is no longer able to use the insured vehicle due to a covered loss, "
        "the insurer will reimburse any expenses incurred for\n"
        "\t leasing of a temporary replacement vehicle;\n"
        "\t public transportation;\n"
        "\t use of taxicab.\n"
        "Upon submission of receipts, payment for the above expenses will be made up to a "
        "maximum of  $ a day and  $ per loss for each insured vehicle.\n"
        "The above amounts cannot be less than the amounts that were specified in "
        "Additional coverages 4.1, of the insurance contract.\n"
        f"{NEW_PAGE_TAG}\n"
        f"{endorsement_header_text}"
        "4.1.2 Application of coverage\n"
        "If the entire insured vehicle was stolen, this coverage will apply only to expenses incurred "
        "from 12:01 A.M. the day after the theft is reported to the police or to the insurer.\n"
        "For all other covered losses, this coverage will apply only to expenses incurred:\n"
        "\t from the time at which the insured vehicle can no longer be operated under its own "
        "power due to damage to the vehicle; or\n"
        "\t from the time at which the insured vehicle is delivered for repair, if it can still "
        "be operated in spite of damage to the vehicle.\n"
        "Expenses will be eligible for reimbursement even if the insurance contract has expired "
        "since the loss.\n"
        "Expenses will no longer be eligible for reimbursement once :\n"
        "\t the insured vehicle has been replaced or repaired; or\n"
        "\t a settlement agreement for the loss has been reached before the insured "
        "vehicle is replaced or repaired.''\n"
        "All other conditions of the insurance contract remain the same.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
