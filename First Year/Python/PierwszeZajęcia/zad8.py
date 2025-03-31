from math import sqrt

a = float(input("Podaj dlugosc przekatnej a: "))
b = a / sqrt(2)
if a > 0:
    print(f'Pole powierzchni calkowitej to {b * b + 2 * b:.2f}')
    print(f'Objetosc wynosi: {1 / 3 * b * b:.2f}')
else:
    print("Wprowadzono niepoprawne a")
