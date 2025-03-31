import random
licz0 = 0
licz1 = 0
for i in range(100):
    n = random.randint(0,1)
    if n == 0:
        licz0 += 1
    else:
        licz1 += 1

print(f'Podczas rzutu 100 raz bylo {licz1} orłów i {licz0} reszek')
