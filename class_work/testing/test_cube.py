import cube
from unittest import TestCase
class TestCube(TestCase):
	def test_that_get_cube_function_exists(self):
		cube.get_cube(3)

	def test_that_cube_function_return_correct_answer(self):
		actual = cube.get_cube(10)
		expected = 1000
		self.assertEqual(actual, expected)
		actual = cube.get_cube(5)
		expected = 125
		self.assertEqual(actual, expected)

	def test_that_get_cube_function_work_for_number_between_1_to_10(self): 
		self.assertRaises(ValueError,cube.get_cube, 40)
		self.assertRaises(ValueError,cube.get_cube, 0 )

	def test_that_get_cube_function_raises_value_error_with_value(self):
		self.assertRaises(ValueError, cube.get_cube, -12)
