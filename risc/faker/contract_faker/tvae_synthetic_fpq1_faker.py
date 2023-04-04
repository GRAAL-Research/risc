from ...faker.contract_faker.contract_faker import FPQ1ContractFaker
from ...faker.protections_faker.protections_faker import ProtectionsFaker
from ...model.tvae_synthetic_protections_model_wrapper import TVAESyntheticProtectionsModelWrapper


class TVAEFPQ1ContractFaker(FPQ1ContractFaker):
    def __init__(self, synthetic_data_faker_model_path: str, language: str, seed: int = 42) -> None:
        """
        A FPQ1 contract faker using a TVAE synthetic protections model to generate synthetic protections using CPU.


        synthetic_data_faker_model_path (str): Path to a TVAE model.
        language (str): Either `'french'` or `'english'`.
        seed (int): The seed value to use for the generation seed. By default, 42.
        """
        protection_faker = ProtectionsFaker(model=TVAESyntheticProtectionsModelWrapper(synthetic_data_faker_model_path))
        super().__init__(protection_faker, language, seed=seed)
