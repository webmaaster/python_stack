from bankAccount import BankAccount  

class User:
    def __init__(self):
        self.bankAccount = BankAccount()

    def make_deposit(self, amount):
        self.bankAccount.deposit(amount)

    def make_withdrawal(self, amount):
        self.bankAccount.withdraw(amount)

    def display_user_balance(self):
        self.bankAccount.display_account_info()