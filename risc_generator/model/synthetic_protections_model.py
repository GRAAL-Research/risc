from abc import ABC, abstractmethod


class SyntheticProtectionsModel(ABC):
    """
    Abstract class of a model.
    """

    @abstractmethod
    def sample(self, num_sample: int, **kwargs) -> dict:
        """
        Sample num_sample of a synthetic protections using a pre-trained model.

        num_sample (int): Number of sample to generate.
        kwargs (dict): Other parameters to use for sampling.

        Return:
            A dictionary of the synthetic protections.
        """
