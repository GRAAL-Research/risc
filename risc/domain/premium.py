from typing import Dict, Union

from .tools import change_to_snake_case


class Premium:
    def __init__(self, **kwargs: Dict) -> None:
        """
        A premium for the protections that generate a premium increase. Namely, liability coverage, property damage
        coverage (B1 to B4), and endorsement 20A, 33, 34 and 43.

        **kwargs (dict): A dictionary where the keys are the protections included in the contract coverage and the
        values are the premium amount.
        """
        for key, value in kwargs.items():
            # We save attribute in snake case format and use the same function in a getter method
            # to get the proper attribute using the CamelCase coverage format.
            self.__setattr__(change_to_snake_case(key), value)

        self.total = sum(list(self.__dict__.values()))  # The total premium amount

    def get_premium(self, item: str) -> Union[str, None]:
        item = change_to_snake_case(item)
        value = None
        if self.get(item) is not None:
            value = str(self.get(item))
        return value

    def get(self, item: str) -> Union[int, None]:
        """
        Method to get a premium value for a specific protection (item). If the premium does not include the
        protection premium, it means it is not covered. Thus, we return a None.

        item (str): Item (the protection) we want the premium amount.

        Return:
            A int of the premium amount or a None if not covered.
        """
        try:
            item = change_to_snake_case(item)
            return getattr(self, item)
        except AttributeError:
            return None
