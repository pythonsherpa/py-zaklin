class BankAccount:

    def __init__(self, owner):
        self.owner = owner
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def show_balance(self):
        print(f"{self.owner} has EUR {self.balance}")

    @property
    def balance(self):
        return self._balance


account_1 = BankAccount(owner='John')
account_1.deposit(100)
account_1._balance = 20000
print(account_1.balance)
account_1.show_balance()

account_2 = BankAccount(owner='Jane')
account_2.withdraw(50)
account_2.show_balance()
