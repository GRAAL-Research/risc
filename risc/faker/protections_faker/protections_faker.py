import random

from faker import Faker

from ...domain.protections import Protections
from ...faker.protections_faker.liability_coverage_faker import (
    liability_coverage_faker,
)
from ...faker.protections_faker.property_coverage_faker import (
    property_coverage_faker,
)
from ...faker.protections_faker.tools.endorsement_coverage_parsing import (
    endorsement_coverage_parsing,
)
from ...faker.protections_faker.tools.protections_faker_validation_tools import (
    is_valid_protections,
    is_only_liability_coverage,
    include_b1_coverage,
    include_b2_coverage,
    include_b3_coverage,
    include_b4_coverage,
)
from ...model.synthetic_protections_model import SyntheticProtectionsModel


class ProtectionsFaker(Faker):
    def __init__(self, model: SyntheticProtectionsModel) -> None:
        """
        model (model): A model to generate fake protections.
        """
        super().__init__()
        self.model = model

    def protections(self, can_have_faq_41: bool) -> Protections:
        """
        can_have_faq_41 (bool): Either or not the protections can include the endorsement FAQ41 in the protections.

        Return:
            A set of protections.
        """
        data_invalid = True
        synthetic_coverage = None

        while data_invalid:
            synthetic_coverage = self.model.sample(num_sample=1)
            if is_valid_protections(synthetic_coverage, can_have_faq_41=can_have_faq_41):
                data_invalid = False

        protections = {}

        liability_coverage = liability_coverage_faker(
            is_only_liability_coverage=is_only_liability_coverage(synthetic_coverage)
        )
        protections.update(liability_coverage)

        property_coverage = property_coverage_faker(
            include_b1_coverage=include_b1_coverage(synthetic_coverage),
            include_b2_coverage=include_b2_coverage(synthetic_coverage),
            include_b3_coverage=include_b3_coverage(synthetic_coverage),
            include_b4_coverage=include_b4_coverage(synthetic_coverage),
        )
        protections.update(property_coverage)

        endorsement_protection = endorsement_coverage_parsing(synthetic_coverage)
        protections.update(**endorsement_protection)

        return Protections(protections=protections)

    def seed_instance(self, seed=42) -> None:
        """
        seed (int): The seed value to use for the generation seed. By default, 42.
        """
        super().seed_instance(seed)
        random.seed(seed)
