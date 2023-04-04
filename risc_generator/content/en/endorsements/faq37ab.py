from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq37ab_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Quebec Endorsement Form\n"
        "Q.E.F. N 37 (A-B)\n"
        "Changes to coverage for electronic equipment\n"
        "(Section B)\n"
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
        "Depending on the applicable option, this endorsement changes the coverage under Section B "
        "of the insurance contract for ''electronic equipment'' that is not ''original electronic equipment.''\n"
        "Option A: Limitation of indemnity\n"
        "In the event of a covered loss, the indemnity under Section B will be limited to  $ for "
        "all damaged ''electronic equipment'' that is not ''original electronic equipment.''\n"
        "In addition, the indemnity may not be greater than the ''actual cash value'' of the "
        "damaged ''electronic equipment''.\n"
        "This limitation will apply even when a Q.E.F. No. 43 (A to F) entitled ''Change to "
        "loss payment'' is attached to the insurance contract.\n"
        "Option B: Exclusion from coverage\n"
        "All ''electronic equipment'' that is not ''original electronic equipment'' will be excluded "
        "from coverage under Section B.\n"
        "Definitions\n"
        "1. Electronic equipment\n"
        "The expression ''electronic equipment'' as used in this endorsement means electronic devices:\n"
        "that are installed or meant to be installed permanently in or on the specified vehicle; and\n"
        "that are used for communicating, reproducing or recording sound or images or both "
        "simultaneously, including:\n"
        "\t - compact disc and DVD players;\n"
        "\t - personal navigation devices (GPS);\n"
        "\t - radios, including citizens band, two-way amateur or other radios; and\n"
        "\t - sound systems.\n"
        f"{NEW_PAGE_TAG}\n"
        f"{endorsement_header_text}"
        "2. Original electronic equipment\n"
        "The expression ''original electronic equipment'' as used in this endorsement means "
        "the electronic equipment:\n"
        "\t that is installed by the manufacturer or the dealer; and\n"
        "\t that was included in the original purchase price of the specified vehicle.\n"
        "All other conditions of the insurance contract remain the same.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
