from typing import Dict

from ...faker.protections_faker.protections_amount_faker import (
    b1_deductible_faker,
    b2_deductible_faker,
    b3_deductible_faker,
    b4_deductible_faker,
)

INCLUDE = "include"
EXCLUDE = "exclude"


def property_coverage_faker(
    include_b1_coverage: bool,
    include_b2_coverage: bool,
    include_b3_coverage: bool,
    include_b4_coverage: bool,
) -> Dict:
    """
    Property coverage faker function of the deductible amount protection and logical of what is included and excluded
    base on the property coverage.

    include_b*_coverage (bool): Either or not a specific chapter coverage (B) is included or not.

    Return:
        A dict of the property coverage where the keys are the coverage and the values are the protections deductible,
        protection amount or, 'include' or 'exclude' coverage.
    """
    car_damage_coverage = {
        "PropertyDamageB1Coverage": INCLUDE,
        "PropertyDamageB2Coverage": INCLUDE,
        "PropertyDamageB3Coverage": INCLUDE,
        "PropertyDamageB4Coverage": INCLUDE,
    }

    # Cases:
    # B1 -> B2, B3 and B4 are 'include' since it is an all coverage
    # B2 only -> all others are 'exclude'
    # B3 only -> B1 and B2 are 'exclude' but B4 is 'include'
    # B4 only -> all others are 'exclude'
    # B2 and B3 -> B1 and B4 are 'include' since B2 and B3 is almost equivalent
    # B2 and B4 -> B1 et B3 are 'exclude'

    # PropertyDamageB1Coverage is B1 (or protection 1): All risk coverage
    # PropertyDamageB2Coverage is B2 (or protection 2): Collision coverage
    # PropertyDamageB3Coverage is B3 (or protection 3): Not collision coverage (fire, glass, etc.)
    # PropertyDamageB4Coverage is B4 (or protection 4): A list of designated risk (e.g. glass, fire, etc.).

    if include_b1_coverage and not include_b2_coverage and not include_b3_coverage and not include_b4_coverage:
        deductible = b1_deductible_faker()
        car_damage_coverage.update({"PropertyDamageB1Coverage": deductible})

    elif include_b2_coverage and not include_b1_coverage and not include_b3_coverage and not include_b4_coverage:
        deductible = b2_deductible_faker()
        car_damage_coverage.update({"PropertyDamageB2Coverage": deductible})

        car_damage_coverage.update({"PropertyDamageB1Coverage": EXCLUDE})
        car_damage_coverage.update({"PropertyDamageB3Coverage": EXCLUDE})
        car_damage_coverage.update({"PropertyDamageB4Coverage": EXCLUDE})

    elif include_b3_coverage and not include_b1_coverage and not include_b2_coverage and not include_b4_coverage:
        deductible = b3_deductible_faker()
        car_damage_coverage.update({"PropertyDamageB3Coverage": deductible})

        car_damage_coverage.update({"PropertyDamageB1Coverage": EXCLUDE})
        car_damage_coverage.update({"PropertyDamageB2Coverage": EXCLUDE})

    elif include_b4_coverage and not include_b1_coverage and not include_b2_coverage and not include_b3_coverage:
        deductible = b4_deductible_faker()
        car_damage_coverage.update({"PropertyDamageB4Coverage": deductible})

        car_damage_coverage.update({"PropertyDamageB1Coverage": EXCLUDE})
        car_damage_coverage.update({"PropertyDamageB2Coverage": EXCLUDE})
        car_damage_coverage.update({"PropertyDamageB3Coverage": EXCLUDE})

    elif include_b2_coverage and include_b3_coverage and not include_b1_coverage and not include_b4_coverage:
        deductible = b2_deductible_faker()
        car_damage_coverage.update({"PropertyDamageB2Coverage": deductible})

        deductible = b3_deductible_faker()
        car_damage_coverage.update({"PropertyDamageB3Coverage": deductible})

    elif include_b2_coverage and include_b4_coverage and not include_b1_coverage and not include_b3_coverage:
        deductible = b2_deductible_faker()
        car_damage_coverage.update({"PropertyDamageB2Coverage": deductible})

        deductible = b4_deductible_faker()
        car_damage_coverage.update({"PropertyDamageB4Coverage": deductible})

        car_damage_coverage.update({"PropertyDamageB1Coverage": EXCLUDE})
        car_damage_coverage.update({"PropertyDamageB3Coverage": EXCLUDE})

    return car_damage_coverage
