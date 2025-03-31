import random
def throw():
    a = random.randint(1,6)
    b = random.randint(1,6)
    return a + b
def singlegame():
    a = throw()
    print(f'Suma pierwszych dwóch rzutów wynosi {a}')
    if a == 7 or a == 11:
        print("Wygrana")
        return True
    elif a == 12 or a == 3 or a == 2:
        print("Przegrana")
        return False
    else:
        print("Zdobywasz punkt i rzucach ponownie")
        a = throw()
        print(f"Suma oczek drugiego rzutu wynosi {a}")
        if a == 7:
            print("Przegrana")
            return False
        else:
            print("Wygrana")
            return True

def get_answer():
    ans = str(input("Czy chcesz grać? (tak/nie) "))
    if ans == "nie":
        return False
    else:
        return True
def game():
    wyg = 0
    prze = 0
    while get_answer() == True:
        if singlegame() == True:
            wyg += 1
        else:
            prze += 1
    print(f'Liczba wygranych {wyg}, liczba przegranych {prze}')

game()