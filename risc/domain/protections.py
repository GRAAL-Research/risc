from typing import Dict, List, Union

from .tools import change_to_snake_case, change_to_camel_case

INCLUDE = "include"
EXCLUDE = "exclude"


class Protections:
    def __init__(self, protections: Dict) -> None:
        for key, value in protections.items():
            # We save attribute in snake case format and use the same function in a getter method
            # to get the proper attribute using the CamelCase coverage format.
            self.__setattr__(change_to_snake_case(key), value)

    def __str__(self) -> str:
        chapter_a_text = f"Chapter A: {self.get('LiabilityCoverage')}$\n"

        chapter_b_text = "Chapter B: \n"

        # Not in include or exclude since we want the case with the franchise amount

        b1 = self.get("PropertyDamageB1Coverage")
        if b1 is not None and b1 not in (INCLUDE, EXCLUDE):
            chapter_b_text += f"All risk protected with {b1}$ franchise\n"

        b2 = self.get("PropertyDamageB2Coverage")
        if b2 is not None and b2 not in (INCLUDE, EXCLUDE):
            chapter_b_text += f"Collision protected with {b2}$ franchise\n"

        b3 = self.get("PropertyDamageB3Coverage")
        if b3 is not None and b3 not in (INCLUDE, EXCLUDE):
            chapter_b_text += f"Other non collision protected with {b3}$ franchise\n"

        b4 = self.get("PropertyDamageB4Coverage")
        if b4 is not None and b4 not in (INCLUDE, EXCLUDE):
            chapter_b_text += f"Designated protected with {b4}$ franchise\n"

        return chapter_a_text + chapter_b_text.strip("\n")

    __repr__ = __str__

    def is_protected(self, protection_name: str) -> bool:
        """
        Method to validate if a set of protection include a specific protection.

        protection_name (str): Name of the protection to validate if it includes in the protection set.

        Return:
            A bool.
        """

        protection_status = self.get(protection_name)

        is_protected = False
        if protection_status is None:
            # We use the default is_protected = False
            pass
        elif isinstance(protection_status, str):
            if protection_status == "include":
                is_protected = True
        elif isinstance(protection_status, (int, float)):
            # > 0 since when protected the value is the deductible
            if protection_status > 0:
                is_protected = True

        return is_protected

    def property_damage_protections(self) -> List:
        """
        Method to extract the property damage with a protection (with a deductible). E.g. protection that are
        not by default include under another protection. For example, if a protection is a B1, than B2, B3 and B4
        are include. Thus, this method will return only the B1 protection.

        Return:
            A list of the property damage protection with a deductible.
        """
        property_damage_protections = []
        b1 = self.get("PropertyDamageB1Coverage")
        if b1 is not None and b1 not in (INCLUDE, EXCLUDE):
            property_damage_protections.append("PropertyDamageB1Coverage")

        b2 = self.get("PropertyDamageB2Coverage")
        if b2 is not None and b2 not in (INCLUDE, EXCLUDE):
            property_damage_protections.append("PropertyDamageB2Coverage")

        b3 = self.get("PropertyDamageB3Coverage")
        if b3 is not None and b3 not in (INCLUDE, EXCLUDE):
            property_damage_protections.append("PropertyDamageB3Coverage")

        b4 = self.get("PropertyDamageB4Coverage")
        if b4 is not None and b4 not in (INCLUDE, EXCLUDE):
            property_damage_protections.append("PropertyDamageB4Coverage")

        return property_damage_protections

    def endorsement_protections(self) -> List:
        """
        Method to get a list of all the endorsement protections in CamelCase.

        Return:
            A list of the endorsement.
        """
        return [change_to_camel_case(key) for key, _ in self.__dict__.items() if "f_a_q" in key]

    def get(self, item: str) -> Union[int, None]:
        """
        Method to get a deductible amount for a specific protection (item).

        item (str): Item (the protection) we want the deductible amount.

        Return:
            A int of the deductible amount or a None if not covered.
        """
        try:
            # Attribute are saved in snake case format.
            return getattr(self, change_to_snake_case(item))
        except AttributeError:
            return None
