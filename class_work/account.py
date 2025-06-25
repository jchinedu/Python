class Account:
    def __init__(self, first_name, last_name, balance = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            return self.balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance

oba = Account("John", "Smith")
oba.deposit(10000)
oba.withdraw(1000)
oba.withdraw(100)
print(oba.balance)