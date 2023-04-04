from unittest import TestCase

from risc_generator import change_to_snake_case, change_to_camel_case


class ContractFakerToolsTest(TestCase):
    def test_givenACamelCaseString_whenChangeToSnakeCase_thenReturnSnakeCaseString(self):
        camel_case_string = "CamelCaseString"

        expected = "camel_case_string"
        actual = change_to_snake_case(camel_case_string)

        self.assertEqual(expected, actual)

        camel_case_string = "CamelCaseString2"

        expected = "camel_case_string2"
        actual = change_to_snake_case(camel_case_string)

        self.assertEqual(expected, actual)

    def test_givenASnakeCaseString_whenChangeToCamelCase_thenReturnCamelCaseString(self):
        camel_case_string = "camel_case_string"

        expected = "CamelCaseString"
        actual = change_to_camel_case(camel_case_string)

        self.assertEqual(expected, actual)

        camel_case_string = "camel_case_string2"

        expected = "CamelCaseString2"
        actual = change_to_camel_case(camel_case_string)

        self.assertEqual(expected, actual)
