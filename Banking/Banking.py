class Banking:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdrawal(self, amount):
        if self.balance>= amount:
            self.balance -= amount
        else:
            raise AssertionError("Insufficient Amount")
    def print_balance(self):
        print(self.balance)

b = Banking()
b.deposit(2000)
b.print_balance()
b.withdrawal(1000)
b.print_balance()
# b.withdrawal(1001)