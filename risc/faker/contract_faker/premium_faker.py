import random

import numpy as np
import torch
from faker import Faker

from ... import Insuree, Protections, Premium, change_to_snake_case


class QuebecPremiumFaker(Faker):
    def __init__(self) -> None:
        """
        The values of the mu uses are base on the 2021 GAA statistics
        (https://gaa.qc.ca/fr/statistiques/cout-de-l-assurance-automobile/cout-de-l-assurance-
        pour-les-voitures-de-tourisme/).
        The 2 millions mu bonus is base on our overall experience of the premium base increase (~2$/month usually).

        The value of the sigma, 0.5, is selected so the concentration the distribution around the mu value.
        """
        super().__init__()
        self.liability_mu = 351
        self.liability_mu_increase = 48

        self.sigma = 0.5

        self.property_damage_b2_coverage_mu = 328
        self.property_damage_b3_coverage_mu = 174
        self.property_damage_b1_coverage_mu = self.property_damage_b2_coverage_mu + self.property_damage_b3_coverage_mu
        self.property_damage_b4_coverage_mu = round(174 * 0.99)  # This protection is a little less that B3

        self.endorsement_20_mu = 50
        self.endorsement_33_mu = 40
        self.endorsement_34_mu = 10
        self.endorsement_43_mu = 250

    def premium(self, protections: Protections, insuree: Insuree) -> Premium:
        # pylint: disable=too-many-branches
        """
        Faker to generate a premium base on an insuree risk. By default, it uses Quebec province premium statistic.
        protections (Protections): Protection to generate the premium.
        insuree (Insuree): Insuree to base the risk factor on.

        About the probabilistic distribution parameters:

        Mu risk factors:
            - Age and Sex: Base on the 2021 GAA Report
                (https://gaa.qc.ca/fr/statistiques/criteres-de-tarification/selon-l-age-et-le-sexe/)
                equally averaged (for simplification).
            - Suspension: We arbitrarily set the multiplication factors to two (2), which reflect our overall
                experience of the premium multiplication factor in such case.
            - number of claims: We arbitrarily set the multiplication factors as the following:
                - if 1 claim: 8% more (base factor).
                - if 2 claim: two time the base factor.
                - if 3 claims or more: three time the base factor.
                It reflects our overall experience of the claims effect on the premium but greatly simplified since
                it does not take into account the claim type and amount.

        Return:
            A premium for the protections that generate an increase in the premium.
        """

        liability_mu = self.liability_mu
        if protections.get("LiabilityCoverage") == 2000000:
            # Increase liability mu if 2 million protection amount
            liability_mu += self.liability_mu_increase

        mu_risk_factor = 1
        if insuree.sex in ("male", "homme"):
            mu_risk_factor *= 1.1597
        if insuree.suspension:
            mu_risk_factor *= 2
        if insuree.number_of_claims_past_years == 1:
            mu_risk_factor *= 1.08
        elif insuree.number_of_claims_past_years == 2:
            mu_risk_factor *= 1.16
        elif insuree.number_of_claims_past_years >= 3:
            mu_risk_factor *= 1.32

        protections_premiums = {}

        liability_coverage_premium = round(random.gauss(mu=liability_mu * mu_risk_factor, sigma=self.sigma))
        protections_premiums.update({"LiabilityCoveragePremium": liability_coverage_premium})

        property_damage_protections = protections.property_damage_protections()
        for key in property_damage_protections:
            mu = getattr(self, f"{change_to_snake_case(key)}_mu")
            premium = round(random.gauss(mu=mu * mu_risk_factor, sigma=self.sigma))

            protections_premiums.update({f"{key}Premium": premium})

        if protections.is_protected("FAQ20Coverage"):
            premium = round(random.gauss(mu=self.endorsement_20_mu * mu_risk_factor, sigma=self.sigma))
            protections_premiums.update({"FAQ20CoveragePremium": premium})
        if protections.is_protected("FAQ20ACoverage"):
            premium = round(random.gauss(mu=self.endorsement_20_mu * mu_risk_factor, sigma=self.sigma))
            protections_premiums.update({"FAQ20ACoveragePremium": premium})
        if protections.is_protected("FAQ33Coverage"):
            premium = round(random.gauss(mu=self.endorsement_33_mu * mu_risk_factor, sigma=self.sigma))
            protections_premiums.update({"FAQ33CoveragePremium": premium})
        if protections.is_protected("FAQ34Coverage"):
            premium = round(random.gauss(mu=self.endorsement_34_mu * mu_risk_factor, sigma=self.sigma))
            protections_premiums.update({"FAQ34CoveragePremium": premium})
        if protections.is_protected("FAQ34ABCoverage"):
            premium = round(random.gauss(mu=self.endorsement_34_mu * mu_risk_factor, sigma=self.sigma))
            protections_premiums.update({"FAQ34ABCoveragePremium": premium})
        if protections.is_protected("FAQ43Coverage"):
            premium = round(random.gauss(mu=self.endorsement_43_mu * mu_risk_factor, sigma=self.sigma))
            protections_premiums.update({"FAQ43CoveragePremium": premium})

        return Premium(**protections_premiums)

    def seed_instance(self, seed=42) -> None:
        """
        seed (int): The seed value to use for the generation seed. By default, 42.
        """
        super().seed_instance(seed)
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
