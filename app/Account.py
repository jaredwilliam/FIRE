from typing import List, Optional


class Account:
    """Base class for all types of accounts."""

    def __init__(self, name: str, balance: float = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdrawal(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient Funds")

    def __str__(self) -> str:
        return f"{self.name}: ${self.balance:.2f}"


# Asset Classes
class CashAccount(Account):
    pass


class InvestmentAccount(Account):
    pass


class RetirementAccount(Account):
    pass


class RealEstate(Account):
    pass


class PersonalProperty(Account):
    pass


class Receivable(Account):
    pass


# Liability Classes
class CurrentLiability(Account):
    pass


class LongTermLiability(Account):
    pass


class OtherLiability(Account):
    pass


if __name__ == "__main__":
    checking = CashAccount("Checking Account", 1500)
    savings = CashAccount("Savings Account", 5000)
    mortgage = LongTermLiability("Mortgage", 200000)

    checking.deposit(500)
    savings.withdrawal(1000)
    print(checking)
    print(savings)
    print(mortgage)
