n = int(input("Podaj liczbę wierszy: "))
spa = n - 1
gwia = 1
for i in range(n):
    for j in range(spa - i):
        print(" ", end="")
    for m in range(gwia):
        print("*", end="")
    gwia += 2
    print()