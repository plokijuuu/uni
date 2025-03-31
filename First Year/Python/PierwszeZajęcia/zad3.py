a = int(input("Podaj liczbe "))
if a > 0:
    print("Liczba dodatnia")
if a % 2 == 0:
    print("Liczba parzysta")

b=int(input("Podaj liczbe "))
if b == a:
    print("Liczby sa rowne")
else:
    print("Liczba a wieksza od b" if a > b else "Liczba b wieksza pd a")

print(f'Pole kwadratu b to {b * b: .2f}')
print(f'Obwod kwadratu b to {4 * b: .2f}')

if b != 0:
    print(f'Liczba przeciwna to {b + 2 * b: .2f}' if b < 0 else f'Liczba przeciwna to {b - 2 * b: .2f}')
    print(f'Liczba odwrotna to {1 / b: .2f}')
else:
    print(0)

if b == 0:
    print("Liczba jest rowna zero")
elif b > 0:
    print("Liczba jest dodatnia")
else:
    print("Liczba jest ujemna")

if b > -5 and b < 5:
    print("Liczba nalezy do przedzialu pierwszego")
if b < 5 or b > 10:
    print("Liczba nalezy do przedzialu drugiego")

