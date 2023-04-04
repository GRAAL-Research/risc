from scipy.stats import poisson


class ClaimsFaker:
    def __init__(self, mu: float = 0.0452) -> None:
        """
        Faker to generate the number of claims an insuree can have in the past five years.
        The default value, 0.0452 is the average claims' frequency for the past 11 years
        according to the GAA Quebec's data (https://gaa.qc.ca/en/statistics/claims-experience/collision-and-upset/).

        The faker use a poisson distribution to simulate the number of claims.
        mu (float): The frequency of a claim. By default, 0.0452 (base on GAA statistics).
        """

        self.mu = mu

    def claims(self, number_of_years: int = 5) -> int:
        """
        Simulate the number of claims in the past `number_of_years` and return
        the number of claims during those X years.

        number_of_years (int): The number of years of claims to sample. By default, 5 years.

        Return:
            The sum of claims in the past X years.
        """
        return poisson.rvs(mu=self.mu, size=number_of_years).sum()
