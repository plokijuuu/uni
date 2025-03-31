import random
licz1 = 0
licz2 = 0
licz3 = 0
licz4 = 0
licz5 = 0
licz6 = 0
for i in range(1000):
    n = random.randint(1, 6)
    if n == 1:
        licz1 += 1
    elif n == 2:
        licz2 += 1
    elif n == 3:
        licz3 += 1
    elif n == 4:
        licz4 += 1
    elif n == 5:
        licz5 += 1
    else:
        licz6 += 1

print(f'Podczas rzutu 1000 razy wypadła:')
print(f'ścianka 1 - {licz1}')
print(f'ścianka 2 - {licz2}')
print(f'ścianka 3 - {licz3}')
print(f'ścianka 4 - {licz4}')
print(f'ścianka 5 - {licz5}')
print(f'ścianka 6 - {licz6}')
