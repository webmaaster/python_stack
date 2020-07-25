class BankAccount:
    def __init__(self):
        self.interest_rate = 0.5
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)

    def yield_interest(self):
        self.balance += (self.balance * self.interest_rate)
        return self


if __name__ == "__main__":
    account1 = BankAccount()
    account2 = BankAccount()

    account1.deposit(1000).deposit(500).deposit(250).withdraw(150).yield_interest().display_account_info()
    account2.deposit(1000).deposit(200).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()