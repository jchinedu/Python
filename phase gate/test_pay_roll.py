import pay_roll
from unittest import TestCase

class PayRollFunction(TestCase):
	def test_that_the_menu_function_exists(self):
		pay_roll.print_menu()

	def test_that_the_add_employee_function_exists(self):
		pay_roll.add_employee()

	def test_that_the_view_employee_function_exists(self):
		pay_roll.view_employees()

	def test_that_the_update_employee_function_exists(self):
		pay_roll.update_employee()




		
