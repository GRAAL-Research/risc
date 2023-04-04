from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq5a_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Quebec Endorsement Form\n"
        "Q.E.F. N 5a\n"
        "Vehicles leased or under a contact of leasing Changes\n"
        "when owner and one lessee are mentioned as insureds\n"
        "The endorsement heading must be entered in the ''Declarations'' section of the insurance contract\n"
        "Name of insurer: \n"
        "Named insured: \n"
        "Endorsement to automobile insurance policy N:\n"
        "Effective date: This endorsement will apply from  at 12:01 A.M. "
        "standard time at the address of the named insured.\n"
        "Specified vehicle: This endorsement will apply only to the following described vehicle:\n"
        "(reference number shown in the ''Declarations'' section of the insurance contract)\n"
        "Endorsement description\n"
        "This endorsement changes the insurance contract:\n"
        "\t when the specified vehicle leased or under a contract of leasing; and\n"
        "\t when the owner and one lessee of the vehicle are mentioned as insureds under the insurance contract.\n"
        "The expression ''named insured'' will then be replaced by ''named lessee'' in the definition of "
        "the following\n"
        "''insured vehicles'':\n"
        "\t Vehicle of which the named insured has recently become the owner.\n"
        "\t Temporary substitute vehicle.\n"
        "\t Vehicle of which the named insured is not the owner.\n"
        "\t Trailer or semi-trailer of which the named insured is the owner.\n"
        "\t Trailer or semi-trailer of which the named insured is not the owner and that is used "
        "in connection with a vehicle insured under the insurance contract.\n"
        "All other conditions of the insurance contract remain the same.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
