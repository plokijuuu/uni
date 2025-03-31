listt = []
def dodawanie(wyn):
    if len(listt) == 5:
        x = min(listt)
        if x < wyn:
            listt.pop(listt.index(x))
            listt.append(wyn)
    else:
        listt.append(wyn)
def wyswietl():
    print(listt)
def sortowanie():
    listt.sort()
def usuwanie(wyn):
    listt.pop(listt.index(wyn))
def prog():
    while True:
        print("Dodawanie wyniku - wybierz 1")
        print("Usuwanie wyniku - wybierz 2")
        print("Wyświetlanie listy - wybierz 3")
        print("Sortowanie listy - wybierz 4")
        print("Zakończenie pracy programu - wybierz 5")
        x = int(input("Wybierz liczbę z menu: "))
        if x == 1:
            y = int(input("Podaj wynik: "))
            dodawanie(y)
        elif x == 2:
            y = int(input("Podaj wynik: "))
            usuwanie(y)
        elif x == 3:
            wyswietl()
        elif x == 4:
            sortowanie()
        else:
            break

prog()