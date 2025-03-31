while True:
    n = int(input("Podaj liczbe calkowita wieksza od 0: "))
    if n > 0:
        break

i = 1
suma = 0
while i <= n:
    suma += i * i
    i += 1

print(suma)