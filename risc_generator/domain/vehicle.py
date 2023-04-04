from typing import Union


class Vehicle:
    def __init__(
        self, year: int, make: str, model: str, vin: str, purchase_condition: str, electric_vehicle: bool
    ) -> None:
        """
        A vehicle.

        year (int): The car year (e.g. 2020).
        make (str): The car maker (e.g. Honda).
        model (str): The model of the car (e.g. Civic).
        vin (str): The vin number of the car.
        purchase_condition (str): The purchase condition of the car in the locale language (e.g. 'used').
        electric_vehicle (bool): Either or not the car is an electric one.
        """
        self.year = year
        self.make = make
        self.model = model
        self.vin = vin
        self.purchase_condition = purchase_condition
        self.electric_vehicle = electric_vehicle

    def __str__(self) -> str:
        return (
            f"{self.make.capitalize()} {self.model.capitalize()} "
            f"{str(self.year).capitalize()} VIN: {self.vin.capitalize()}"
        )

    def is_electric(self) -> bool:
        """
        Method to get if vehicle is an electric one.
        """
        return self.electric_vehicle

    def format_vehicle_complete_details(self, with_text: Union[None, str] = None) -> str:
        """
        Method to format the vehicle complete details.

        with_text (Union[None, str]): Either or not to include wrapping details with the vehicle complete details. If
            `with_text=None`, the vehicle details will be formatted as the following:
            `'vehicle_make vehicle_model vehicle_year vehicle_vin'`. If `with_text='Text'`, the vehicle details will be
            formatted as the following: `'vehicle_make - vehicle_model - vehicle_year - "Text" vehicle_vin'`.
            By default, None.

        Return:
            The formatted details text.
        """
        if with_text is not None:
            text = [" - ", " - ", f" - {with_text} "]
        else:
            text = [" "] * 3
        return f"{self.make}{text[0]}{self.model}{text[1]}{str(self.year)}{text[2]}{self.vin}"

    def format_vehicle_make_year_details(self) -> str:
        """
        Method to format the make and year vehicle details.

        Return:
            The formatted make and year details.
        """
        return f"{self.make} - {str(self.year)}"

    def format_vehicle_make_model_year_details(self) -> str:
        """
        Method to format the make, model and year vehicle details.

        Return:
            The formatted make, model and year details.
        """
        return f"{self.make} {self.model} {str(self.year)}"
