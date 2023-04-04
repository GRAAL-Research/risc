from typing import Dict

INCLUDE = "include"
EXCLUDE = "exclude"


def endorsement_coverage_parsing(synthetic_coverage: Dict) -> Dict:
    """
    Function to parse the synthetic coverage protections to modify the endorsement (e.g. "FAQ") into 'include' value
    if 1 and in 'exclude' value otherwise (0 value).

    synthetic_coverage (Dict): The synthetic coverage dict coverage with 1 for "protected" and 0 otherwise.

    Return:
        A parsed synthetic coverage where endorsement (FAQ) with ones are now 'include' and endorsement
        with zeros are 'exclude'.
    """
    return {key: INCLUDE if value == 1 else EXCLUDE for key, value in synthetic_coverage.items() if "FAQ" in key}
