import random


def generate_a_client_number() -> str:
    """
    Function to generate a client number of 6 digits in a string format.
    """
    return "".join([str(random.randint(0, 9)) for _ in range(6)])
