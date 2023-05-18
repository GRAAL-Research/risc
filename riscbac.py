# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""RISCBAC: a synthetic bilingual automotive insurance contract dataset"""


import csv
import json
import os

import datasets


_CITATION = """\
@misc{beaucheminrisc,
    title={{RISC: Generating Realistic Synthetic Bilingual Insurance
Contract}},
    author={David Beauchemin and Richard Khoury},
    year={2023},
    eprint={2304.04212},
    archivePrefix={arXiv}
}
"""

# You can copy an official description
_DESCRIPTION = """\
RISCBAC was created using [RISC](https://github.com/GRAAL-Research/risc), an open-source Python package data 
generator. RISC generates look-alike automobile insurance contracts based on the Quebec regulatory insurance 
form in French and English.

It contains 10,000 English and French insurance contracts generated using the same seed. Thus, contracts share 
the same deterministic synthetic data (RISCBAC can be used as an aligned dataset). RISC can be used to generate 
more data for RISCBAC.
"""

_HOMEPAGE = "https://huggingface.co/datasets/davebulaval/RISCBAC"

_LICENSE = "Attribution 4.0 International (CC BY 4.0)"

_URLS = {
    "en": "https://huggingface.co/datasets/davebulaval/RISCBAC/blob/main/en.zip",
    "fr": "https://huggingface.co/datasets/davebulaval/RISCBAC/blob/main/fr.zip",
}


class RISCBAC(datasets.GeneratorBasedBuilder):
    """RISCBAC: a synthetic bilingual automotive insurance contract dataset"""

    VERSION = datasets.Version("1.0.0")

    BUILDER_CONFIGS = [
        datasets.BuilderConfig(
            name="en", version=VERSION, description="This part of the dataset are automobile contract in English."
        ),
        datasets.BuilderConfig(
            name="fr", version=VERSION, description="This part of the dataset are automobile contract in French."
        ),
    ]

    def _info(self):
        features = datasets.Features(
            {
                "text": datasets.Value("string"),
            }
        )
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            homepage=_HOMEPAGE,
            license=_LICENSE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        urls = _URLS[self.config.name]
        data_dir = dl_manager.download_and_extract(urls)
        if self.config.name == "en":
            return [
                datasets.SplitGenerator(
                    name=datasets.Split.TRAIN,
                    gen_kwargs={
                        "files_dir_path": os.path.join(data_dir, "en"),
                        "split": "full",
                    },
                )
            ]
        else:
            return [
                datasets.SplitGenerator(
                    name=datasets.Split.TRAIN,
                    gen_kwargs={
                        "files_dir_path": os.path.join(data_dir, "fr"),
                        "split": "full",
                    },
                ),
            ]

    def _generate_examples(self, files_dir_path, split):
        files = os.listdir(files_dir_path)
        for key, file in enumerate(files):
            with open(os.path.join(files_dir_path, file), "r", encoding="utf-8") as f:
                text = ["".join(f.readlines()).strip()]
                yield key, {"text": text}
