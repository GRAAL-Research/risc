import random
from typing import List


def liability_coverage_amount_faker(liability_amount_probs: List) -> int:
    """
    Faker function to generate a fake liability coverage base on probability vectors (2 elements). Liability amount can
     either be 1 million or 2 million dollars.

    Return:
        The liability coverage amount (int).
    """

    return random.choices([1000000, 2000000], weights=liability_amount_probs, k=1)[0]


def b1_deductible_faker() -> int:
    """
    Faker function to generate a fake B1 deductible.

    Return:
        The deductible amount (int).
    """
    return random.choices([250, 500, 1000], weights=[0.15, 0.7, 0.20], k=1)[0]


def b2_deductible_faker() -> int:
    """
    Faker function to generate a fake B2 deductible.

    Return:
        The deductible amount (int).
    """

    return random.choices([250, 500, 1000], weights=[0.20, 0.65, 0.15], k=1)[0]


def b3_deductible_faker() -> int:
    """
    Faker function to generate a fake B3 deductible.

    Return:
        The deductible amount (int).
    """

    return random.choices([250, 500, 1000], weights=[0.50, 0.40, 0.10], k=1)[0]


def b4_deductible_faker() -> int:
    """
    Faker function to generate a fake B4 deductible.
    """

    return random.choices([250, 500, 1000], weights=[0.55, 0.40, 0.05], k=1)[0]
