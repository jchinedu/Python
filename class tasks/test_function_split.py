import unittest
import split_function
class TestFunctionSplit(unittest.TestCase):
    def test_function_split_add_at_the_end_of_odd_letter(self):
        actual = split_function.function_split("joy","ce")
        self.assertEqual(actual, "joyce")

    def test_function_split_add_the_letter_at_the_middle_for_even_letters(self):
        actual = split_function.function_split("helloo","ce")
        self.assertEqual(actual, "helceloo")

    def test_the_function_collects_two_parameters(self):
        actual = split_function.function_split("joy","ce")