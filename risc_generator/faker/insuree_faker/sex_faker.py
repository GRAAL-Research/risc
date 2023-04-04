import random


class SexFaker:
    def __init__(
        self, locale: str, number_of_male_drivers: int = 2860709, population_of_drivers: int = 5546433
    ) -> None:
        """
        Faker to statistically generate a biological gender base on a driver population. By default, it uses Quebec
        province population.

        locale (str): The locale language setting to use for simulation. Can either be `'fr_CA'` or `'en_CA'`.
        number_of_male_drivers (int) : Number of male drivers. Default is Quebec number of male
            driver in 2020 base on the SAAQ bilan routier https://saaq.gouv.qc.ca/saaq/documentation/bilan-routier/.
        population_of_drivers (int): Number of drivers. Default is Quebec number of driver
            in 2020 base on the SAAQ bilan routier https://saaq.gouv.qc.ca/saaq/documentation/bilan-routier/.
        """
        self.number_of_male_drivers = number_of_male_drivers
        self.population_of_drivers = population_of_drivers

        self.proportion_of_male_driver = number_of_male_drivers / population_of_drivers

        if locale == "fr_CA":
            self.gender_1 = "homme"
            self.gender_2 = "femme"
        elif locale == "en_CA":
            self.gender_1 = "male"
            self.gender_2 = "female"
        else:
            raise ValueError(f"The locale {locale} is not supporter. It can either be 'fr_CA' or 'en_CA'.")

    def gender(self) -> str:
        """
        Method to fake a gender.

        Return:
            A gender in the locale language.
        """

        gender = self.gender_1
        u = random.uniform(0, 1)
        if u > self.proportion_of_male_driver:
            gender = self.gender_2
        return gender
