import unittest
import new_task

class TestNewTask(unittest.TestCase):
    def test_length_of_list(self):
        self.assertEqual(new_task.length_of_list([1, 2, 3]), 3)
        self.assertEqual(new_task.length_of_list([1, 2, 3, 4]), 4)
        self.assertEqual(new_task.length_of_list([1, 2, 3, 4, 5]), 5)

    def test_sum_elements_at_even_positions(self):
        self.assertEqual(new_task.sum_elements_at_even_positions([1, 2, 3]), 4)
        self.assertEqual(new_task.sum_elements_at_even_positions([1, 2, 3, 4]), 4)
        self.assertEqual(new_task.sum_elements_at_even_positions([1, 2, 3, 4, 5]), 9)
        self.assertEqual(new_task.sum_elements_at_even_positions([1, 2, 3, 4, 5]), 9)

    def test_sum_odd_elements_at_odd_positions(self):
        self.assertEqual(new_task.sum_odd_elements_at_odd_positions([1, 2, 3]), 2)
        self.assertEqual(new_task.sum_odd_elements_at_odd_positions([1, 2, 3, 4]), 6)
        self.assertEqual(new_task.sum_odd_elements_at_odd_positions([1, 2, 3, 4, 5]), 6)

    def test_multiply_all_elements_at_every_third_positions(self):
        self.assertEqual(new_task.multiply_all_elements_at_every_third_positions([1, 2, 3]), 3)
        self.assertEqual(new_task.multiply_all_elements_at_every_third_positions([1, 2, 3, 4]), 3)
        self.assertEqual(new_task.multiply_all_elements_at_every_third_positions([1, 2, 3, 4, 5]), 3)
        self.assertEqual(new_task.multiply_all_elements_at_every_third_positions([1, 2, 3, 4, 5, 6]), 18)

    def test_calculate_the_average_of_all_elements_in_the_list(self):
        self.assertEqual(new_task.calculate_the_average_of_all_elements_in_the_list([1, 2, 3]), 2)
        self.assertEqual(new_task.calculate_the_average_of_all_elements_in_the_list([1, 2, 3, 4]), 2.5)

