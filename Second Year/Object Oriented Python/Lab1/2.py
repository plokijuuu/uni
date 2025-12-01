import random

class Dice:
    def __init__(self, sides):
        self.__sides = sides
        self.__value = None

    def roll(self):
        self.__value = random.randint(1, self.__sides)

    def get_sides(self):
        return self.__sides

    def get_value(self):
        return self.__value

    def __str__(self):
        return f"Liczba ścian: {self.__sides}, Wartość: {self.__value}"


dice1 = Dice(6)
dice2 = Dice(6)
computer_dice1 = Dice(6)
computer_dice2 = Dice(6)

computer_score = 0
player_score = 0

while True:
    computer_dice1.roll()
    computer_dice2.roll()
    computer_score += computer_dice1.get_value() + computer_dice2.get_value()

    choice = input("Czy chcesz rzucić kostkami? (t/n): ")
    if choice.lower() != 't':
        break

    dice1.roll()
    dice2.roll()
    player_score += dice1.get_value() + dice2.get_value()
    print(f"Wynik rzutu: {dice1.get_value()} i {dice2.get_value()}. Suma punktów: {player_score}")

    if player_score > 21:
        print("Przekroczyłeś 21 punktów. Przegrana!")
        exit()

print(f"Punkty komputera: {computer_score}")
print(f"Twoje punkty: {player_score}")

if player_score <= 21 and (player_score > computer_score or computer_score > 21):
    print("Wygrałeś!")
else:
    print("Przegrałeś!")
