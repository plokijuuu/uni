def fun(a,b,c,d):
    sum = a + b + c + d - min(a,b,c,d)
    return sum/3

a = int(input("Podaj liczbe: "))
b = int(input("Podaj liczbe: "))
c = int(input("Podaj liczbe: "))
d = int(input("Podaj liczbe: "))
print(fun(a,b,c,d))