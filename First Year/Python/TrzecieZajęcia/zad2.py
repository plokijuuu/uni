def far(x):
    return 9/5*x + 32

x = float(input("Podaj temperature: "))
while x > -273.15:
    print(far(x))
    x = float(input("Podaj temperature: "))
