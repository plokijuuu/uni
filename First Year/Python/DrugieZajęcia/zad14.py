import random

while True:
    n = int(input("Podaj liczbę z zakresu od 1 do 100: "))
    if 1 <= n <= 100:
        break
    print("Podano złą liczbę.")
los = random.randint(1, 100)
licz = 1
start = 1
end = 100
while n != los:
    print("Zła odpowiedz. Spróbuj ponownie")
    licz += 1
    if n < los:
        print(f'Liczba {los} jest za duża')
        end = los
    else:
        print(f'Liczba {los} jest za mała')
        start = los

    los = random.randint(start, end)

print(f'Gratulacje udało ci się zgadnąć liczbę {los} za {licz} razem')
