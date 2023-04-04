from ..config import NEW_PAGE_TAG


def generate_bill_text(self):
    text = ""
    if self.payment_method == "facture":
        text += (
            "FACTURATION - Reçu officiel\n"
            "Assurance des particuliers\n"
            f"Numéro client : {self.client_number}\n"
            f"Nom et adresse de l'assuré\n"
            f"{self.insuree.name}\n"
            f"{self.insuree.address}\n"
            f"Nom du payeur : {self.insuree.name}\n"
            f"ÉTAT DE VOTRE COMPTE - MODE DE PAIEMENT COMPTANT SEULEMENT\n"
            f"CATÉGORIE D'ASSURANCE | N POLICE | TRANSACTION ACTUELLE | PRISE D'EFFET | TYPE DE TRANSACTION | "
            f"MONTANT INCLUANT TAXE | SOLDE DE LA POLICE | TOTAL\n"
            f"Automobile | 001 | | | SOLDE AVANT TRANSACTION | | {self.premium.total}$ | {self.premium.total}$\n"
            f"À payer-terme en vigueur {self.premium.total}$\n"
            f"{NEW_PAGE_TAG}\n"
        )

    return text
