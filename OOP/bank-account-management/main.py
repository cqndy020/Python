"""
Bank Account Management System
*Bank*== bank name, creating/closing bank account, deposit/withdrawal
*account*== account number, account name, account type

Account type: Savings / Checking
"""

class Account:
    def __init__(self, account_number: float, account_holder, type):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0
        self.type = type
        self.transactions = []

    def view_balance(self):
        return f"Your balance: {self.balance}."
    
    def display_account_info(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: {self.balance}\nAccount Type: {self.type}"
    
    def deposit(self, amount:float):
        assert amount >= 0, 'The amount should be positive'

        self.balance += amount
        self.transactions.append(Transaction('Deposit', amount))
    
    def withdraw(self, amount:float):
        assert amount >=0, 'The amount should be positive'

        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction('Withdrawal', amount))
        else:
            print(f'You can only withdraw: ${self.balance}')

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def __str__(self):
        if Bank:
            print('New transaction occurs.')

    def create_account(self, account_number, account_holder, type):
        account = Account(account_number, account_holder, type)
        self.accounts.append(account)
        return account
    
    def close_account(self, account):
        self.accounts.remove(account)

    def display_accounts(self):
        for account in self.accounts:
            print(account.display_account_info())
            print("=" * 20)

    def perform_transaction(self, account, transaction_type, amount):
        if transaction_type == 'Deposit':
            account.deposit(amount)
            print('Deposit successfully!')

        elif transaction_type == 'Withdrawal':
            account.withdraw(amount)
            print('Withdraw successfully!')
            
        else:
            print("Transaction could only deposit and withdraw.\nTo deposit: Type 'Deposit'\nTo Withdraw: Type 'Withdrawal'")

class Transaction:
    def __init__(self, transaction_type, amount:float):
        assert amount >= 0, "The amount should be more than or equal to 0."

        self.transaction_type = transaction_type
        self.amount = amount

    def display_transaction(self):
        return f"{self.transaction_type}  ${self.amount}"

bank = Bank('KBZ')

acc1 = bank.create_account('12345', 'Alice', 'Savings')
acc2 = bank.create_account('56789', 'Bob', 'Checking')

acc1.deposit(100.0)

bank.perform_transaction(acc1, 'withdrawal', 55)
