from risc_generator import FPQ1Contract, Protections, Insuree, Vehicle
from tests.domain.contract.contract_base import ContractTestBase


class ContractClientAdvantagesTest(ContractTestBase):
    def setUp(self) -> None:
        self.a_protections = Protections(protections=self.a_dict_of_protections)

    def test_givenAFRContract_whenGenerateText_thenReturnProperFRText(self):
        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=self.a_suspension,
            number_of_claims_past_years=self.a_number_of_claims_past_years,
            association_rebate=False,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_bill_payment_method,
            protections=self.a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fpq1_contract.generate_client_advantages_text()

        a_insurer_name = "Assureur"
        a_website = "assureur.ca"
        a_mental_health_program_name = "MentalHealth"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "AVANTAGES CLIENT\n"
            f"Suivez-nous\n\n"
            f"Additionez les économies en regroupant "
            f"vos assurances chez nous! Visitez "
            f"{a_website} pour plus de détails.\n"
            f"Suivez-nous sur Facebook pour être "
            f"informé de nos concours et promotions!\n"
            f"(Facebook.com/{a_insurer_name}).\n"
            f"Visitez notre blogue {a_website} pour "
            f"obtenir une foule de rensignements utiles "
            f"liés au domaine de l'assurance et des "
            f"services financiers.\n"
            "Économies dont vous bénéficiez\n\n"
            f"Regroupez vos assurances à {a_insurer_name} et bénéficiez d'économies substantielles\n"
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
            "Votre assistance juridique\n\n"
            "\tService téléphonique de renseignements juridiques inclus gratuitement avec toute assurance.\n"
            "\tQuel que soit le problème, nos avocats membres du Barreau du Québec sont à l'écoute pour vous "
            "informer précisément sur vos droits. Confidentialité assurée.\n"
            "\tMunissez-vous d'une protection légale complète à peu de frais en ajoutant"
            " l'assurance protection juridique à vos protections. Appelez-nous pour obtenir les détails et profiter "
            "de ce privilège!\n"
            f"{a_new_page}\n"
            "AVANTAGES CLIENT\n"
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
            f"{a_insurer_name}.ca/{a_mental_health_program_name}.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractPreAuthorized_whenGenerateText_thenReturnProperFRText(self):
        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=self.a_suspension,
            number_of_claims_past_years=self.a_number_of_claims_past_years,
            association_rebate=False,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fpq1_contract.generate_client_advantages_text()

        a_insurer_name = "Assureur"
        a_website = "assureur.ca"
        a_mental_health_program_name = "MentalHealth"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "AVANTAGES CLIENT\n"
            f"Suivez-nous\n\n"
            f"Additionez les économies en regroupant "
            f"vos assurances chez nous! Visitez "
            f"{a_website} pour plus de détails.\n"
            f"Suivez-nous sur Facebook pour être "
            f"informé de nos concours et promotions!\n"
            f"(Facebook.com/{a_insurer_name}).\n"
            f"Visitez notre blogue {a_website} pour "
            f"obtenir une foule de rensignements utiles "
            f"liés au domaine de l'assurance et des "
            f"services financiers.\n"
            "Économies dont vous bénéficiez\n\n"
            "Rabais pour avoir choisi le Paiement pré-autorisé comme mode de paiement de votre prime\n"
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
            "Votre assistance juridique\n\n"
            "\tService téléphonique de renseignements juridiques inclus gratuitement avec toute assurance.\n"
            "\tQuel que soit le problème, nos avocats membres du Barreau du Québec sont à l'écoute pour vous "
            "informer précisément sur vos droits. Confidentialité assurée.\n"
            "\tMunissez-vous d'une protection légale complète à peu de frais en ajoutant"
            " l'assurance protection juridique à vos protections. Appelez-nous pour obtenir les détails et profiter "
            "de ce privilège!\n"
            f"{a_new_page}\n"
            "AVANTAGES CLIENT\n"
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
            f"{a_insurer_name}.ca/{a_mental_health_program_name}.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractWithRebateGroup_whenGenerateText_thenReturnProperFRText(self):
        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=self.a_suspension,
            number_of_claims_past_years=self.a_number_of_claims_past_years,
            association_rebate=True,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_bill_payment_method,
            protections=self.a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fpq1_contract.generate_client_advantages_text()

        a_insurer_name = "Assureur"
        a_website = "assureur.ca"
        a_mental_health_program_name = "MentalHealth"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "AVANTAGES CLIENT\n"
            f"Suivez-nous\n\n"
            f"Additionez les économies en regroupant "
            f"vos assurances chez nous! Visitez "
            f"{a_website} pour plus de détails.\n"
            f"Suivez-nous sur Facebook pour être "
            f"informé de nos concours et promotions!\n"
            f"(Facebook.com/{a_insurer_name}).\n"
            f"Visitez notre blogue {a_website} pour "
            f"obtenir une foule de rensignements utiles "
            f"liés au domaine de l'assurance et des "
            f"services financiers.\n"
            "Économies dont vous bénéficiez\n\n"
            "Rabais parce que vous êtes membre/client d'une association\n"
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
            "Votre assistance juridique\n\n"
            "\tService téléphonique de renseignements juridiques inclus gratuitement avec toute assurance.\n"
            "\tQuel que soit le problème, nos avocats membres du Barreau du Québec sont à l'écoute pour vous "
            "informer précisément sur vos droits. Confidentialité assurée.\n"
            "\tMunissez-vous d'une protection légale complète à peu de frais en ajoutant"
            " l'assurance protection juridique à vos protections. Appelez-nous pour obtenir les détails et profiter "
            "de ce privilège!\n"
            f"{a_new_page}\n"
            "AVANTAGES CLIENT\n"
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
            f"{a_insurer_name}.ca/{a_mental_health_program_name}.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractWithAnElectricCar_whenGenerateText_thenReturnProperFRText(self):
        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=self.a_suspension,
            number_of_claims_past_years=self.a_number_of_claims_past_years,
            association_rebate=False,
        )

        a_vehicle = Vehicle(
            year=self.a_year,
            make=self.a_maker,
            model=self.a_model,
            vin=self.a_vin,
            purchase_condition=self.a_purchase_condition,
            electric_vehicle=True,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=a_vehicle,
            payment_method=self.a_bill_payment_method,
            protections=self.a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fpq1_contract.generate_client_advantages_text()

        a_insurer_name = "Assureur"
        a_website = "assureur.ca"
        a_mental_health_program_name = "MentalHealth"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "AVANTAGES CLIENT\n"
            f"Suivez-nous\n\n"
            f"Additionez les économies en regroupant "
            f"vos assurances chez nous! Visitez "
            f"{a_website} pour plus de détails.\n"
            f"Suivez-nous sur Facebook pour être "
            f"informé de nos concours et promotions!\n"
            f"(Facebook.com/{a_insurer_name}).\n"
            f"Visitez notre blogue {a_website} pour "
            f"obtenir une foule de rensignements utiles "
            f"liés au domaine de l'assurance et des "
            f"services financiers.\n"
            "Économies dont vous bénéficiez\n\n"
            "Rabais pour un véhicule électrique\n"
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
            "Votre assistance juridique\n\n"
            "\tService téléphonique de renseignements juridiques inclus gratuitement avec toute assurance.\n"
            "\tQuel que soit le problème, nos avocats membres du Barreau du Québec sont à l'écoute pour vous "
            "informer précisément sur vos droits. Confidentialité assurée.\n"
            "\tMunissez-vous d'une protection légale complète à peu de frais en ajoutant"
            " l'assurance protection juridique à vos protections. Appelez-nous pour obtenir les détails et profiter "
            "de ce privilège!\n"
            f"{a_new_page}\n"
            "AVANTAGES CLIENT\n"
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
            f"{a_insurer_name}.ca/{a_mental_health_program_name}.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAFRContractWithAllRebates_whenGenerateText_thenReturnProperFRText(self):
        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=self.a_suspension,
            number_of_claims_past_years=self.a_number_of_claims_past_years,
            association_rebate=True,
        )

        a_vehicle = Vehicle(
            year=self.a_year,
            make=self.a_maker,
            model=self.a_model,
            vin=self.a_vin,
            purchase_condition=self.a_purchase_condition,
            electric_vehicle=True,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_fr_locale,
        )

        actual = fpq1_contract.generate_client_advantages_text()

        a_insurer_name = "Assureur"
        a_website = "assureur.ca"
        a_mental_health_program_name = "MentalHealth"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "AVANTAGES CLIENT\n"
            f"Suivez-nous\n\n"
            f"Additionez les économies en regroupant "
            f"vos assurances chez nous! Visitez "
            f"{a_website} pour plus de détails.\n"
            f"Suivez-nous sur Facebook pour être "
            f"informé de nos concours et promotions!\n"
            f"(Facebook.com/{a_insurer_name}).\n"
            f"Visitez notre blogue {a_website} pour "
            f"obtenir une foule de rensignements utiles "
            f"liés au domaine de l'assurance et des "
            f"services financiers.\n"
            "Économies dont vous bénéficiez\n\n"
            "Rabais pour avoir choisi le Paiement pré-autorisé comme mode de paiement de votre prime\n"
            "Rabais parce que vous êtes membre/client d'une association\n"
            "Rabais pour un véhicule électrique\n"
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
            "Votre assistance juridique\n\n"
            "\tService téléphonique de renseignements juridiques inclus gratuitement avec toute assurance.\n"
            "\tQuel que soit le problème, nos avocats membres du Barreau du Québec sont à l'écoute pour vous "
            "informer précisément sur vos droits. Confidentialité assurée.\n"
            "\tMunissez-vous d'une protection légale complète à peu de frais en ajoutant"
            " l'assurance protection juridique à vos protections. Appelez-nous pour obtenir les détails et profiter "
            "de ce privilège!\n"
            f"{a_new_page}\n"
            "AVANTAGES CLIENT\n"
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
            f"{a_insurer_name}.ca/{a_mental_health_program_name}.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContract_whenGenerateText_thenReturnProperENText(self):
        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=self.a_suspension,
            number_of_claims_past_years=self.a_number_of_claims_past_years,
            association_rebate=False,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_bill_payment_method,
            protections=self.a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = fpq1_contract.generate_client_advantages_text()

        a_insurer_name = "Assureur"
        a_website = "assureur.ca"
        a_mental_health_program_name = "MentalHealth"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "CLIENT ADVANTAGES\n"
            f"Follow us\n\n"
            f"Add up the savings by bundling your insurance with us! Visit "
            f"{a_website} for more information.\n"
            f"Follow us on Facebook to stay on top of our contests and promotions!\n"
            f"(Facebook.com/{a_insurer_name}).\n"
            f"Visit our Zone {a_website} blog  for a wealth of useful information on the "
            f"insurance industry and financial services.\n"
            "Your Saving\n\n"
            f"Group your insurance with {a_insurer_name} nd benefit from substantial savings\n"
            "Summary of Client Advantages\n\n"
            "Your auto insurance\n"
            "\tPrivileged rates for claim-free drivers.\n"
            "\tAutomatic coverage if you're driving a leased or borrowed vehicle, in Canada or the United States "
            "(the eligibility limit is specified in the Q.E.F. endorsement N 27 of your automobile insurance policy)."
            "\tRental costs for a replacement vehicle in the event of a covered loss: Q.E.F. endorsement N 20a of your "
            "insurance policy covers the reimbursement of automobile rental costs and, during a trip, "
            "additional living expenses incurred, following an insured loss that deprives you of your vehicle "
            "while repairs are being made.\n"
            "The available amounts are indicated in your insurance policy.\n"
            "\t$0 deductible in the event of a hit-and-run, a total loss or for a windshield repair.\n"
            "\tGet an additional 10% discount when you insure another vehicle (car, motorcycle, snowmobile, ATV, boat, "
            "caravan or motor home) and your residence with us.\n"
            "\tGet an additional 5% discount by insuring your home with us.\n"
            "Your legal assistance\n\n"
            "\tFree legal assistance over the telephone is included with all insurance plans.\n"
            "\tNo matter what the problem, our lawyers, all members of the Barreau du Québec, are there for you to "
            "inform you of your rights. Confidentiality is guaranteed.\n"
            "\tFor a low fee, protect yourself with comprehensive legal insurance by adding Legal Access Insurance to "
            "your coverages. Call us to get the details or to take advantage of this offer!\n"
            f"{a_new_page}\n"
            "CLIENT ADVANTAGES\n"
            "Summary of Client Advantages\n\n"
            "Our Claims Department\n"
            "\tSpeedy and fair claims process, at your disposal 24/7.\n"
            "\tIn the event of a loss involving more than one product that's insured with us, you pay a single "
            "deductible, the higher of the two.\n"
            "\tTo support your psychological well-being, we are pleased to offer you the free services of "
            "professionals to help you overcome the problems experienced following a loss. Totally confidential, "
            "this service is offered to all our insureds in the 12 months following a loss covered by an "
            f"individual insurance policy. For more information, visit "
            f"{a_insurer_name}.ca/{a_mental_health_program_name}.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractPreAuthorized_whenGenerateText_thenReturnProperENText(self):
        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=self.a_suspension,
            number_of_claims_past_years=self.a_number_of_claims_past_years,
            association_rebate=False,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = fpq1_contract.generate_client_advantages_text()

        a_insurer_name = "Assureur"
        a_website = "assureur.ca"
        a_mental_health_program_name = "MentalHealth"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "CLIENT ADVANTAGES\n"
            f"Follow us\n\n"
            f"Add up the savings by bundling your insurance with us! Visit "
            f"{a_website} for more information.\n"
            f"Follow us on Facebook to stay on top of our contests and promotions!\n"
            f"(Facebook.com/{a_insurer_name}).\n"
            f"Visit our Zone {a_website} blog  for a wealth of useful information on the "
            f"insurance industry and financial services.\n"
            "Your Saving\n\n"
            "Discount for choosing Pre-Authorized Payment as your premium payment method\n"
            "Summary of Client Advantages\n\n"
            "Your auto insurance\n"
            "\tPrivileged rates for claim-free drivers.\n"
            "\tAutomatic coverage if you're driving a leased or borrowed vehicle, in Canada or the United States "
            "(the eligibility limit is specified in the Q.E.F. endorsement N 27 of your automobile insurance policy)."
            "\tRental costs for a replacement vehicle in the event of a covered loss: Q.E.F. endorsement N 20a of your "
            "insurance policy covers the reimbursement of automobile rental costs and, during a trip, "
            "additional living expenses incurred, following an insured loss that deprives you of your vehicle "
            "while repairs are being made.\n"
            "The available amounts are indicated in your insurance policy.\n"
            "\t$0 deductible in the event of a hit-and-run, a total loss or for a windshield repair.\n"
            "\tGet an additional 10% discount when you insure another vehicle (car, motorcycle, snowmobile, ATV, boat, "
            "caravan or motor home) and your residence with us.\n"
            "\tGet an additional 5% discount by insuring your home with us.\n"
            "Your legal assistance\n\n"
            "\tFree legal assistance over the telephone is included with all insurance plans.\n"
            "\tNo matter what the problem, our lawyers, all members of the Barreau du Québec, are there for you to "
            "inform you of your rights. Confidentiality is guaranteed.\n"
            "\tFor a low fee, protect yourself with comprehensive legal insurance by adding Legal Access Insurance to "
            "your coverages. Call us to get the details or to take advantage of this offer!\n"
            f"{a_new_page}\n"
            "CLIENT ADVANTAGES\n"
            "Summary of Client Advantages\n\n"
            "Our Claims Department\n"
            "\tSpeedy and fair claims process, at your disposal 24/7.\n"
            "\tIn the event of a loss involving more than one product that's insured with us, you pay a single "
            "deductible, the higher of the two.\n"
            "\tTo support your psychological well-being, we are pleased to offer you the free services of "
            "professionals to help you overcome the problems experienced following a loss. Totally confidential, "
            "this service is offered to all our insureds in the 12 months following a loss covered by an "
            f"individual insurance policy. For more information, visit "
            f"{a_insurer_name}.ca/{a_mental_health_program_name}.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractWithRebateGroup_whenGenerateText_thenReturnProperENText(self):
        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=self.a_suspension,
            number_of_claims_past_years=self.a_number_of_claims_past_years,
            association_rebate=True,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=self.a_vehicle,
            payment_method=self.a_bill_payment_method,
            protections=self.a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = fpq1_contract.generate_client_advantages_text()

        a_insurer_name = "Assureur"
        a_website = "assureur.ca"
        a_mental_health_program_name = "MentalHealth"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "CLIENT ADVANTAGES\n"
            f"Follow us\n\n"
            f"Add up the savings by bundling your insurance with us! Visit "
            f"{a_website} for more information.\n"
            f"Follow us on Facebook to stay on top of our contests and promotions!\n"
            f"(Facebook.com/{a_insurer_name}).\n"
            f"Visit our Zone {a_website} blog  for a wealth of useful information on the "
            f"insurance industry and financial services.\n"
            "Your Saving\n\n"
            "Discount because you are a member/client of an association\n"
            "Summary of Client Advantages\n\n"
            "Your auto insurance\n"
            "\tPrivileged rates for claim-free drivers.\n"
            "\tAutomatic coverage if you're driving a leased or borrowed vehicle, in Canada or the United States "
            "(the eligibility limit is specified in the Q.E.F. endorsement N 27 of your automobile insurance policy)."
            "\tRental costs for a replacement vehicle in the event of a covered loss: Q.E.F. endorsement N 20a of your "
            "insurance policy covers the reimbursement of automobile rental costs and, during a trip, "
            "additional living expenses incurred, following an insured loss that deprives you of your vehicle "
            "while repairs are being made.\n"
            "The available amounts are indicated in your insurance policy.\n"
            "\t$0 deductible in the event of a hit-and-run, a total loss or for a windshield repair.\n"
            "\tGet an additional 10% discount when you insure another vehicle (car, motorcycle, snowmobile, ATV, boat, "
            "caravan or motor home) and your residence with us.\n"
            "\tGet an additional 5% discount by insuring your home with us.\n"
            "Your legal assistance\n\n"
            "\tFree legal assistance over the telephone is included with all insurance plans.\n"
            "\tNo matter what the problem, our lawyers, all members of the Barreau du Québec, are there for you to "
            "inform you of your rights. Confidentiality is guaranteed.\n"
            "\tFor a low fee, protect yourself with comprehensive legal insurance by adding Legal Access Insurance to "
            "your coverages. Call us to get the details or to take advantage of this offer!\n"
            f"{a_new_page}\n"
            "CLIENT ADVANTAGES\n"
            "Summary of Client Advantages\n\n"
            "Our Claims Department\n"
            "\tSpeedy and fair claims process, at your disposal 24/7.\n"
            "\tIn the event of a loss involving more than one product that's insured with us, you pay a single "
            "deductible, the higher of the two.\n"
            "\tTo support your psychological well-being, we are pleased to offer you the free services of "
            "professionals to help you overcome the problems experienced following a loss. Totally confidential, "
            "this service is offered to all our insureds in the 12 months following a loss covered by an "
            f"individual insurance policy. For more information, visit "
            f"{a_insurer_name}.ca/{a_mental_health_program_name}.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractWithAnElectricCar_whenGenerateText_thenReturnProperENText(self):
        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=self.a_suspension,
            number_of_claims_past_years=self.a_number_of_claims_past_years,
            association_rebate=False,
        )

        a_vehicle = Vehicle(
            year=self.a_year,
            make=self.a_maker,
            model=self.a_model,
            vin=self.a_vin,
            purchase_condition=self.a_purchase_condition,
            electric_vehicle=True,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=a_vehicle,
            payment_method=self.a_bill_payment_method,
            protections=self.a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = fpq1_contract.generate_client_advantages_text()

        a_insurer_name = "Assureur"
        a_website = "assureur.ca"
        a_mental_health_program_name = "MentalHealth"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "CLIENT ADVANTAGES\n"
            f"Follow us\n\n"
            f"Add up the savings by bundling your insurance with us! Visit "
            f"{a_website} for more information.\n"
            f"Follow us on Facebook to stay on top of our contests and promotions!\n"
            f"(Facebook.com/{a_insurer_name}).\n"
            f"Visit our Zone {a_website} blog  for a wealth of useful information on the "
            f"insurance industry and financial services.\n"
            "Your Saving\n\n"
            "Discount for an electric vehicle\n"
            "Summary of Client Advantages\n\n"
            "Your auto insurance\n"
            "\tPrivileged rates for claim-free drivers.\n"
            "\tAutomatic coverage if you're driving a leased or borrowed vehicle, in Canada or the United States "
            "(the eligibility limit is specified in the Q.E.F. endorsement N 27 of your automobile insurance policy)."
            "\tRental costs for a replacement vehicle in the event of a covered loss: Q.E.F. endorsement N 20a of your "
            "insurance policy covers the reimbursement of automobile rental costs and, during a trip, "
            "additional living expenses incurred, following an insured loss that deprives you of your vehicle "
            "while repairs are being made.\n"
            "The available amounts are indicated in your insurance policy.\n"
            "\t$0 deductible in the event of a hit-and-run, a total loss or for a windshield repair.\n"
            "\tGet an additional 10% discount when you insure another vehicle (car, motorcycle, snowmobile, ATV, boat, "
            "caravan or motor home) and your residence with us.\n"
            "\tGet an additional 5% discount by insuring your home with us.\n"
            "Your legal assistance\n\n"
            "\tFree legal assistance over the telephone is included with all insurance plans.\n"
            "\tNo matter what the problem, our lawyers, all members of the Barreau du Québec, are there for you to "
            "inform you of your rights. Confidentiality is guaranteed.\n"
            "\tFor a low fee, protect yourself with comprehensive legal insurance by adding Legal Access Insurance to "
            "your coverages. Call us to get the details or to take advantage of this offer!\n"
            f"{a_new_page}\n"
            "CLIENT ADVANTAGES\n"
            "Summary of Client Advantages\n\n"
            "Our Claims Department\n"
            "\tSpeedy and fair claims process, at your disposal 24/7.\n"
            "\tIn the event of a loss involving more than one product that's insured with us, you pay a single "
            "deductible, the higher of the two.\n"
            "\tTo support your psychological well-being, we are pleased to offer you the free services of "
            "professionals to help you overcome the problems experienced following a loss. Totally confidential, "
            "this service is offered to all our insureds in the 12 months following a loss covered by an "
            f"individual insurance policy. For more information, visit "
            f"{a_insurer_name}.ca/{a_mental_health_program_name}.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)

    def test_givenAENContractWithAllRebates_whenGenerateText_thenReturnProperENText(self):
        a_insuree = Insuree(
            sex=self.a_sex,
            name=self.a_name,
            birth_date=self.a_date_of_birth,
            address=self.an_address,
            suspension=self.a_suspension,
            number_of_claims_past_years=self.a_number_of_claims_past_years,
            association_rebate=True,
        )

        a_vehicle = Vehicle(
            year=self.a_year,
            make=self.a_maker,
            model=self.a_model,
            vin=self.a_vin,
            purchase_condition=self.a_purchase_condition,
            electric_vehicle=True,
        )

        fpq1_contract = FPQ1Contract(
            client_number=self.a_client_number,
            contract_start_date=self.a_contract_start_date,
            insuree=a_insuree,
            vehicle=a_vehicle,
            payment_method=self.a_pre_authorize_payment_method,
            protections=self.a_protections,
            premium=self.a_premium_mock,
            financing=self.a_creditor,
            locale=self.a_en_locale,
        )

        actual = fpq1_contract.generate_client_advantages_text()

        a_insurer_name = "Assureur"
        a_website = "assureur.ca"
        a_mental_health_program_name = "MentalHealth"
        a_new_page = "<###NEW_PAGE###>"

        expected = (
            "CLIENT ADVANTAGES\n"
            f"Follow us\n\n"
            f"Add up the savings by bundling your insurance with us! Visit "
            f"{a_website} for more information.\n"
            f"Follow us on Facebook to stay on top of our contests and promotions!\n"
            f"(Facebook.com/{a_insurer_name}).\n"
            f"Visit our Zone {a_website} blog  for a wealth of useful information on the "
            f"insurance industry and financial services.\n"
            "Your Saving\n\n"
            "Discount for choosing Pre-Authorized Payment as your premium payment method\n"
            "Discount because you are a member/client of an association\n"
            "Discount for an electric vehicle\n"
            "Summary of Client Advantages\n\n"
            "Your auto insurance\n"
            "\tPrivileged rates for claim-free drivers.\n"
            "\tAutomatic coverage if you're driving a leased or borrowed vehicle, in Canada or the United States "
            "(the eligibility limit is specified in the Q.E.F. endorsement N 27 of your automobile insurance policy)."
            "\tRental costs for a replacement vehicle in the event of a covered loss: Q.E.F. endorsement N 20a of your "
            "insurance policy covers the reimbursement of automobile rental costs and, during a trip, "
            "additional living expenses incurred, following an insured loss that deprives you of your vehicle "
            "while repairs are being made.\n"
            "The available amounts are indicated in your insurance policy.\n"
            "\t$0 deductible in the event of a hit-and-run, a total loss or for a windshield repair.\n"
            "\tGet an additional 10% discount when you insure another vehicle (car, motorcycle, snowmobile, ATV, boat, "
            "caravan or motor home) and your residence with us.\n"
            "\tGet an additional 5% discount by insuring your home with us.\n"
            "Your legal assistance\n\n"
            "\tFree legal assistance over the telephone is included with all insurance plans.\n"
            "\tNo matter what the problem, our lawyers, all members of the Barreau du Québec, are there for you to "
            "inform you of your rights. Confidentiality is guaranteed.\n"
            "\tFor a low fee, protect yourself with comprehensive legal insurance by adding Legal Access Insurance to "
            "your coverages. Call us to get the details or to take advantage of this offer!\n"
            f"{a_new_page}\n"
            "CLIENT ADVANTAGES\n"
            "Summary of Client Advantages\n\n"
            "Our Claims Department\n"
            "\tSpeedy and fair claims process, at your disposal 24/7.\n"
            "\tIn the event of a loss involving more than one product that's insured with us, you pay a single "
            "deductible, the higher of the two.\n"
            "\tTo support your psychological well-being, we are pleased to offer you the free services of "
            "professionals to help you overcome the problems experienced following a loss. Totally confidential, "
            "this service is offered to all our insureds in the 12 months following a loss covered by an "
            f"individual insurance policy. For more information, visit "
            f"{a_insurer_name}.ca/{a_mental_health_program_name}.\n"
            f"{a_new_page}\n"
        )

        self.assertEqual(expected, actual)
