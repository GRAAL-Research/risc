from ..config import FAKE_INSURER_WEBSITE, FAKE_INSURER_NAME, NEW_PAGE_TAG, FAKE_MENTAL_HEALTH_PROGRAM_NAME


def generate_client_advantages_text(self) -> str:
    text = (
        "AVANTAGES CLIENT\n"
        f"Suivez-nous\n\n"
        f"Additionez les économies en regroupant "
        f"vos assurances chez nous! Visitez "
        f"{FAKE_INSURER_WEBSITE} pour plus de détails.\n"
        f"Suivez-nous sur Facebook pour être "
        f"informé de nos concours et promotions!\n"
        f"(Facebook.com/{FAKE_INSURER_NAME}).\n"
        f"Visitez notre blogue {FAKE_INSURER_WEBSITE} pour "
        f"obtenir une foule de rensignements utiles "
        f"liés au domaine de l'assurance et des "
        f"services financiers.\n"
    )

    text += "Économies dont vous bénéficiez\n\n"
    rebate_text = ""

    # No multi-product case to deal with as the dataset is composed just of new customer with a single car on
    # the contract and single product.
    if self.payment_method == "pre-authorize":
        rebate_text += "Rabais pour avoir choisi le Paiement pré-autorisé comme mode de paiement de votre prime\n"
    if self.insuree.insuree_is_in_a_rebate_group():
        rebate_text += "Rabais parce que vous êtes membre/client d'une association\n"
    if self.vehicle.is_electric():
        rebate_text += "Rabais pour un véhicule électrique\n"
    if rebate_text == "":
        # Case for no rebate
        rebate_text += f"Regroupez vos assurances à {FAKE_INSURER_NAME} et bénéficiez d'économies substantielles\n"

    text += rebate_text

    text += (
        "Rappel des avantages clients\n\n"
        "Votre assurance auto\n"
        "\tTarification privilégiée pour les conducteurs sans réclamation.\n"
        "\tCouverture automatique si vous conduisez un véhicule loué ou emprunté; au "
        "Canada ou aux États-Unis (la limite admissible est précisée à la garantie "
        "F.A.Q. N 27 de votre police d'assurance automobile).\n"
        "\tLocation d'un véhicule de remplacement en cas de sinistre couvert : l'avenant "
        "F.A.Q. N 20a de votre police d'assurance couvre notamment les frais de location d'une automobile et, "
        "en cours de voyage, les frais supplémentaires de subsistance encourus à la suite d'un sinistre couvert"
        " vous privant de votre véhicule pendant la réparation. Les montants disponibles sont indiqués dans "
        "votre police d'assurance.\n"
        "\t0 $ de franchise en cas de délit de fuite, de perte totale ou de réparation de pare-brise.\n"
        "\tObtenez 10 % de rabais supplémentaire en assurant un autre véhicule "
        "(auto, moto, motoneige, quad, bateau, caravane ou autocaravane) et votre résidence chez nous.\n"
        "\tObtenez 5 % de rabais supplémentaire en assurant aussi votre résidence chez nous.\n"
    )

    text += (
        "Votre assistance juridique\n\n"
        "\tService téléphonique de renseignements juridiques inclus gratuitement avec toute assurance.\n"
        "\tQuel que soit le problème, nos avocats membres du Barreau du Québec sont à l'écoute pour vous "
        "informer précisément sur vos droits. Confidentialité assurée.\n"
        "\tMunissez-vous d'une protection légale complète à peu de frais en ajoutant"
        " l'assurance protection juridique à vos protections. Appelez-nous pour obtenir les détails et profiter "
        "de ce privilège!\n"
    )

    text += NEW_PAGE_TAG + "\n"
    text += "AVANTAGES CLIENT\n"

    text += (
        "Rappel des avantages clients\n\n"
        "Indemnisation\n"
        "\tService d'indemnisation rapide et équitable, disponible 24 h sur 24, 7 jours sur 7.\n"
        "\tSi un sinistre touche plus d'un produit assuré avec nous, vous n'aurez qu'une seule "
        "franchise à payer, soit la plus élevée des deux.\n"
        "\tAfin de protéger votre santé psychologique, nous sommes heureux de vous offrir "
        "gratuitement les services professionnels pour vous aider à surmonter les difficultés découlant d'un "
        "sinistre.\n"
        "Totalement confidentiel, ce service est offert à tous nos assurés dans les 12 mois suivant un sinistre "
        f"couvert touchant une police d'assurance des particuliers. Pour tous les détails, visitez "
        f"{FAKE_INSURER_NAME}.ca/{FAKE_MENTAL_HEALTH_PROGRAM_NAME}.\n"
    )

    text += NEW_PAGE_TAG + "\n"

    return text
