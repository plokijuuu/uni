def square(a,b,c,x):
    return a*x*x + b*x + c
try:
    a = int(input("Podaj liczbe: "))
    b = int(input("Podaj liczbe: "))
    c = int(input("Podaj liczbe: "))
    x = int(input("Podaj liczbe: "))
    print(square(a,b,c,x))
except ValueError:
    print("Błąd proszę podać liczbę")





