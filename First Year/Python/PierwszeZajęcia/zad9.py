d = float(input("Podaj dochod: "))

if d < 8000:
    print(f'Podatek wynosi: {0:.2f}')
elif 8000 >= d <= 34500:
    print(f'Podatek wynosi: {(d - 8000) * 0.1:.2f}')
elif d > 34500:
    print(f'Podatek wynosi: {(34500 - 8000) * 0.1 + (d - 34500) * 0.24:.2f}')