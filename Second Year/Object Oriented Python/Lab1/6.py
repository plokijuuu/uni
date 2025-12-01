class Pet:
    def __init__(self, name, hunger=0, tiredness=0):
        self.name = name
        self.hunger = hunger
        self.tiredness = tiredness

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (value.isalpha() and len(value) >= 3):
            raise ValueError("Imię zwierzaka musi mieć co najmniej 3 litery i zawierać tylko litery.")
        self._name = value.capitalize()

    def _passage_of_time(self):
        self.hunger += 1
        self.tiredness += 1

    @property
    def mood(self):
        total = self.hunger + self.tiredness
        if total < 5:
            return "szczęśliwy"
        elif total <= 10:
            return "zadowolony"
        elif total <= 15:
            return "podenerwowany"
        else:
            return "wściekły"

    def talk(self):
        self._passage_of_time()
        print(f"{self.name} jest teraz {self.mood}.")

    def eat(self, food=4):
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self._passage_of_time()
        print(f"{self.name} zjadł posiłek.")

    def play(self, fun=4):
        self.tiredness -= fun
        if self.tiredness < 0:
            self.tiredness = 0
        self._passage_of_time()
        print(f"{self.name} bawił się wesoło.")

    def __str__(self):
        return f"Zwierzak: {self.name}\nGłód: {self.hunger}\nZnudzenie: {self.tiredness}\nNastrój: {self.mood}"


def main():
    name = input("Podaj imię swojego zwierzaka: ")
    try:
        pet = Pet(name)
    except ValueError as e:
        print("Błąd:", e)
        return

    while True:
        print("\n--- Menu Opieki nad Zwierzakiem ---")
        print("1. Porozmawiaj ze zwierzakiem")
        print("2. Nakarm zwierzaka")
        print("3. Pobaw się ze zwierzakiem")
        print("xy. Pokaż szczegóły zwierzaka")
        print("0. Zakończ")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            pet.talk()
        elif choice == "2":
            try:
                amount = int(input("Ile jedzenia chcesz dać zwierzakowi? "))
                pet.eat(amount)
            except ValueError:
                print("Podaj liczbę całkowitą.")
        elif choice == "3":
            try:
                time = int(input("Ile czasu chcesz poświęcić na zabawę? "))
                pet.play(time)
            except ValueError:
                print("Podaj liczbę całkowitą.")
        elif choice.lower() == "xy":
            print("\n" + str(pet))
        elif choice == "0":
            print(f"Do zobaczenia! {pet.name} będzie za tobą tęsknić!")
            break
        else:
            print("Nieprawidłowy wybór.")


if __name__ == "__main__":
    main()
