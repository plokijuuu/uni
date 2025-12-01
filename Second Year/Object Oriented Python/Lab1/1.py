import random

class Coin:
    def __init__(self, denomination):
        self.denomination = denomination
        self.side = "orzeł"

    def throw(self):
        self.side = random.choice(["orzeł", "reszka"])

    def __str__(self):
        return f"{self.denomination} zł - {self.side}"


print("Symulacja 15 rzutów jedną monetą")
coin1 = Coin(1)

for i in range(15):
    coin1.throw()
    print(f"Rzut {i+1}: {coin1}")

print("Symulacja gry hazardowej")

def simulate_game():
    coins = [Coin(1), Coin(2), Coin(5)]
    saldo = 0
    while saldo < 20:
        for coin in coins:
            coin.throw()
            if coin.side == "orzeł":
                saldo += coin.denomination

        if saldo >= 20:
            break
    return saldo

wins = 0
losses = 0

for i in range(100):
    result = simulate_game()
    if result == 20:
        wins += 1
    else:
        losses += 1

print(f"Wyniki po 100 symulacjach:")
print(f" - Wygrane (dokładnie 20 zł): {wins}")
print(f" - Przegrane (powyżej 20 zł): {losses}")
