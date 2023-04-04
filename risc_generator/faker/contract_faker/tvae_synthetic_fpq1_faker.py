import os
from typing import Union

from ...faker.contract_faker.contract_faker import FPQ1ContractFaker
from ...faker.protections_faker.protections_faker import ProtectionsFaker
from ...model.tvae_synthetic_protections_model_wrapper import TVAESyntheticProtectionsModelWrapper


class TVAEFPQ1ContractFaker(FPQ1ContractFaker):
    def __init__(
        self, tvae_synthetic_data_faker_model_path: Union[None, str] = None, language: str = "en", seed: int = 42
    ) -> None:
        """
        A FPQ1 contract faker using a TVAE synthetic protections model to generate synthetic protections using CPU.


        tvae_synthetic_data_faker_model_path (str): Path to a TVAE model (see `here
            <https://docs.sdv.dev/sdv/single-table-data/modeling/synthesizers/tvaesynthesizer>`_
            for details on TVAE model) if you want to use your. If None, we will
            use our pre-trained model trained on a private dataset of a Canadian insurance company. By default,
            `"None"`.
        language (str): Either `'french'` (or `'fr'`) or `'english'` (or `'en'`). By default, `"en"`.
        seed (int): The seed value to use for the generation seed. By default, 42.
        """
        if tvae_synthetic_data_faker_model_path is None:
            tvae_synthetic_data_faker_model_path = (
                os.path.join(os.path.dirname(__file__), '../../resources', "tvae_model_q1_2023.pkl"),
            )
        protection_faker = ProtectionsFaker(
            model=TVAESyntheticProtectionsModelWrapper(tvae_synthetic_data_faker_model_path)
        )
        super().__init__(protection_faker, language, seed=seed)
