import unittest
import account

class TestAccount(unittest.TestCase):
    def test_that_accounts_can_be_created(self):
        oba = account.Account("John", "Smith")
    def test_that_account_can_withdraw(self):
        self.assertEqual(account.Account("John", "Smith").withdraw(100), -100)
        self.assertEqual(account.Account("John", "Smith").withdraw(1000), -1000)
        self.assertEqual(account.Account("John", "Smith").withdraw(1000), -1000)

    def test_that_account_can_deposit(self):
        self.assertEqual(account.Account("John", "Smith").deposit(100), 100)
        self.assertEqual(account.Account("John", "Smith").deposit(1000), 1000)
        self.assertEqual(account.Account("John", "Smith").deposit(1000), 1000)