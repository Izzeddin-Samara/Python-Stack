# user.py

class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance:.2f}")
        return self

    def transfer_money(self, other_user, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_user.make_deposit(amount)
        else:
            print("Insufficient funds")
        return self

# Create instances of the User class
user1 = User("Ahmad")
user2 = User("Omar")
user3 = User("Ali")

# Operations for the first user
user1.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(75).display_user_balance()

# Operations for the second user
user2.make_deposit(300).make_deposit(150).make_withdrawal(100).make_withdrawal(50).display_user_balance()

# Operations for the third user
user3.make_deposit(500).make_withdrawal(100).make_withdrawal(200).make_withdrawal(50).display_user_balance()

# Transfer money from the first user to the third user
user1.transfer_money(user3, 50)
user1.display_user_balance()
user3.display_user_balance()
