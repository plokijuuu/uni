def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
try:
    n = int(input("Podaj liczbe: "))
    while collatz(n) != 1:
        n = collatz(n)
        print(n)
    print(collatz(n))

except ValueError:
    print("Błąd")

