"""Bank Account Management System"""

class Account:
    def __init__(self, account_number: float, account_holder, balance: float, type):
        assert balance >= 0, "The balance cannot be negative."

        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.type = type

    
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def adding_new_account(self, account):
        if self.account != self.name:
            self.accounts.append(account)
            print(f'Adding {self.account} successfully!')
        else:
            print(f'{self.account} is already exist.\nYou can remove or update your account.')
