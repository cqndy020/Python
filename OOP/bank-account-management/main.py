"""Bank Account Management System"""

class Account:
    def __init__(self, account_number: float, account_holder, balance: float, type):
        assert balance >= 0, "The balance cannot be negative."

        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.type = type

    def view_balance(self):
        return f"Your balance: {self.balance}."
    
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def __str__(self):
        if Bank:
            print('New transaction occurs.')

    def adding_new_account(self, account):
        if self.account != self.name:
            self.accounts.append(account)
            print(f'Adding {self.account} successfully!')
        else:
            print(f'{self.account} is already exist.\nYou can remove or update your account.')

    def closing_account(self, account):
        pass

class Transaction:
    def __init__(self, transaction_type, amount):
        assert amount >= 0, "The amount should be more than or equal to 0."

        self.transaction_type = transaction_type
        self.amount = self.amount

    def display_transaction(self):
        return f"{self.transaction_type}  ${self.amount}"
