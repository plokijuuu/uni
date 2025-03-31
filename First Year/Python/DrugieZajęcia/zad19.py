n = int(input("Podaj liczbę dni miesiąca: "))
d = int(input("Podaj początkowy dzień miesiąća (1- Nie, 7- Sob): "))

for i in range(1, d):
    print("   ", end="")
if d >= n:
    for i in range(1, n+1):
        print(f' {i} ', end='')
else:
    for i in range(1, 7-d+2):
        print(f' {i} ', end='')

    licz = 7 - d + 2
    pom = 0
    while licz <= n:
        if pom % 7 == 0:
            print()
            pom = 0
        if licz < 10:
            print(" ", end="")
        print(f'{licz} ', end="")
        licz += 1
        pom += 1

