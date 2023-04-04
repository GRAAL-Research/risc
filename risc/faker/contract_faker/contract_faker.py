import random
from typing import List

import numpy as np
import torch
from faker import Faker
from tqdm import tqdm

from .premium_faker import QuebecPremiumFaker
from ... import Premium
from ...domain.contract import FPQ1Contract
from ...domain.insuree import Insuree
from ...domain.protections import Protections
from ...domain.vehicle import Vehicle
from ...faker.contract_faker.financing_faker import FinancingFaker
from ...faker.contract_faker.payment_method_faker import PaymentMethodFaker
from ...faker.contract_faker.tools import generate_a_client_number
from ...faker.insuree_faker.insuree_faker import InsureeFaker
from ...faker.protections_faker.protections_faker import ProtectionsFaker
from ...faker.vehicule_faker.vehicle_faker import QuebecVehicleFaker


class FPQ1ContractFaker:
    def __init__(self, protections_faker: ProtectionsFaker, language: str, seed: int = 42):
        """
        protections_faker (ProtectionsFaker): A protection faker to generate fake protections.
        language (str): Either `'french'` (or `'fr'`) or `'english'` (or `'en'`).
        seed (int): The seed value to use for the generation seed. By default, 42.
        """
        if language in ("french", "fr"):
            self.locale = "fr_CA"
        elif language in ("english", "en"):
            self.locale = "en_CA"
        else:
            raise ValueError("The language can either be 'french' or 'english'.")

        self.protections_faker = protections_faker
        self.insuree_faker = InsureeFaker(locale=self.locale)
        self.vehicle_faker = QuebecVehicleFaker(locale=self.locale)
        self.date_faker = Faker(locale=self.locale)
        self.payment_method_faker = PaymentMethodFaker(locale=self.locale)
        self.premium_faker = QuebecPremiumFaker()
        self.financing_faker = FinancingFaker(locale=self.locale)

        self._set_seed(seed=seed)
        self.clients_number = set()

    def contract(self) -> FPQ1Contract:
        """
        Method to fake a contract.

        clients_number (set): A set of already generate clients number to generate unique client numbers.

        Return:
            A FPQ1Contract in the contract faker language.
        """

        client_number = self._generate_unique_client_number()

        insuree: Insuree = self.insuree_faker.insuree()

        # Date the coverage start
        contract_start_date = self.date_faker.date_between(start_date="-1y", end_date="today")
        contract_year = contract_start_date.year

        protections: Protections = self.protections_faker.protections(can_have_faq_41=insuree.can_have_faq_41())

        premium: Premium = self.premium_faker.premium(protections=protections, insuree=insuree)

        include_faq_43: bool = protections.is_protected("FAQ43Coverage")
        include_faq_5a: bool = protections.is_protected("FAQ5aCoverage")

        vehicle: Vehicle = self.vehicle_faker.vehicle(
            faq_43=include_faq_43, faq_5a=include_faq_5a, contract_year=contract_year
        )

        payment_method = self.payment_method_faker.payment_method()

        if protections.is_protected("FAQ23ACoverage") or protections.is_protected("FAQ5ACoverage"):
            # Car are either finance with a financing (e.g. FAQ23A) or a lessor (i.e. rented) (e.g. FAQ5A).
            financing = self.financing_faker.financing()
        else:
            financing = None

        return FPQ1Contract(
            client_number=client_number,
            contract_start_date=contract_start_date,
            insuree=insuree,
            vehicle=vehicle,
            payment_method=payment_method,
            protections=protections,
            premium=premium,
            financing=financing,
            locale=self.locale,
        )

    def sample_contracts(self, number_sample: int) -> List:
        """
        Method to generate a sample of `number_sample` of contracts.

        number_sample (int): The number of sample to generate.

        Return:
            The list of synthetic contract.
        """
        fpq1_synthetic_data = []
        for _ in tqdm(range(0, number_sample)):
            fpq1_synthetic_data.append(self.contract())

        return fpq1_synthetic_data

    def _generate_unique_client_number(self) -> str:
        """
        Function to generate a unique client number base on randomly generated number.
        It uses a list of client number to validate if the new client number is not already in the client list.

        clients_number (list): A list of the already generated clients number.

        Return:
            A unique client ID (str).
        """
        unique = False

        while not unique:
            client_number = generate_a_client_number()
            if client_number not in self.clients_number:
                # Since client_number is a string (thus an iterable), the update add
                # all the 6 numbers of the client_number. So we use a list to add the
                # whole number.
                self.clients_number.update([client_number])

                unique = True
        return client_number

    def _set_seed(self, seed):
        Faker.seed(seed)
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        self.protections_faker.seed_instance(seed)
        self.date_faker.seed_instance(seed)
        self.payment_method_faker.seed_instance(seed)
        self.premium_faker.seed_instance(seed)
        self.vehicle_faker.seed_instance(seed)
