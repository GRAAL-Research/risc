<div align="center">

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/risc_generator)](https://pypi.org/project/risc_generator)
[![PyPI Status](https://badge.fury.io/py/risc_generator.svg)](https://badge.fury.io/py/risc_generator)
[![PyPI Status](https://pepy.tech/badge/risc_generator)](https://pepy.tech/project/risc_generator)
[![Downloads](https://pepy.tech/badge/risc_generator/month)](https://pepy.tech/project/risc_generator)

[![Formatting](https://github.com/GRAAL-Research/risc/actions/workflows/formatting.yml/badge.svg?branch=stable)](https://github.com/GRAAL-Research/risc/actions/workflows/formatting.yml)
[![Linting](https://github.com/GRAAL-Research/risc/actions/workflows/linting.yml/badge.svg?branch=stable)](https://github.com/GRAAL-Research/risc/actions/workflows/linting.yml)
[![Tests](https://github.com/GRAAL-Research/risc/actions/workflows/tests.yml/badge.svg?branch=stable)](https://github.com/GRAAL-Research/risc/actions/workflows/tests.yml)

[![codecov](https://codecov.io/gh/GRAAL-Research/risc/branch/main/graph/badge.svg)](https://codecov.io/gh/GRAAL-Research/risc)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/62464699ff0740d0b8064227c4274b98)](https://www.codacy.com/gh/GRAAL-Research/risc/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=GRAAL-Research/risc&amp;utm_campaign=Badge_Grade)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

[![pr welcome](https://img.shields.io/badge/PR-Welcome-%23FF8300.svg?)](https://img.shields.io/badge/PR-Welcome-%23FF8300.svg?)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](http://www.gnu.org/licenses/lgpl-3.0)
</div>

## Here is RISC.

RISC is an open-source Python package data generator. It generates look-alike automobile insurance contracts based on
the Quebec regulatory insurance form in French and English.

Use RISC to generate look-a-like Quebec Car insurance forms (FPQ1) both in French and English. RISC simulation is
deterministic; thus, it can generate an aligned insurance contract (i.e. same driver data) using an initial seed.
RISC uses a pretrained TVAE model on a private dataset to generate look-a-like car protections.
See our [article here](https://arxiv.org/abs/2304.04212) for more detail about RISC implementation and generated the 
[RSICBAC](https://huggingface.co/datasets/davebulaval/RISCBAC) dataset specification.

RISC was written in Python 3.9 and is compatible with the __latest version of PyTorch__ and __Python >= 3.8__ (**SciPy
seems difficult to build on Python 3.11. Thus, we don't support Python 3.11 for now**).

## Getting Started:

```python
from risc_generator import TVAEFPQ1ContractFaker

seed = 42
n = 10

# Let's sample 10 insurance English insurance contracts (default configuration).
en_fpq1_synthetic_dataset = TVAEFPQ1ContractFaker(seed=seed).sample_contracts(number_sample=n)

# Now, let's do it for French contracts.
fr_fpq1_synthetic_dataset = TVAEFPQ1ContractFaker(language="fr", seed=seed).sample_contracts(number_sample=n)

# Since we have used the same seed, both datasets share the same insuree information.

# Use our own TVAE model:
fpq1_synthetic_dataset = TVAEFPQ1ContractFaker(tvae_synthetic_data_faker_model_path="a_path_to_a_tvae_.pkl",
                                               language="fr", seed=seed).sample_contracts(number_sample=n)

# You can also create a new FPQ1ContractFaker using another type of model using our interface.

from risc_generator import FPQ1ContractFaker, ProtectionsFaker


class RuleBaseFPQ1ContractFaker(FPQ1ContractFaker):
    def __init__(self, language: str = "en", seed: int = 42):
        protection_faker = ProtectionsFaker(
            model=ARuleBaseProtectionFaker()
        )
        super().__init__(protection_faker, language, seed=seed)
```

------------------

## Installation

Before installing RISC, you must have your environment's latest version of [PyTorch](https://pytorch.org/).

- **Install the stable version of RISC:**

```sh
pip install risc_generator
```

- **Install the latest development version of RISC:**

```sh
pip install -U git+https://github.com/GRAAL-Research/risc.git@dev
```

------------------

## Cite

Use the following for the article or dataset;

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

and this one for the package;

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
