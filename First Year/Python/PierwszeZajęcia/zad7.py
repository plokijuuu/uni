day = int(input("Podaj dzien: "))
month = int(input("Podaj miesiac: "))
year = int(input("Podaj rok: "))

if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2050:
    print(f'Data to: {day:02}.{month:02}.{year}')
