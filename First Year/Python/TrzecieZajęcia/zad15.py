import random

def choose_word(word_list):
    return random.choice(word_list)
def check_letter(word):
    print(f'Twoje słowo ma {len(word)} liter')
    for x in range(5):
        x = str(input("Podaj litere: "))
        x = x.lower()
        if x in word:
            print("Tak znajduje się w twoim słowie")
        else: print("Nie ma jej w twoim słowie")
def play_game():
    listt = ["kot", "pies", "kaczka", "lew"]
    y = choose_word(listt)
    check_letter(y)
    g = str(input("Zgadnij słowo: "))
    g = g.lower()
    if g == y:
        print("Gratulacje! Poprawna odpowiedź")
    else:
        print(f"Niestety nie udało się zgadnąć :( Poprawna odpowiedź to {y}")

play_game()