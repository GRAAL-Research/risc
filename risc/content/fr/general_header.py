def generate_general_pages_header_text(policy_number: str) -> str:
    header_template = (
        "POLICE D'ASSURANCE AUTOMOBILE DU QUÉBEC\n"
        "F.P.Q. N 1 - FORMULAIRE DES PROPRIÉTAIRES\n"
        f"Numéro de police : {policy_number}\n\n"
    )
    return header_template
