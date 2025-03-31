while True:
    n = int(input("Podaj liczbe calkowita wieksza od 2: "))
    if n > 2:
        break

while True:
    k = int(input("Podaj mniejszą od poprzedniej liczbę całkowitą (większą od 0): "))
    if k < n and k > 0:
        break

for i in range(1, n + 1):
    if i % k == 0:
        continue
    else:
        print(i)
