import warnings

from sdv.single_table import TVAESynthesizer

try:
    from sdv.utils import load_synthesizer
except ImportError:  # Older SDV 1.x releases only expose the (now deprecated) ``TVAESynthesizer.load``.
    load_synthesizer = TVAESynthesizer.load

from ..model.synthetic_protections_model import SyntheticProtectionsModel


class TVAESyntheticProtectionsModelWrapper(SyntheticProtectionsModel):
    def __init__(self, model_path: str) -> None:
        """
        A Synthetic protection model using a TVAE architecture.
        See CTGAN (https://pypi.org/project/ctgan/) for more details.
        """
        with warnings.catch_warnings():
            # The pre-trained model was fitted with SDV 1.14.0; SDV warns on every load with a newer version.
            warnings.filterwarnings("ignore", message=".*this synthesizer was created on version.*")
            self.model = load_synthesizer(model_path)

    def sample(self, num_sample: int, **kwargs) -> dict:
        """
        Sample num_sample of a synthetic protections using a pre-trained model.

        num_sample (int): Number of sample to generate.
        kwargs (dict): Other parameters to use for sampling.

        Return:
            A dictionary of the synthetic protections.
        """
        # We set output_file_path to "disable" since it generate a tempfile and for a large number of single file
        # tempfile generation, it seems to raise an error. "Disabling" the tempfile creation avoid this error for an
        # unknown reason.
        return self.model.sample(num_rows=num_sample, output_file_path="disable", **kwargs).to_dict(orient="records")[0]
