print("Witaj w systemie logowania do komputera!")

while True:
    s = str(input("Podaj hasło dostępu: "))
    if s == 'programowanie':
        break
    print("Błędne hasło! Odmowa dostępu!")

print("Logowanie zakończyło się sukcesem!")