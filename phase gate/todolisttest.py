import todolist
from unittest import TestCase

class Testtodolist(TestCase):
    def test_that_wait_for_go_back_function_exists(self):
     todolist.wait_for_go_back()
    def test_that_add_a_task_function_exists(self):
     todolist.add_a_task()
    def test_that_add_a_task_function_work_for_number_between_0_to_1(self):
     self.assertRaises(ValueError,todolist.add_a_task(), 40)
     self.assertRaises(ValueError,todolist.add_a_task())

       
           	
