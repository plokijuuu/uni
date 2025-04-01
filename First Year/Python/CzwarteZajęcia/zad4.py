from collections import Counter


def zlicz(tekst):
    zliczanie = {}
    for i in tekst:
        i = i.lower()
        if i.isalpha():
            if i in zliczanie:
                zliczanie[i] += 1
            else:
                zliczanie[i] = 1

    for i in sorted(zliczanie):
        print(f"[{i}]: {zliczanie[i]}")

def zlicz_counter(tekst):
    filtr = [i.lower() for i in tekst if i.isalpha()]
    zliczanie = Counter(filtr)

    for i in sorted(zliczanie):
        print(f"[{i}]: {zliczanie[i]}")

zlicz("TTTTttt Tt T a")
zlicz_counter("TTTTttt Tt T a")