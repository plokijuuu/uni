import random

los = random.randint(1,100)
licz = 0
while True:
    n = int(input("Zgadnij liczbę od 1 do 100: "))
    licz += 1
    if n == los:
        break
    print("Zła odpowiedź :(")
    if n < los:
        print("Twoja liczba jest mniejsza")
    else:
        print("Twoja liczba jest wieksza")
print(f'Gratulacje! Zgadłeś szukaną liczbę za {licz} razem :)')

