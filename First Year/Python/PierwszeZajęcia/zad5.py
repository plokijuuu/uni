x = int(input("Podaj pierwsza wspolrzedna: "))
y = int(input("Podaj druga wspolrzedna: "))

if x > 0 and y > 0:
    print("Pierwsza cwiartka")
elif x < 0 and y > 0:
    print("Druga cwiartka")
elif x < 0 and y < 0:
    print("Trzecia cwiartka")
else:
    print("Czwarta cwiartka")