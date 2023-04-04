def change_to_snake_case(string: str) -> str:
    """
    Function to change a text in any case type (e.g. CamelCase) to snake_case.

    string (str): The string to convert to snake_case.

    Return:
        The string in snake_case.
    """
    return ''.join(['_' + i.lower() if i.isupper() else i for i in string]).lstrip('_')


def change_to_camel_case(string: str) -> str:
    """
    Function to change a text in any case type (e.g. snake_case) to CamelCase.

    string (str): The string to convert to CamelCase.

    Return:
        The string in CamelCase.
    """
    first, *others = string.split('_')
    return ''.join([first.capitalize(), *map(str.title, others)])
