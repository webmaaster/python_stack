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

#Chaining methodcd ..

user1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(515).display_user_balance()
user2.make_deposit(200).make_deposit(201).make_withdrawal(300).make_withdrawal(50).display_user_balance()
user3.make_deposit(550).make_withdrawal(50).make_withdrawal(120).make_withdrawal(110).display_user_balance()

user1.transfer_money(user3, 25).display_user_balance()
user3.display_user_balance()