from ..config import FAKE_INSURER_WEBSITE, FAKE_INSURER_NAME, NEW_PAGE_TAG, FAKE_MENTAL_HEALTH_PROGRAM_NAME


def generate_client_advantages_text(self) -> str:
    text = (
        "CLIENT ADVANTAGES\n"
        f"Follow us\n\n"
        f"Add up the savings by bundling your insurance with us! Visit "
        f"{FAKE_INSURER_WEBSITE} for more information.\n"
        f"Follow us on Facebook to stay on top of our contests and promotions!\n"
        f"(Facebook.com/{FAKE_INSURER_NAME}).\n"
        f"Visit our Zone {FAKE_INSURER_WEBSITE} blog  for a wealth of useful information on the "
        f"insurance industry and financial services.\n"
    )

    text += "Your Saving\n\n"
    rebate_text = ""

    # No multi-product case to deal with as the dataset is composed just of new customer with a single car on
    # the contract and single product.
    if self.payment_method == "pre-authorize":
        rebate_text += "Discount for choosing Pre-Authorized Payment as your premium payment method\n"
    if self.insuree.insuree_is_in_a_rebate_group():
        rebate_text += "Discount because you are a member/client of an association\n"
    if self.vehicle.is_electric():
        rebate_text += "Discount for an electric vehicle\n"
    if rebate_text == "":
        # Case for no rebate
        rebate_text += f"Group your insurance with {FAKE_INSURER_NAME} nd benefit from substantial savings\n"

    text += rebate_text

    text += (
        "Summary of Client Advantages\n\n"
        "Your auto insurance\n"
        "\tPrivileged rates for claim-free drivers.\n"
        "\tAutomatic coverage if you're driving a leased or borrowed vehicle, in Canada or the United States "
        "(the eligibility limit is specified in the Q.E.F. endorsement N 27 of your automobile insurance policy)."
        "\tRental costs for a replacement vehicle in the event of a covered loss: Q.E.F. endorsement N 20a of your "
        "insurance policy covers the reimbursement of automobile rental costs and, during a trip, additional living "
        "expenses incurred, following an insured loss that deprives you of your vehicle while repairs are being made.\n"
        "The available amounts are indicated in your insurance policy.\n"
        "\t$0 deductible in the event of a hit-and-run, a total loss or for a windshield repair.\n"
        "\tGet an additional 10% discount when you insure another vehicle (car, motorcycle, snowmobile, ATV, boat, "
        "caravan or motor home) and your residence with us.\n"
        "\tGet an additional 5% discount by insuring your home with us.\n"
    )

    text += (
        "Your legal assistance\n\n"
        "\tFree legal assistance over the telephone is included with all insurance plans.\n"
        "\tNo matter what the problem, our lawyers, all members of the Barreau du Québec, are there for you to "
        "inform you of your rights. Confidentiality is guaranteed.\n"
        "\tFor a low fee, protect yourself with comprehensive legal insurance by adding Legal Access Insurance to "
        "your coverages. Call us to get the details or to take advantage of this offer!\n"
    )

    text += NEW_PAGE_TAG + "\n"
    text += "CLIENT ADVANTAGES\n"

    text += (
        "Summary of Client Advantages\n\n"
        "Our Claims Department\n"
        "\tSpeedy and fair claims process, at your disposal 24/7.\n"
        "\tIn the event of a loss involving more than one product that's insured with us, you pay a single "
        "deductible, the higher of the two.\n"
        "\tTo support your psychological well-being, we are pleased to offer you the free services of professionals "
        "to help you overcome the problems experienced following a loss. Totally confidential, this service is "
        "offered to all our insureds in the 12 months following a loss covered by an individual insurance policy. "
        f"For more information, visit {FAKE_INSURER_NAME}.ca/{FAKE_MENTAL_HEALTH_PROGRAM_NAME}.\n"
    )

    text += NEW_PAGE_TAG + "\n"

    return text
