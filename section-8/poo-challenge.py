class Account:
    owner: str
    balance: float

    def __init__(self, owner: str, balance: int) -> None:
        self.owner = owner
        self.balance = balance

    def __str__(self) -> str:
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"

    def deposit(self, amount: float) -> None:
        self.balance += amount
        print(f"Deposit accepted\nYour current balance is: {self.balance}")

    def withdraw(self, amount: float) -> None:
        self.balance
        if self.balance - amount >= 0:
            self.balance -= amount
            print(f"Withdrawal accepted\nYour current balance is: {self.balance}")
        else:
            print("Funds unavailable!")


# 1. Instantiate the class
acct1 = Account("Jose", 100)
# 2. Print the object
print(acct1)
# 3. Show the account owner attribute
print(acct1.owner)
# 4. Show the account balance attribute
print(acct1.balance)
# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.withdraw(75)
# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
