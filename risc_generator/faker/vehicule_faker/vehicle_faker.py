import random

from faker import Faker

from .vehicle_provider import VehicleProvider
from ...domain.vehicle import Vehicle
from ...faker.vehicule_faker.purchase_condition_faker import (
    QuebecPurchaseConditionFaker,
)
from ...faker.vehicule_faker.tools import is_valid_vehicle_year, generate_vin


class QuebecVehicleFaker(Faker):
    def __init__(self, locale: str) -> None:
        """
        locale (str): The locale language setting to use for simulation. Can either be `'fr_CA'` or `'en_CA'`.
        """
        super().__init__(locale=locale)
        self.vehicle_faker = Faker(locale=locale)
        self.vehicle_faker.add_provider(VehicleProvider)
        self.purchase_condition_faker = QuebecPurchaseConditionFaker(locale=locale)

    def vehicle(self, faq_43: bool, faq_5a: bool, contract_year: int) -> Vehicle:
        """
        Method to fake a vehicle.

        faq_43 (bool): Either or not the car need to respect FAQ43 endorsement.
        contract_year (bool): Year of the contract.

        Return:
            A faked Vehicle.
        """
        if faq_43:
            # If there is a FAQ 43, the vehicle need to be 5 years old or less

            invalid = True
            while invalid:  # We loop until the vehicle year is valid
                vehicle = self.vehicle_faker.vehicle_object()

                vehicle_year = vehicle.get("Year")
                if is_valid_vehicle_year(vehicle_year=vehicle_year, contract_year=contract_year):
                    # A vehicle year is valid when the difference between
                    # the starting year of the contrat and the age of the vehicle is
                    # smaller than 5. For example, given a starting year of the contract
                    # in 2020, vehicle needs to be at most a 2015 model.
                    invalid = False
                    vehicle_details = vehicle
        else:
            vehicle_details = self.vehicle_faker.vehicle_object()

        vehicle_details.update({"vin": generate_vin()})

        if faq_5a:
            # Endorsement FAQ5A is for car in rental, thus the car is necessarily new.
            vehicle_details.update({"purchase_condition": self.purchase_condition_faker.new_purchase_condition()})
        else:
            vehicle_details.update({"purchase_condition": self.purchase_condition_faker.purchase_condition()})

        # We lowercase the key since some are capitalize
        vehicle_details = {key.lower(): value for key, value in vehicle_details.items()}

        return Vehicle(**vehicle_details)

    def seed_instance(self, seed=42) -> None:
        """
        seed (int): The seed value to use for the generation seed. By default, 42.
        """
        super().seed_instance(seed)
        self.vehicle_faker.seed_instance(seed)
        self.purchase_condition_faker.seed_instance(seed)
        random.seed(seed)
