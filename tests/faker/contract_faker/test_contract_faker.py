from unittest import TestCase
from unittest.mock import MagicMock

from risc_generator import FPQ1ContractFaker, Protections


class FPQ1ContractFakerTest(TestCase):
    def test_givenAFaq43Protections_whenIsProtected_thenReturnTrue(self):
        protections = Protections(protections={"FAQ43": "include", "Another protection": 0})
        self.assertTrue(protections.is_protected("FAQ43"))

    def test_givenNotAFaq43Protections_whenIsProtected_thenReturnTrue(self):
        protections = Protections(protections={"FAQ43": "exclude", "Another protection": 1})
        self.assertFalse(protections.is_protected("FAQ43"))


class FPQ1ContractFakerVehicleTest(TestCase):
    def _contract_faker_with_protections(self, protections: dict) -> FPQ1ContractFaker:
        protections_faker = MagicMock()
        protections_faker.protections.return_value = Protections(protections=protections)
        contract_faker = FPQ1ContractFaker(protections_faker=protections_faker, language="en")
        contract_faker.premium_faker = MagicMock()
        contract_faker.vehicle_faker = MagicMock()
        return contract_faker

    def test_givenAFaq5aProtection_whenContract_thenVehicleIsFakedAsARental(self):
        contract_faker = self._contract_faker_with_protections(
            {"LiabilityCoverage": 1000000, "FAQ5ACoverage": "include", "FAQ43Coverage": "exclude"}
        )

        contract_faker.contract()

        self.assertTrue(contract_faker.vehicle_faker.vehicle.call_args.kwargs["faq_5a"])

    def test_givenNoFaq5aProtection_whenContract_thenVehicleIsNotFakedAsARental(self):
        contract_faker = self._contract_faker_with_protections(
            {"LiabilityCoverage": 1000000, "FAQ5ACoverage": "exclude", "FAQ43Coverage": "exclude"}
        )

        contract_faker.contract()

        self.assertFalse(contract_faker.vehicle_faker.vehicle.call_args.kwargs["faq_5a"])
