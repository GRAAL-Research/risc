import random
from statistics import mean

from faker import Faker


class QuebecPurchaseConditionFaker(Faker):
    def __init__(self, locale: str) -> None:
        """
        Fake the purchase condition by using the average ratio of Quebec new cars
        over the total number of car base on the Statistic Canada and the 2021 SAAQ statistics.
        Statistic Canada: https://www150.statcan.gc.ca/n1/pub/71-607-x/71-607-x2021019-fra.htm
        SAAQ: https://saaq.gouv.qc.ca/saaq/documentation/bilan-routier/

        locale (str): The locale language setting to use for simulation. Can either be `'fr_CA'` or `'en_CA'`.
        """
        super().__init__(locale=locale)

        new_car_2017 = 474263
        total_car_2017 = 4758010
        ratio_2017 = new_car_2017 / total_car_2017

        new_car_2018 = 464208
        total_car_2018 = 4779332
        ratio_2018 = new_car_2018 / total_car_2018

        new_car_2019 = 458195
        total_car_2019 = 4836544
        ratio_2019 = new_car_2019 / total_car_2019

        new_car_2020 = 383256
        total_car_2020 = 4936202
        ratio_2020 = new_car_2020 / total_car_2020

        self.average_ratio = mean([ratio_2017, ratio_2018, ratio_2019, ratio_2020])

        if locale == "fr_CA":
            self.used_condition = "usagé"
            self.new_condition = "neuf"
        elif locale == "en_CA":
            self.used_condition = "used"
            self.new_condition = "new"
        else:
            raise ValueError(f"The locale {locale} is not supporter. It can either be 'fr_CA' or 'en_CA'.")

    def purchase_condition(self) -> str:
        """
        Method to fake a purchase condition.

        Return:
            A purchase condition in the locale language.
        """
        purchase_condition = self.used_condition

        u = random.uniform(0, 1)
        if u <= self.average_ratio:
            purchase_condition = self.new_condition

        return purchase_condition

    def new_purchase_condition(self) -> str:
        """
        Method to return a new purchase condition in the locale language.

        Return:
            A new purchase condition.
        """
        return self.new_condition

    def seed_instance(self, seed=42) -> None:
        """
        seed (int): The seed value to use for the generation seed. By default, 42.
        """
        super().seed_instance(seed)
        random.seed(seed)
