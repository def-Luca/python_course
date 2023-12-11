"""we run the test from terminal in the folder by writing python .\folder_name.py"""
"""we can use the same class to test multiple functions"""
import unittest
from o_function_def import o_return, string_counter


class FunctionTestCase(unittest.TestCase):
    def test_o_return(self):
        # compare the result we expect to get
        expected_result = ["country", "power", "jOurnal"]
        # with the result you get with the function
        actual_result = o_return(*["country", "power", "java", "mackerel", "jOurnal"])
        self.assertIsInstance(actual_result, list)
        self.assertEqual(expected_result, actual_result)
        # we use assert syntaxe to check what we are interested in

    def test_string_counter(self):
        input_string = "Hello Pythonistas"
        expected_output = {"lower": 15, "upper": 2}

        actual_result = string_counter(input_string)
        self.assertIsInstance(actual_result, dict)
        # we expect the result to be a dict
        self.assertEqual(actual_result, expected_output)
        # we expect the results to be equal
# so basically we wrote first the test and now we write the function

if __name__ == "__main__":
    print("greeting from test module")
    unittest.main()  # standard syntax for writing the tests
