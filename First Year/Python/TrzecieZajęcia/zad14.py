import random

def choose_word(word_list):
    x = random.choice(word_list)
    return x
def shuffle_letters(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)
def play_game():
    list = ["kot", "cztery", "pies"]
    s = choose_word(list)
    print(shuffle_letters(s))
    while True:
        y = str(input("Sprobuj zgadnac slowo: "))
        y = y.lower()
        if y == s:
            break

    print("Gratulacje! Wygrana!")

play_game()

