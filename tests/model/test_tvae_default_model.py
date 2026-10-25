from unittest import TestCase

import pytest

from risc_generator import TVAEFPQ1ContractFaker
from risc_generator.domain.contract import FPQ1Contract
from risc_generator.faker.contract_faker.tvae_synthetic_fpq1_faker import DEFAULT_TVAE_MODEL_PATH


class DefaultTVAEModelPathTest(TestCase):
    def test_givenThePackage_whenDefaultModelPath_thenItPointsToTheShippedModel(self):
        self.assertTrue(DEFAULT_TVAE_MODEL_PATH.is_file())
        self.assertEqual(".pkl", DEFAULT_TVAE_MODEL_PATH.suffix)


@pytest.mark.model
class TVAEFPQ1ContractFakerTest(TestCase):
    a_seed = 42
    a_number_of_contracts = 3

    def test_givenTheDefaultModel_whenSampleContracts_thenGeneratesContractsWithText(self):
        contracts = TVAEFPQ1ContractFaker(seed=self.a_seed).sample_contracts(number_sample=self.a_number_of_contracts)

        self.assertEqual(self.a_number_of_contracts, len(contracts))
        for contract in contracts:
            self.assertIsInstance(contract, FPQ1Contract)
            self.assertIn("QUEBEC AUTOMOBILE INSURANCE POLICY", contract.generate_contract_text())

    def test_givenTheSameSeed_whenSampleEnAndFrContracts_thenContractsAreAligned(self):
        en_contracts = TVAEFPQ1ContractFaker(language="en", seed=self.a_seed).sample_contracts(
            number_sample=self.a_number_of_contracts
        )
        fr_contracts = TVAEFPQ1ContractFaker(language="fr", seed=self.a_seed).sample_contracts(
            number_sample=self.a_number_of_contracts
        )

        for en_contract, fr_contract in zip(en_contracts, fr_contracts, strict=True):
            self.assertEqual(en_contract.client_number, fr_contract.client_number)
            self.assertEqual(en_contract.vehicle.vin, fr_contract.vehicle.vin)
            self.assertEqual(vars(en_contract.protections), vars(fr_contract.protections))
            # The English contract must stay in English after French contracts were generated.
            self.assertIn("QUEBEC AUTOMOBILE INSURANCE POLICY", en_contract.generate_contract_text())
            self.assertIn("POLICE D'ASSURANCE AUTOMOBILE DU QUÉBEC", fr_contract.generate_contract_text())
