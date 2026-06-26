class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New Balance: ₹{self.balance}")

    def display(self):
        print(f"Account Owner: {self.owner}")
        print(f"Current Balance: ₹{self.balance}")



acc = BankAccount("Rahul", 1000)
acc.display()
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)