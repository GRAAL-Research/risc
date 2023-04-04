from unittest import TestCase

from risc_generator import Protections


class FPQ1ContractFakerTest(TestCase):
    def test_givenAFaq43Protections_whenIsProtected_thenReturnTrue(self):
        protections = Protections(protections={"FAQ43": "include", "Another protection": 0})
        self.assertTrue(protections.is_protected("FAQ43"))

    def test_givenNotAFaq43Protections_whenIsProtected_thenReturnTrue(self):
        protections = Protections(protections={"FAQ43": "exclude", "Another protection": 1})
        self.assertFalse(protections.is_protected("FAQ43"))
