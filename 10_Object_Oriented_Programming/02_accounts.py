import datetime
import pytz

class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print(f"Account created for {self.name}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_list.append((Account._current_time(), amount))
            print(f"{self.name} deposited {amount} into account")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
            print(f"{self.name} withdrew {amount}")
        else:
            print("Insufficient funds")

    def show_balance(self):
        print(f"{self.name}'s balance is {self.balance}")
    
    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                trans_type = "deposit"
            else:
                trans_type = "withdrawal"
            print(f"{trans_type} of {amount} on {date.astimezone(pytz.utc).strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    account = Account("John", 1000)
    account.deposit(500)
    account.withdraw(500)
    account.show_balance()
    account.show_transactions()