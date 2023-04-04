from ..config import NEW_PAGE_TAG


def generate_bill_text(self):
    text = ""
    if self.payment_method == "bill":
        text += (
            "INVOICING - Official receipt\n"
            "Personal Insurance\n"
            f"Customer number: {self.client_number}\n"
            f"Name and address of the insured\n"
            f"{self.insuree.name}\n"
            f"{self.insuree.address}\n"
            f"Payer's name: {self.insuree.name}\n"
            f"YOUR ACCOUNT STATUS - CASH ONLY\n"
            f"CLASS OF INSURANCE | POLICY NUMBER | CURRENT TRANSACTION | EFFECTIVE DATE | TRANSACTION TYPE "
            f"AMOUNT INCLUDING TAX | POLICY BALANCE | TOTAL\n"
            f"Automotive | 001 | | | BALANCE BEFORE TRANSACTION | | {self.premium.total}$ | {self.premium.total}$\n"
            f"Payable-Term in effect {self.premium.total}$\n"
            f"{NEW_PAGE_TAG}\n"
        )

    return text
