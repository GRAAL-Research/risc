from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq2_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Quebec Endorsement Form\n"
        "Q.E.F. N 2\n"
        "Vehicles of which named insured is not owner and when driven by named drivers\n"
        "(Section A)\n"
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
        "Endorsement description\n"
        "This endorsement extends coverage under Section A of the insurance contract by adding the following "
        "paragraph to Article 2 entitled ''Insured vehicles'':\n"
        "''a vehicle of the   type when driven, at the time of the loss, by one of the "
        "following persons:\n"
        "NAME | AGE | RELATIONSHIP TO NAMED INSURED\n"
        "1. | | \n"
        "2. | | \n"
        "3. | | \n"
        "4. | | \n"
        "For the vehicle to be considered an ''insured vehicle'' under Section A, the following conditions "
        "must be met:\n"
        "1. At the time of the loss, the vehicle is not being driven in connection with a garage business.\n"
        "2. The owner or frequent user of the vehicle is not one of the following persons:\n"
        "\t the named insured or anyone whose domicile is the same as that of the named insured;\n"
        "\t a person mentioned in the table above or anyone whose domicile is the same as that of "
        "such person.\n"
        f"{NEW_PAGE_TAG}\n"
        f"{endorsement_header_text}"
        "3. The vehicle is not provided by an employer of:n"
        "\t the named insured or anyone whose domicile is the same as that of the named insured;\n"
        "\t a person mentioned in the table above or anyone whose domicile is the same as that of "
        "such person.\n"
        "4. The vehicle is not appropriated to a use:\n"
        "\t as a taxicab, bus or coach; or\n"
        "\t for commercial delivery.''\n"
        "All other conditions of the insurance contract remain the same.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
