from ..endorsements.endorsement_header import generate_endorsement_page_header_text
from ...config import NEW_PAGE_TAG


@staticmethod
def generate_faq28_endorsement_text() -> str:
    endorsement_header_text = generate_endorsement_page_header_text()
    text = (
        f"{endorsement_header_text}"
        "Quebec Endorsement Form\n"
        "Q.E.F. N 28\n"
        "Limitation of coverage for named drivers\n"
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
        "This endorsement limits coverage under the insurance contract when the specified vehicle is, "
        "at the time of the loss, being driven or used by:  (named driver)\n"
        "In such instance, coverage will be limited to the following perils, or to those "
        "perils entered specifically for this endorsement in the ''Declarations'' section of the insurance contract:\n"
        "COVERAGE | PERILS | AMOUNT OF INSURANCE AND DEDUCTIBLE | COVERED/NOT COVERED\n"
        "Section A: Civil liability | Property damage or bodily injury to another person | "
        "Amount of insurance:  $ |  $\n"
        "Section B: Damage to insured vehicles | Protection 1 : ''All perils'', Protection 2 : "
        "Perils of collision and upset, Protection 3: All perils other than collision or upset, "
        "Protection 4: Specific perils | Deductible per loss: $ $ $ $ |      \n"
        "All other conditions of the insurance contract remain the same.\n"
        f"{NEW_PAGE_TAG}\n"
    )

    return text
