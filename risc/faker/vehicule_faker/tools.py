import random
import string


def is_valid_vehicle_year(vehicle_year: int, contract_year: int) -> bool:
    """
    Function to validate if a vehicle year respect the 5 years gap for the FAQ43 endorsements.

    vehicle_year (int): Year of the vehicle.
    contract_year (int): Year of the contract.

    Return:
        Either or not the vehicle is valid.
    """
    return contract_year - vehicle_year <= 5


def generate_vin() -> str:
    """
    Generate a VIN number that DOES NOT respect proper VIN specs. It generates a random selection of 17 characters as
    the VIN, which is not a valid VIN. The characters are number (0 to 9) and ascii capitalize letters (A-Z)
    (no special characters).
    """

    return "".join(random.choices(string.digits + string.ascii_uppercase, k=17))
