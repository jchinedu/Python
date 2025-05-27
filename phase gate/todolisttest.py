import todolist
from unittest import TestCase

class Testtodolist(TestCase):
    def test_that_wait_for_go_back_function_exists(self):
     todolist.wait_for_go_back()
    def test_that_add_a_task_function_exists(self):
     todolist.add_a_task()
    def test_that_add_a_task_function_returns_correct_answer(self):
     actual = todolist.add_a_task()
     expected =None
     self.assertEqual(actual, expected)
    def test_that_view_task_function_exists(self):
     todolist.view_task()
    #def test_that_mark_a_task_as_complete_function_exists(self):
    #mark_a_task_as_complete()
    def test_that_delete_a_task_function_exist(self):
     Delete_a_task()


       
           	
