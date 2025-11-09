# Реализуй три класса:
# BankAccount(owner: str, balance: float=0.0)
# Инкапсуляция баланса через @property (+ проверка balance >= 0).
# Методы: deposit(amount), withdraw(amount) -> float.
# SavingsAccount(BankAccount)
# Полиморфно переопредели withdraw: удерживай фиксированную комиссию FEE (по умолчанию 1.0).
# PremiumAccount(BankAccount)
# Полиморфно переопредели withdraw: без комиссии, но разрешён овердрафт до OVERDRAFT=100.0.
# Валидация входных данных:
# Отрицательные суммы в deposit/withdraw запрещены.
# При недостатке средств (с учётом комиссии/овердрафта) — бросай ValueError с понятным текстом.
# Приватные поля:
# Баланс хранить в _balance, читать/менять только через property.

class BankAccount:

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner: str = owner
        self._balance: float = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value: float):
        if value >= 0:
            self._balance = value
        else:
            raise ValueError("Balance can't be negative")

    def deposit(self, value) -> float:
        if value >= 0:
            self.balance = self.balance + value
        else:
            raise ValueError("Deposit can't be negative")
        return self.balance

    def withdraw(self, value: float) -> float:
        if value > self.balance:
            raise ValueError("Error withdraw!")
        self.balance = self.balance - value
        return self.balance

class SavingsAccount(BankAccount):
    FEE = 1.0

    def withdraw(self, value: float) -> float:
        total = value + self.FEE
        if total > self.balance:
            raise ValueError("Error withdraw!")
        self.balance -= total
        return self.balance


class PremiumAccount(BankAccount):
    OVERDRAFT = 100.0

    def withdraw(self, value: float) -> float:
        if value > self.balance + self.OVERDRAFT:
            raise ValueError("Overdraft limit error")
        self.balance -= value
        return self.balance


acc1 = PremiumAccount('Alex', 1200)
acc2 = SavingsAccount('Pit', 200)
acc3 = SavingsAccount('Max', 0)

print(acc1.owner, acc1.balance)
print(acc2.owner, acc2.balance)
print(acc3.owner, acc3.balance)


# for acc in [acc1, acc2, acc3]:
#     acc.withdraw(9)
#     print(acc.owner, acc.balance)

for acc in [acc1, acc2, acc3]:
    acc.deposit(100)
    print(acc.owner, acc.balance)

for acc in [acc1, acc2, acc3]:
    acc.withdraw(9)
    print(acc.owner, acc.balance)