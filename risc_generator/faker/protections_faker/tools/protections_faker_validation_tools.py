from typing import Dict


def is_valid_protections(synthetic_coverage: Dict, can_have_faq_41: bool) -> bool:
    """
    Function to validate if a set of synthetic coverage is valid based on the Quebec insurance market.

    Conditions are:
        - It must contain the mandatory liability coverage.
        - It does not include the B1 coverage and any other B[2-4] coverage (B1 is a superset of all other
            protections).
        - It does not include B3 and B4 (B3 is a superset of B4).
        - It does not include a FAQ41 if it cannot have one (can_have_faq_41).
        - If it includes a FAQ43 it include a Section B coverage (B1, B2, B3 or B4).

    synthetic_coverage (Dict): A synthetic coverage dict with zeros and ones for the protection configuration.
    can_have_faq_41 (bool): Either or not the protection configuration can include a FAQ41 endorsement (depends on
        driver claims history in the past five years).

    Return:
        A bool representing if the protections is valid.
    """
    # The liability coverage is mandatory in Quebec
    if synthetic_coverage.get("LiabilityCoverage") == 0:
        return False
    valid_protections = True

    # Case where the protection include a Section B-1 (all risks) and other Section B coverage, which
    # is impossible since B-1 cover all loss of B-2 and B-3 (and B-4).
    if include_b1_coverage(synthetic_coverage) and not (
        not include_b2_coverage(synthetic_coverage)
        and not include_b3_coverage(synthetic_coverage)
        and not include_b4_coverage(synthetic_coverage)
    ):
        valid_protections = False

    # Case where the protection include a Section B-3 (all risks) and a B-4 coverage. B-4 is an under set of B-3.
    # i.e. not logical to have both.
    if include_b3_coverage(synthetic_coverage) and include_b4_coverage(synthetic_coverage):
        valid_protections = False

    # If the clients cannot have a FAQ41 (i.e. no claims in the past five years) but the synthetic protection include a
    # FAQ 41.
    if not can_have_faq_41 and synthetic_coverage.get("FAQ41Coverage") == 1:
        valid_protections = False

    # If the protections include a FAQ43, it must have a Section B coverage.
    if synthetic_coverage.get("FAQ43Coverage") and not (
        include_b1_coverage(synthetic_coverage)
        or include_b2_coverage(synthetic_coverage)
        or include_b3_coverage(synthetic_coverage)
        or include_b4_coverage(synthetic_coverage)
    ):
        valid_protections = False

    return valid_protections


def is_only_liability_coverage(synthetic_coverage: Dict) -> bool:
    """
    Function to validate if a synthetic coverage include only a liability coverage and no property damage coverage
    (B1 to B4).

    synthetic_coverage (Dict): A synthetic coverage dict with zeros and ones for the protection configuration.

    Return:
        Either or not the coverage include only liability coverage (no property damage coverage).
    """
    only_liability_coverage = True

    # Not an only liability coverage if at least one property coverage is there
    if (
        include_b1_coverage(synthetic_coverage)
        or include_b2_coverage(synthetic_coverage)
        or include_b3_coverage(synthetic_coverage)
        or include_b4_coverage(synthetic_coverage)
    ):
        only_liability_coverage = False
    return only_liability_coverage


def include_b1_coverage(synthetic_coverage: Dict) -> bool:
    """
    Function to validate if a synthetic coverage include a B1 property damage coverage.

    synthetic_coverage (Dict): A synthetic coverage dict with zeros and ones for the protection configuration.

    Return:
        Either or not the coverage include a B1 property damage coverage.
    """
    return synthetic_coverage.get("PropertyDamageB1Coverage") == 1


def include_b2_coverage(synthetic_coverage: Dict) -> bool:
    """
    Function to validate if a synthetic coverage include a B2 property damage coverage.

    synthetic_coverage (Dict): A synthetic coverage dict with zeros and ones for the protection configuration.

    Return:
        Either or not the coverage include a B2 property damage coverage.
    """
    return synthetic_coverage.get("PropertyDamageB2Coverage") == 1


def include_b3_coverage(synthetic_coverage: Dict) -> bool:
    """
    Function to validate if a synthetic coverage include a B3 property damage coverage.

    synthetic_coverage (Dict): A synthetic coverage dict with zeros and ones for the protection configuration.

    Return:
        Either or not the coverage include a B3 property damage coverage.
    """
    return synthetic_coverage.get("PropertyDamageB3Coverage") == 1


def include_b4_coverage(synthetic_coverage: Dict) -> bool:
    """
    Function to validate if a synthetic coverage include a B4 property damage coverage.

    synthetic_coverage (Dict): A synthetic coverage dict with zeros and ones for the protection configuration.

    Return:
        Either or not the coverage include a B4 property damage coverage.
    """
    return synthetic_coverage.get("PropertyDamageB4Coverage") == 1
