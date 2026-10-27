# Creating Bank Account Class

class InsufficientFundsEroor(Exception):
    pass

class Account: 
    def __init__(self,holder,balance=0):
        self.holder=holder
        self.balance=balance

    def deposit(self,amount):
        self.balance=amount+self.balance
        print(self.holder," deposited ",amount," -> balance ",self.balance)

    def withdraw(self,amount):
        if amount>self.balance:
            raise InsufficientFundsEroor(f"Insufficient funds: balance {self.balance}, requested {amount}")

        self.balance=self.balance-amount
        print(f"{self.holder} withdraw {amount} -> balance {self.balance}")

    def show(self):
        print(f"Holder: {self.holder}, Balance: {self.balance}")
account=Account("Arun",1000)

try:
    account.deposit(500)
    account.withdraw(2000)

except InsufficientFundsEroor as e:
    print("Error: ",e)

finally:
    print("Transaction finished")


