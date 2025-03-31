licz = int(input("Podaj licznik: "))
mian = int(input("Podaj mian: "))

if licz < mian:
    print("Ulamek wlasciwy")
elif licz % mian == 0:
    print("Ulamek niewlasciwy")
else:
    print("Ulamek mieszany")