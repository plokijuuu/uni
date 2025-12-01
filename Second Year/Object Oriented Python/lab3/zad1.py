from datetime import datetime

class Note:
    _last_id = 0

    def __init__(self, text, tag):
        self.text = text
        self.tag = tag
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Note._last_id += 1
        self.ID = Note._last_id

    def match(self, query):
        return query.lower() in self.text.lower() or query.lower() in self.tag.lower()


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, text, tag):
        note = Note(text, tag)
        self.notes.append(note)

    def _find_note(self, ID):
        for note in self.notes:
            if note.ID == ID:
                return note
        return None

    def modify_text(self, ID, new_text):
        note = self._find_note(ID)
        if note:
            note.text = new_text
            return True
        return False

    def modify_tag(self, ID, new_tag):
        note = self._find_note(ID)
        if note:
            note.tag = new_tag
            return True
        return False

    def search(self, query):
        return [note for note in self.notes if note.match(query)]


class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.options = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def show_menu(self):
        print("""
-----------------------------
      PROSTY NOTATNIK
-----------------------------
1. Pokaż wszystkie notatki
2. Szukaj notatek
3. Dodaj notatkę
4. Modyfikuj notatkę
5. Zakończ
-----------------------------
""")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Wybierz opcję: ").strip()
            action = self.options.get(choice)
            if action:
                action()
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.")

    def show_notes(self, notes=None):
        if notes is None:
            notes = self.notebook.notes
        if not notes:
            print("Brak notatek do wyświetlenia.")
            return
        print("\n----- LISTA NOTATEK -----")
        for note in notes:
            print(f"ID: {note.ID}")
            print(f"Data: {note.date}")
            print(f"Tag: {note.tag}")
            print(f"Treść: {note.text}")
            print("-" * 40)

    def search_notes(self):
        query = input("Podaj wyszukiwane słowo: ").strip()
        results = self.notebook.search(query)
        if results:
            self.show_notes(results)
        else:
            print("Nie znaleziono żadnych notatek.")

    def add_note(self):
        text = input("Podaj treść notatki: ")
        tag = input("Podaj etykietę (tag): ")
        self.notebook.new_note(text, tag)
        print("Notatka została dodana!")

    def modify_note(self):
        """Pozwala zmodyfikować istniejącą notatkę."""
        try:
            ID = int(input("Podaj ID notatki do modyfikacji: "))
        except ValueError:
            print("ID musi być liczbą!")
            return

        print("1. Zmień treść\n2. Zmień tag")
        choice = input("Wybierz opcję: ").strip()
        if choice == "1":
            new_text = input("Podaj nową treść: ")
            if self.notebook.modify_text(ID, new_text):
                print("Treść została zmieniona.")
            else:
                print("Nie znaleziono notatki o podanym ID.")
        elif choice == "2":
            new_tag = input("Podaj nowy tag: ")
            if self.notebook.modify_tag(ID, new_tag):
                print("Tag został zmieniony.")
            else:
                print("Nie znaleziono notatki o podanym ID.")
        else:
            print("Nieprawidłowy wybór.")

    def quit(self):
        """Zamyka program."""
        print("Do widzenia!")
        exit()


if __name__ == "__main__":
    Menu().run()
