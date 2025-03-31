slo = str(input("Podaj słowo: "))
listt = ['a', 'e', 'i', 'o', 'u']
slo1 = ""
for i in range(len(slo)):
    if slo[i] not in listt:
        slo1 += slo[i]
print(slo1)