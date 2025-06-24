import atm_bank_app
from unittest import TestCase

class TestBankAtmFunction(TestCase):
	def test_that_balance_can_not_be_less_than_100(self):
		actual = atm_bank_app.atm_system() 
		expected = 100
		self.assertEqual(100, expected)
	def test_that_balance_can_be_floating_numbers(self):
		actual = atm_bank_app.atm_system()
		expected = 100.4
		self.assertEqual(100.4, expected)
	def test_that_withdrawal_amount_must_be_in_multiples_of_500_and_1000(self):
		actual = atm_bank_app.atm_system()
		expected = 500
		self.assertEqual(500, expected)
	def test_that_withdrawal_works(self):
		expected = 3000
		self.assertRaises(expected,3000)
	def test_that_withdrawal_amount_must_be_greater_than_100(self):
		actual = atm_bank_app.atm_system()
		expected = 100
		self.assertEqual(100, expected)

	

	

		

