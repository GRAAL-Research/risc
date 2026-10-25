<div align="center">

[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FGRAAL-Research%2Frisc%2Fmain%2Fpyproject.toml)](https://github.com/GRAAL-Research/risc/blob/main/pyproject.toml)
[![PyPI Status](https://badge.fury.io/py/risc_generator.svg)](https://badge.fury.io/py/risc_generator)
[![PyPI Status](https://pepy.tech/badge/risc_generator)](https://pepy.tech/project/risc_generator)
[![Downloads](https://pepy.tech/badge/risc_generator/month)](https://pepy.tech/project/risc_generator)

[![CI](https://img.shields.io/github/actions/workflow/status/GRAAL-Research/risc/tests.yml?branch=main&logo=github&label=CI)](https://github.com/GRAAL-Research/risc/actions/workflows/tests.yml)
[![Documentation](https://img.shields.io/github/actions/workflow/status/GRAAL-Research/risc/docs.yml?branch=main&logo=github&label=Documentation)](https://github.com/GRAAL-Research/risc/actions/workflows/docs.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/GRAAL-Research/risc/codeql-analysis.yml?branch=main&logo=github&label=CodeQL)](https://github.com/GRAAL-Research/risc/actions/workflows/codeql-analysis.yml)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/62464699ff0740d0b8064227c4274b98)](https://www.codacy.com/gh/GRAAL-Research/risc/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=GRAAL-Research/risc&amp;utm_campaign=Badge_Grade)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

[![pr welcome](https://img.shields.io/badge/PR-Welcome-%23FF8300.svg?)](https://img.shields.io/badge/PR-Welcome-%23FF8300.svg?)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](http://www.gnu.org/licenses/lgpl-3.0)
</div>

## Here is RISC

RISC is an open-source Python package data generator. It generates look-alike automobile insurance contracts based on
the Quebec regulatory insurance form (FPQ1) in French and English.

RISC simulation is deterministic: with the same seed, it generates aligned French and English contracts (same insuree,
vehicle and protections). RISC uses a TVAE model, pre-trained on a private dataset of a Canadian insurer, to generate
look-alike car protections. See our [article](https://arxiv.org/abs/2304.04212) for more details about the RISC
implementation and the specification of the [RISCBAC](https://huggingface.co/datasets/davebulaval/RISCBAC) dataset
generated with it.

RISC supports __Python 3.11 to 3.14__, NumPy 2 and recent versions of PyTorch. The pre-trained protections model is a
TVAE model from [SDV](https://github.com/sdv-dev/SDV) 1.x; SDV 2 is not supported yet.

## Getting Started

```python
from risc_generator import TVAEFPQ1ContractFaker

seed = 42
n = 10

# Sample 10 English insurance contracts (default configuration).
en_contracts = TVAEFPQ1ContractFaker(seed=seed).sample_contracts(number_sample=n)

# Now, the same for French contracts.
fr_contracts = TVAEFPQ1ContractFaker(language="fr", seed=seed).sample_contracts(number_sample=n)

# Since we used the same seed, both datasets share the same insuree, vehicle and protections.
# Each contract is an FPQ1Contract object; get its full text with
contract_text = en_contracts[0].generate_contract_text()

# The text contains a "<###NEW_PAGE###>" marker at each page break of the paper form.
pages = contract_text.split("<###NEW_PAGE###>")

# Use your own TVAE model (an SDV 1.x ``TVAESynthesizer`` saved with ``synthesizer.save``):
contracts = TVAEFPQ1ContractFaker(
    tvae_synthetic_data_faker_model_path="a_path_to_a_tvae_model.pkl", language="fr", seed=seed
).sample_contracts(number_sample=n)
```

You can also plug another type of protections model by implementing the `SyntheticProtectionsModel` interface:

```python
from risc_generator import FPQ1ContractFaker, ProtectionsFaker, SyntheticProtectionsModel


class RuleBasedProtectionsModel(SyntheticProtectionsModel):
    def sample(self, num_sample: int, **kwargs) -> dict:
        # Return a dictionary of protections (same keys as the pre-trained TVAE model).
        ...


class RuleBasedFPQ1ContractFaker(FPQ1ContractFaker):
    def __init__(self, language: str = "en", seed: int = 42) -> None:
        protections_faker = ProtectionsFaker(model=RuleBasedProtectionsModel())
        super().__init__(protections_faker, language, seed=seed)
```

------------------

## Installation

RISC requires Python 3.11 or later. [PyTorch](https://pytorch.org/) is installed as a dependency; install it first
if you need a specific build (e.g. CPU only or a given CUDA version).

- **Install the stable version of RISC:**

> Python 3.11+ support starts with RISC 0.1.0. Until it is published on PyPI, install the development version below.

```sh
pip install risc_generator
# or
uv pip install risc_generator
```

- **Install the latest development version of RISC:**

```sh
pip install -U git+https://github.com/GRAAL-Research/risc.git@main
```

------------------

## RISCBAC Dataset

[RISCBAC](https://huggingface.co/datasets/davebulaval/RISCBAC) contains 10,000 English and French insurance contracts
generated with RISC using the same seed. The `RISCBAC.py` file at the root of this repository is its Hugging Face
`datasets` loading script, and `RISCBACCHANGELOG.md` tracks the dataset versions.

------------------

## Cite

Use the following for the article or dataset:

```
@article{Beauchemin2023RISC,
	author = {Beauchemin, David and Khoury, Richard},
	journal = {Proceedings of the Canadian Conference on Artificial Intelligence},
	year = {2023},
	month = {jun 5},
	note = {https://caiac.pubpub.org/pub/k18zu6c9},
	publisher = {Canadian Artificial Intelligence Association (CAIAC)},
	title = {RISC: Generating {Realistic} {Synthetic} {Bilingual} {Insurance} {Contract}},
}
```

and this one for the package:

```
@misc{risc,
    author = {David Beauchemin},
    title  = {{RISC: an open-source Python package data generator to generate look-alike automobile insurance contracts based on the Quebec regulatory insurance form in French and English}},
    year   = {2023},
    note   = {\url{https://github.com/GRAAL-Research/risc}}
}
```

------------------

## Contributing to RISC

We welcome user input, whether it regards bugs found in the library or feature propositions! Make sure to have a
look at our [contributing guidelines](https://github.com/GRAAL-Research/risc/blob/main/.github/CONTRIBUTING.md)
for more details on this matter.

## License

RISC is LGPLv3 licensed, as found in
the [LICENSE file](https://github.com/GRAAL-Research/risc/blob/main/LICENSE).

------------------
