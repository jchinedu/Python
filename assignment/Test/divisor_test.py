import divisor_1
from unittest import TestCase

class TestDivisorFunction(TestCase):
    def test_that_division_function_exists(self):
        result = divisor_1.divisor([10, 3, 4, 2, 5], 2)
        self.assertEqual(result, [10, 4, 2])

    def test_that_division_function_parameters_exists(self):
        result = divisor_1.divisor([10, 3, 4, 2, 5], 5)
        self.assertEqual(result, [10, 5])
   
    def test_return_list_of_numbers(self):
        result = divisor_1.divisor([9,3,6,18,50,49], 3)
        self.assertEqual(result, [9,3,6,18])
	
   