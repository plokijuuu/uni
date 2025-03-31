n = int(input("Podaj liczbe wieksza od 1: "))
g = n
print("Podpunkt a")
for i in range(1, n + 1):
    print(f'{i} ', end='')
print()
i = 1
while i <= n:
    print(f'{i} ', end='')
    i += 1
print()
print("Podpunkt b")
for i in range(n,0,-1):
    print(f'{i} ', end='')
print()
while n > 0:
    print(f'{n} ', end='')
    n -= 1
print()
n = g
print("Podpunkt c")
for i in range(n):
    if i % 2 == 0:
        print(f'{i} ', end='')
print()
i = 0
while i < n:
    if i % 2 == 0:
        print(f'{i} ', end='')
    i += 1
print()
print("Podpunkt d")
for i in range(n,0,-1):
    if i % 2 != 0:
        print(f'{i} ', end='')
print()
while n > 0:
    if n % 2 != 0:
        print(f'{n} ', end='')
    n -= 1
print()
n = g
print("Podpunkt e")
for i in range(1, n*3, 3):
    print(f'{i} ', end='')
print()
i = 1
while n > 0:
    print(f'{i} ', end='')
    i += 3
    n -= 1
print()
n = g
print("Podpunkt f")
suma = 1
for i in range(1,13):
    suma = suma * i
    print(f'{suma} ', end='')
print()
i = 1
suma = 1
while i <= 12:
    suma = suma * i
    print(f'{suma} ', end='')
    i += 1
print()
print("Podpunkt g")
for i in range(1,n+1):
    print(f'{1/i:.2f} ', end='')
print()
i = 1
while i <= n:
    print(f'{1/i:.2f} ', end='')
    i += 1
print()
print("Podpunkt h")
pom = 3
print(pom, end='')
for i in range(1,17):
    pom = 6 * pom - 13/2
    print(f' {pom:.2f}', end='')
print()
pom = 3
print(pom, end='')
n = 17
while (n-1) > 0:
    pom = 6 * pom - 13 / 2
    print(f' {pom:.2f}', end='')
    n -= 1
print()
n = g
print("Podpunkt i")
pom = 0
print(pom, end='')
for i in range(1,31):
    pom = 2 * pom +1
    print(f' {pom}', end='')
print()
pom = 0
n=31
print(pom, end='')
while (n-1) > 0:
    pom = 2 * pom + 1
    print(f' {pom}', end='')
    n -= 1
print()
n = g
print("Podpunkt j")
suma = 0
for i in range (1, n+1):
    suma += i*i
print(suma)
suma = 0
i = 1
while i <= n:
    suma += i*i
    i += 1
print(suma)
print("Podpunkt k")
suma = 0
for i in range(2, 2*n + 1, 2):
    suma += i
print(suma)
suma = 0
i = 2
while i <= 2*n:
    suma += i
    i += 2
print(suma)
print("Podpunkt l")
suma = 0
for i in range(1, 2*n + 2, 2):
    suma += i
print(suma)
suma = 0
i = 1
while i <= 2*n+1:
    suma += i
    i += 2
print(suma)
print("Podpunkt m")
suma = 0
for i in range(0, n+1):
    if i % 2 == 0:
        suma += 1
print(f'Parzyste - {suma}, nieparzyste - {n-suma}')
suma = 0
while n >= 0:
    if n % 2 == 0:
        suma += 1
    n -= 1
n = g
print(f'Parzyste - {suma}, nieparzyste - {n-suma}')
print("Podpunkt o")
suma = 0
for i in range(3, n+1, 3):
    suma += 1
print(suma)
i = 3
suma = 0
while i <= n:
    suma += 1
    i += 3
print(suma)
print("Podpunkt p")
suma = 0
for i in range(5, n+1, 5):
    suma += 1
print(suma)
i = 5
suma = 0
while i <= n:
    suma += 1
    i += 5
print(suma)
print("Podpunkt q")
suma = 0
for i in range(1, n+1):
    suma += 1/i
print(f'{suma:.2f}')
suma = 0
i = 1
while i <= n:
    suma += 1/i
    i += 1
print(f'{suma:.2f}')
print("Podpunkt r")
suma = 0
for i in range(1, n+1):
    suma += 1/(i*i)
print(f'{suma:.2f}')
suma = 0
i = 1
while i <= n:
    suma += 1/(i*i)
    i += 1
print(f'{suma:.2f}')






