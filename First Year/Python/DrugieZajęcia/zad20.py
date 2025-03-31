n = int(input("Podaj liczbe wyrazów ciągów dla której policzyć sumę: "))
suma1 = 0
suma2 = 0
pom = -1
for i in range(2, n + 2):
    suma1 += 1.0/i
    suma2 += 1.0/i * pom
    pom = pom * -1

print(f'Suma 1 ciągu to {suma1:.2f}, suma 2 ciągu to {suma2:.2f}')