class User:
  def __init__(self):
    self.balance = 0
 
  def make_deposit(self, amount):
    self.balance += amount
    return self

  def make_withdrawal(self, amount):
    self.balance -= amount
    return self

  def display_user_balance(self):
    print(self.balance)
    return self

  def transfer_money(self, another_user_object, amount):
    self.make_withdrawal(amount)
    another_user_object.make_deposit(amount)
    return self

user1 = User()
user2 = User()
user3 = User()

user1.make_deposit(100)
user1.make_deposit(200)
user1.make_deposit(300)
user1.make_withdrawal(515)
user1.display_user_balance()

user2.make_deposit(200)
user2.make_deposit(201)
user2.make_withdrawal(300)
user2.make_withdrawal(50)
user2.display_user_balance()

user3.make_deposit(550)
user3.make_withdrawal(50)
user3.make_withdrawal(120)
user3.make_withdrawal(110)
user3.display_user_balance()

user1.transfer_money(user3, 25)
user1.display_user_balance()
user3.display_user_balance()