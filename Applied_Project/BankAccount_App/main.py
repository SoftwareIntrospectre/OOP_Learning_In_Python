class BankAccount:
    def __init__(self):
        self.balance = 0


    def get_balance(self):
        print(f"Balance = {self.balance}")


    def deposit(self, amount):
        if amount < 0:
            print("Cannot deposit a negative number.")

        elif amount == 0:
            print("Cannot deposit a zero amount.")

        else:
            self.balance += amount
            print(f"Deposit amount = {self.balance}")


    def withdraw(self, amount):
        if amount > self.balance:
            print("Cannot withdraw more than deposited")

        elif amount <=0:
            print("Cannot withdraw fewer than 1")

        else:
            self.balance -= amount
            print(f"Withdrawl amount = {amount}")
    


account1 = BankAccount()

account1.get_balance()

account1.deposit(0)
account1.deposit(-3)
account1.deposit(100)

account1.get_balance()
account1.withdraw(-10)
account1.withdraw(90)
account1.get_balance()
account1.deposit(500000)