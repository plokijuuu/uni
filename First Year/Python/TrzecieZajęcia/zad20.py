import random


listt = ["śmierdzący", "brzydki"]
list1 = ["idiota", "debil"]

def dodawanieprzy(slo):
    listt.append(slo)

def usuwanieprzy(slo):
    if len(listt) > 2:
        listt.pop(listt.index(slo))

def dodawanierze(slo):
    list1.append(slo)

def usuwanierze(slo):
    if len(list1) > 2:
        list1.pop(listt.index(slo))

def genera():
    imie = str(input("Podaj imie: "))
    wiek = int(input("Podaj wiek: "))
    if wiek >= 40:
        print(f'{imie} to stary {random.choice(listt)} {random.choice(list1)}')
    else:
        print(f'{imie} to nieokrzesany {random.choice(listt)} {random.choice(list1)}')
def prog():
    while True:
        print("Dodanie przymiotnika - wybierz 1")
        print("Dodanie rzeczownika - wybierz 2")
        print("Usuwanie przymiotnika - wybierz 3")
        print("Usuwanie rzeczownika - wybierz 4")
        print("Generowanie obelgi - wybierz 5")
        print("Zakoncz program - wybierz 6")
        x = int(input("Wybierz liczbę z menu: "))
        if x == 1:
            dodawanieprzy(str(input("Podaj przymiotnik: ")))
        elif x == 2:
            dodawanierze(str(input("Podaj rzeczownik: ")))
        elif x == 3:
            usuwanieprzy(str(input("Podaj przymiotnik: ")))
        elif x == 4:
            usuwanierze(str(input("Podaj rzeczownik: ")))
        elif x == 5:
            genera()
        else:
            break

prog()
