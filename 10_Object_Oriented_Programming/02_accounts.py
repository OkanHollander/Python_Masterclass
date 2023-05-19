import datetime
import pytz


class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance) -> None:
        self._name = name
        self._balance = balance
        self._transaction_list = []
        print(f"Account created for {self._name} with balance {self._balance}")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transaction_list.append((Account._current_time(), amount))
            print(f"{self._name} deposited {amount} into account")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            self._transaction_list.append((Account._current_time(), - amount))
            print(f"{self._name} withdrew {amount}")
        else:
            print("Insufficient funds")

    def show_balance(self):
        print(f"{self._name}'s balance is {self._balance}")

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                trans_type = "deposit"
            else:
                trans_type = "withdrawal"
            print(
                f"{trans_type} of {amount} on {date.astimezone(pytz.utc).strftime('%Y-%m-%d %H:%M:%S')}"
            )


if __name__ == "__main__":
    account = Account("John", 1000)
    account.deposit(500)
    account.withdraw(500)
    account.show_balance()
    account.show_transactions()

    steph = Account("Steph", 1000)
    steph.deposit(500)
    steph.withdraw(200)
    steph.show_transactions()
    steph.show_balance()
