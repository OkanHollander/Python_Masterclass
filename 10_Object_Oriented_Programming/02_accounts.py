class Account:
    """Simple account class with balance"""

    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
        print(f"Account created for {self.name}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.name} deposited {amount}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} withdrew {amount}")
        else:
            print("Insufficient funds")

    def show_balance(self):
        print(f"{self.name}'s balance is {self.balance}")


if __name__ == "__main__":
    account = Account("John", 1000)
    account.deposit(500)
    account.withdraw(500)
    account.show_balance()