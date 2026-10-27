# Creating Inheritance and Overriding

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

class SavingsAccount(Account):
    def __init__(self,holder,balance=0,min_balance=500):
        super().__init__(holder,balance)
        self.min_balance=min_balance

    def withdraw(self, amount):
        if self.balance-amount < self.min_balance:
            raise InsufficientFundsEroor(f"Insufficient funds: balance {self.balance}, requested {amount}")
        self.balance -= amount
        print(f"{self.holder} withdraw {amount} -> balance {self.balance}")

priya = SavingsAccount("Priya",1500)

try:
    priya.withdraw(1200)
    

except InsufficientFundsEroor as e:
    print("Error:",e)

try:
    priya.withdraw(800)
    
except InsufficientFundsEroor as e:
        print("Error:",e)

print(isinstance(priya,Account))



