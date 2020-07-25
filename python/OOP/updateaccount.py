from account import BankAccount  

class User:
    def __init__(self):
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        self.account.display_account_info()