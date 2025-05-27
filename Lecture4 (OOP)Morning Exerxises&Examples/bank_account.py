# Real World Scenarios or Problems.

# Bank Accounts: Saving account and current account inherit from bank Account

# deposit, withdraw, display balance, types of accounts

# Super class
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}. New balance: {self.balance}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Withdrew {amount}. New balance: {self.balance}')

        else:
            print('Insufficient funds. ')

    def display_balance(self):
        print(f'Account {self.account_number} Balance: {self.balance}')


# subclass : Saving account
class SavingAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)

        self.interest_rate = interest_rate  # Store the interest rate

    # Add new method for interest rate calculation
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        # Add the interest
        self.balance += interest
        print(f'Interest of {interest} added. New balance: {self.balance}')


# Child class : Current account
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit  # Store overdraft

        # Override withdraw method to allow overdraft

        def withdraw(self, amount):
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                print(f'Withdrew {amount}. New balance: {self.balance}')

            else:
                print('Exceeded the overdraft limit.')


# Create objects

saving = SavingAccount('SAV0555555', 100000, 5)
current = CurrentAccount('CUR0577777', 50000, 10)

# Test Method display
saving.display_balance()
saving.add_interest()
saving.withdraw(20000)
print(' LB ____________________')

current.display_balance()
current.withdraw(70000)
current.withdraw(45000)
