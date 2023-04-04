from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq13_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Quebec Endorsement Form\n"
        "Q.E.F. N 13c\n"
        "Limitation under Protection 3 for vehicle glass\n"
        "(Section B)\n"
        "The endorsement heading must be entered in the ''Declarations'' section of the insurance contract\n"
        "Name of insurer: \n"
        "Named insured: \n"
        "Endorsement to automobile insurance policy N:\n"
        "Effective date: This endorsement will apply from  at 12:01 A.M. "
        "standard time at the address of the named insured.\n"
        "Specified vehicle: This endorsement will apply only to the following described vehicle:\n"
        "(reference number shown in the ''Declarations'' section of the insurance contract)\n"
        "Endorsement description\n"
        "This endorsement limits coverage under Protection 3, Section B of the insurance contract by excluding"
        "damage caused to the glass of the specified vehicle, except in the case of:\n"
        "\t attempted theft;\n"
        "\t civil commotion;\n"
        "\t earthquakes;\n"
        "\t explosions;\n"
        "\t falling or forced landing of aircraft or parts of aircraft;\n"
        "\t fire;\n"
        "\t hail;\n"
        "\t lightning;\n"
        "\t riot;\n"
        "\t rising water;\n"
        "\t stranding, sinking, burning, derailment or collision of any vehicle or vessel "
        "in or upon which the specified vehicle is being transported;\n"
        "\t theft; and\n"
        "\t windstorms.\n"
        "All other conditions of the insurance contract remain the same.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
