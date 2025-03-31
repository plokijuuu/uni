sex = str(input("Jesteś kobietą czy mężczyzną (M - mężczyzna, K - kobieta): "))

if sex == "K":
    age = int(input("Ile masz lat?: "))
    if 10 <= age <= 12:
        print("Możesz być w drużynie")
    else:
        print("Nie możesz być w drużynie")
else:
    print("Nie możesz być w drużynie")
