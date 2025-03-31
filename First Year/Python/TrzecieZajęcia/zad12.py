slo = str(input("Podaj słowo: "))
listt = []
for i in range(26):
    listt.append(0)

for i in range(len(slo)):
    listt[ord(slo[i])-ord('a')] += 1
c = 'A'
for i in range(len(listt)):
    print(f'{c} - {listt[i]}')
    c = ord(c) + 1
    c = chr(c)