while True:
    n = int(input("Podaj nie ujemna liczbe calkowita n: "))
    if n >= 0:
        break
i = 1
suma = 0
while i <= n:
    suma += i
    i += 1

print(suma)


