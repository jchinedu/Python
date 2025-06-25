from unittest import TestCase
import account 
class BankTest(TestCase):

	def test_create_account_function_exist(self):
        	account.create_account("alice", "1234567890")
        	

	def test_create_account_success(self):
		account.create_account("johnny","08161237898")
		self.assertEqual(2, len(account.accounts))

	def test_that_name_of_account_exist(self):
        	account1 = account.create_account("johnny", "1234567890")
        	self.assertTrue("johnny", account1[0])

	def test_name_can_be_found(self):
		account.get_name()

	def test_that_number_of_account_exist(self):
        	account1 = account.create_account("johnny", "1234567890")
        	self.assertTrue("1234567890", account1[1])

	def test_deposit_function_exist(self):
        	account.deposit("john", 1,800)
        
	def test_deposit_cannot_be_less_than_zero(self):
		account.deposit("john", -1000, 700)

	def test_deposit_zero_amount(self):
        	self.assertIsNone(account.deposit("john", 0, 700))

	def test_deposit_float_amount(self):
    		account.deposit("john", 50.25,800)

	def test_name_is_available_on_deposit(self):
		account.deposit("john", 5000, 900)

	def test_the_withdraw_function_exist(self):
        	account.withdraw("alice", 100, 500)
	
	def test_withdraw_success(self):
        	account.create_account("john", "1234567890")
        	new_balance = account.withdraw("john", 200, 500)
        	self.assertEqual(new_balance, 300)
	def test_withdraw_insufficient_funds(self):
		account.create_account("john", "1234567890") 
		with self.assertRaises(ValueError) as context:
			account.withdraw("john", 200, 100)
		self.assertIn("Insufficient funds", str(context.exception))

	def test_withdraw_negative_amount(self):
       		account.create_account("john", "1234567890")
        	with self.assertRaises(ValueError) as context:
            		account.withdraw("john", -50, 100)
        	self.assertIn("Withdrawal amount must be positive", str(context.exception))
	def test_withdraw_account_not_found(self):
        	with self.assertRaises(ValueError) as context:
            		account.withdraw("ghost", 100, 500)
        	self.assertIn("Account not found", str(context.exception))

	def test_withdraw_negative_amount(self):
        	account.create_account("john", "1234567890")
        	with self.assertRaises(ValueError) as context:
           		account.withdraw("john", -50, 100)
        	self.assertIn("Withdrawal amount must be positive", str(context.exception))

	def test_withdraw_negative(self):
        	account.create_account("mary", "1234567890")
        	with self.assertRaises(ValueError):
            		account.withdraw("mary", -30, 300)

	def test_withdraw_exact_balance(self):
        	account.create_account("jane", "2222222222")
        	new_balance = account.withdraw("jane", 300, 300)
        	self.assertEqual(new_balance, 0)

	def test_withdraw_account_not_found(self):
        	with self.assertRaises(ValueError) as context:
            		account.withdraw("ghost", 50, 100)
        	self.assertIn("Account not found", str(context.exception))

	def test_withdraw_float_amount(self):
        	account.create_account("mike", "6666666666", 1000.0)
        	new_balance = account.withdraw("mike", 99.99, 1000.0)
        	self.assertAlmostEqual(new_balance, 900.01)

	def test_get_all_customers_returns_accounts(self):
        	account.create_account("Alice", "1234567890")
        	account.create_account("Bob", "0987654321")
        	customers = account.get_all_customers()
        	self.assertEqual(len(customers), 7)
        	self.assertIn(["Alice", "1234567890"], customers)
        	self.assertIn(["Bob", "0987654321"], customers)

	def test_find_customer_by_name(self):
        	account.create_account("Charlie", "1112223333")
        	result = account.find_customer("Charlie", "1112223333" )
        	self.assertEqual(result, ["Charlie", "1112223333"])

	def test_find_customer_by_phone(self):
        	account.create_account("Dana", "4445556666")
        	result = account.find_customer("Dana", "4445556666")
        	self.assertEqual(result, ["Dana", "4445556666"])

	def test_find_customer_by_both_name_and_phone(self):
		account.create_account("onoja", "9072290338")
		result = account.find_customer("onoja","9072290338")
		self.assertEqual(result, ["onoja","9072290338"])
	

	
	
			
		
	
