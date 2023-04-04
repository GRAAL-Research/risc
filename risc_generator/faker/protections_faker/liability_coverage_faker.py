from typing import Dict

from ...faker.protections_faker.protections_amount_faker import (
    liability_coverage_amount_faker,
)


def liability_coverage_faker(is_only_liability_coverage: bool) -> Dict:
    """
    Faker function to generate a liability coverage amount base.

    Our observation shows that liability coverage varies depending on the car's protection.
    If the vehicle is protected under liability coverage, liability amount protection is generally
    speaking only 1M$. Otherwise, the liability
    coverage is more equally distributed if the car is protected with material damage coverage. Thus, the cases are the
    following:

    - Only liability coverage: 95% of clients have 1M$ in liability coverage, and 5% have 2M$.
    - Liability and material damage coverage: 60% of clients have 1M$ in liability coverage, and 40% have 2M$.

    The probabilities are a simplification of our market observation. We haven't conducted an empirical analysis.

    Return:
        A dict with the key 'LiabilityCoverage' and the value of the liability coverage.
    """
    probs = [0.6, 0.4]
    if is_only_liability_coverage:
        probs = [0.95, 0.1]

    liability_coverage_amount = liability_coverage_amount_faker(liability_amount_probs=probs)

    return {"LiabilityCoverage": liability_coverage_amount}
