import random


def association_rebate_faker() -> bool:
    """
    Faker function to fake an association rebate.

    Return:
        A bool if it has an association rebate or not.
    """
    return random.choices([True, False], weights=[0.05, 0.95], k=1)[0]
