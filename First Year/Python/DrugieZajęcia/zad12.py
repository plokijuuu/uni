while True:
    try:
        n = int(input("Podaj liczbę całkowitą większą od 1: "))
        if n < 2:
            raise ValueError
    except ValueError:
        print("Podano niepoprawną liczbę")
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                print("To nie jest liczba pierwsza")
                break
            i += 1

        if i * i > n:
            print("To jest liczba pierwsza")
