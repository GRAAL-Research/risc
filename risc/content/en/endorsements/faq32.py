from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq32_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Quebec Endorsement Form\n"
        "Q.E.F. N 32\n"
        "Recreational-purpose vehicles\n"
        "The endorsement heading must be entered in the ''Declarations'' section of the insurance contract\n"
        "Name of insurer: \n"
        "Named insured: \n"
        "Endorsement to automobile insurance policy N: \n"
        "Effective date: This endorsement will apply from  at 12:01 A.M. "
        "standard time at the address of the named insured.\n"
        "Specified vehicle: This endorsement will apply only to the following described vehicle:\n"
        "(reference number shown in the ''Declarations'' section of the insurance contract)\n"
        "Endorsement description\n"
        "Endorsement description\n"
        "This endorsement amends the insurance contract for a recreational-purpose motor vehicle that:\n"
        "\t is specifically designated in Item 3, ''Declarations'' of the insurance contract; or\n"
        "\t is one of the ''insured vehicles'' under the insurance contract.\n"
        "Recreational-purpose motor vehicle\n"
        "''Recreational-purpose motor vehicle'' means, among other things, any motor vehicle, "
        "whether commercially built or otherwise, of a type similar to:\n"
        "\t all-terrain vehicles;\n"
        "\t dune buggies;\n"
        "\t micro-cars;\n"
        "\t minibikes; and\n"
        "\t snowmobiles.\n"
        "Description of amendments\n"
        "1. Section A: Paragraph E, Article 2 entitled ''Insured vehicles'' is replaced with "
        "the following paragraph: ''E. Unless described in the ''Declarations'' section, any "
        "trailer (whether or not the named insured is the owner thereof) used with a "
        "recreational-purpose motor vehicle that is:\n"
        "\t of the same type as that described in the ''Declarations'' section; and\n"
        "\t covered by the insurance contract.\n"
        "2. General conditions: Paragraph (a), Article 7 entitled ''Prohibited use of "
        "insured vehicle'' is replaced with the following paragraph:\n"
        "''(a) When they are not legally authorized to drive;''\n"
        f"{NEW_PAGE_TAG}\n"
        f"{endorsement_header_text}"
        "3. The expressions ''motor vehicle'' and ''motor vehicle used for personal purposes'' are replaced "
        "throughout the insurance contract with the following expression: "
        "''recreational-purpose motor vehicle of the same type as that described in "
        "the ‘Declarations' section.''\n"
        "All other conditions of the insurance contract remain the same.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
