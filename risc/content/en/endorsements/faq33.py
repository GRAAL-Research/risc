from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq33_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Quebec Endorsement Form\n"
        "Q.E.F. N 33\n"
        "Insurance for roadside assistance costs\n"
        "The endorsement heading must be entered in the ''Declarations'' section of the insurance contract."
        "Details required for the endorsement may be entered in the ''Declarations'' section or in the endorsement"
        "itself, at the insurer's option.\n"
        "Name of insurer: \n"
        "Named insured: \n"
        "Endorsement to automobile insurance policy N:\n"
        "Effective date: This endorsement will apply from  at 12:01 A.M. "
        "standard time at the address of the named insured.\n"
        "Additional insurance premium payable:\n"
        "\t Amount payable:  \n"
        "\t Due date:  \n"
        "Specified vehicle: This endorsement will apply only to the following described vehicle:\n"
        "(reference number shown in the ''Declarations'' section of the insurance contract)\n"
        "Endorsement description\n"
        "This endorsement provides that the roadside assistance costs described below and incurred for "
        "the specified vehicle will be reimbursed by the insurer.\n"
        "Roadside assistance costs\n"
        "The costs of the following roadside assistance services will be covered:\n"
        "\t battery boosting;\n"
        "\t door unlocking;\n"
        "\t gas delivery, up to 10 liters;\n"
        "\t towing within a radius of   kilometres (minimum 25 km);\n"
        "\t wheel change.\n"
        "Mechanical repairs and parts or supplies used to repair the specified vehicle are "
        "not covered under this endorsement.\n"
        "Limits of liability\n"
        "\t  $ per event giving rise to roadside assistance charges.\n"
        "\t  $ per policy year.\n"
        "\t   events per policy year.\n"
        "Claim\n"
        "The named insured must justify a claim by submitting to the insurer paid invoices "
        "for the roadside assistance costs.\n"
        "All other conditions of the insurance contract remain the same.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
