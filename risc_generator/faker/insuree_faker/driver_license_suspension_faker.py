import random


class DriverLicenseSuspensionFaker:
    def __init__(
        self,
        total_alcohol_suspension: int = 14273,
        total_points_suspension: int = 93047,
        total_drivers: int = 5528681,
    ):
        """
        Faker to generate a probabilistic driver license suspension using the ratio of
        alcohol suspension and points suspension. Default are the 2019 SAAQ values
        https://saaq.gouv.qc.ca/fileadmin/documents/publications/donnees-statistiques-2019.pdf.
        We use the 2019 value due to the COVID restrictions during 2020-2021 where license suspension have
        significantly dropped due to less opportunity to drive, thus less opportunity to receive a driving suspension.

        total_alcohol_suspension: Number of alcohol suspension.
        total_points_suspension: Number of suspension due to points.
        total_drivers: Total diver population.
        """
        self.total_drivers = total_drivers
        self.total_alcohol_suspension = total_alcohol_suspension
        self.total_points_suspension = total_points_suspension

        self.proportion_of_suspension = (total_alcohol_suspension + total_points_suspension) / total_drivers

    def suspension(self) -> bool:
        """
        Method to fake a suspension.

        Return:
            A suspension status.
        """
        suspension = False
        u = random.uniform(0, 1)
        if u <= self.proportion_of_suspension:
            suspension = True
        return suspension
