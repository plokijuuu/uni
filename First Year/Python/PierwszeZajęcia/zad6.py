from math import sqrt

a = int(input("Podaj zmienna a rownania kwadratowego: "))
b = int(input("Podaj zmienna b rownania kwadratowego: "))
c = int(input("Podaj zmienna c rownania kwadratowego: "))

if a != 0:
    delta = b * b - 4 * c
    if delta > 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print(f'Pierwiastki funkcji kwadratowej to: {x1}, {x2}')
    elif delta == 0:
        x = (-b / (2 * a))
        print(f'Pierwiastek funkcji kwadratowej to: {x}')
    else:
        print("Nie ma pierwiastkow")
elif b == 0:
    print(f'Rozwiazaniem jest zbior liczb rzeczywistych' if c == 0 else f'Nie ma pierwiastkow')
else:
    x = -c / b
    print(f'Pierwiastek funkcji to: {x}')
