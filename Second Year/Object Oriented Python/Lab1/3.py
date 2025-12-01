class Account:
    def __init__(self, name, balance):
        if balance < 0:
            raise ValueError("Saldo początkowe nie może być ujemne.")
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Nie można wpłacić ujemnej kwoty.")
        self.balance += amount

    def take(self, amount):
        if amount > self.balance:
            raise ValueError("Brak środków na koncie.")
        self.balance -= amount

    def __str__(self):
        return f"Konto: {self.name}, Saldo: {self.balance} zł"


try:
    account = Account("Jan Kowalski", 1000)
    print(account)

    account.deposit(500)
    print("Po wpłacie:", account)

    account.take(200)
    print("Po wypłacie:", account)

    account.take(2000)
    print("Po próbie wypłaty:", account)

except ValueError as e:
    print("Błąd:", e)
