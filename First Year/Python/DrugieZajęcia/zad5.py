ocena = int(input("Podaj liczbe punktow: "))

if ocena < 0 or ocena > 100:
    print("Błędne dane")
else:
    if 90 <= ocena <= 100:
        print("Otrzymałeś A")
    elif 80 <= ocena <= 89:
        print("Otrzymałeś B")
    elif 70 <= ocena <= 79:
        print("Otrzymałeś C")
    elif 60 <= ocena <= 69:
        print("Otrzymałeś D")
    else:
        print("Otrzymałeś E")