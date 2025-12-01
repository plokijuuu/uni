class Person:
    def __init__(self, name=None, surname=None, age=None):
        self._name = None
        self._surname = None
        self._age = None

        if name:
            self.name = name
        if surname:
            self.surname = surname
        if age is not None:
            self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) < 3:
            raise ValueError("Imię musi zawierać co najmniej 3 znaki.")
        self._name = value.strip().capitalize()

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str) or len(value.strip()) < 3:
            raise ValueError("Nazwisko musi zawierać co najmniej 3 znaki.")
        self._surname = value.strip().capitalize()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("Wiek musi być liczbą całkowitą.")
        if not (0 <= value <= 130):
            raise ValueError("Wiek musi być z zakresu 0–130.")
        self._age = value

    def __str__(self):
        return f"{self.name} {self.surname}, wiek: {self.age} lat"


class Student(Person):
    def __init__(self, name=None, surname=None, age=None, major=None):
        super().__init__(name, surname, age)
        self.major = major
        self.grades = {}

    def add_grade(self, subject, grade):
        if not subject or len(subject.strip()) < 2:
            raise ValueError("Nazwa przedmiotu musi zawierać co najmniej 2 znaki.")
        if not (2.0 <= grade <= 5.0):
            raise ValueError("Ocena musi być z zakresu 2.0–5.0.")
        self.grades[subject.strip().title()] = grade

    def show_grades(self):
        if not self.grades:
            print("Brak ocen.")
        else:
            print("Oceny studenta:")
            for subject, grade in self.grades.items():
                print(f" - {subject}: {grade}")

    def __str__(self):
        base = super().__str__()
        return f"{base}, kierunek: {self.major}"


class Employee(Person):
    def __init__(self, name=None, surname=None, age=None, position=None):
        super().__init__(name, surname, age)
        self.position = position
        self.skills = []

    def add_skill(self, skill):
        if not skill or len(skill.strip()) < 2:
            raise ValueError("Nazwa umiejętności musi zawierać co najmniej 2 znaki.")
        self.skills.append(skill.strip().capitalize())

    def show_skills(self):
        if not self.skills:
            print("Brak umiejętności.")
        else:
            print("Umiejętności pracownika:")
            for skill in self.skills:
                print(f" - {skill}")

    def __str__(self):
        base = super().__str__()
        return f"{base}, stanowisko: {self.position}"

if __name__ == "__main__":
    print("=== TWORZENIE OSOBY ===")
    try:
        name = input("Podaj imię: ")
        surname = input("Podaj nazwisko: ")
        age = int(input("Podaj wiek: "))

        person = Person(name, surname, age)
        print("\nUtworzono obiekt:")
        print(person)

    except ValueError as e:
        print(f"Błąd: {e}")

    print("\n=== TWORZENIE STUDENTA ===")
    student = Student()
    try:
        student.name = input("Podaj imię studenta: ")
        student.surname = input("Podaj nazwisko studenta: ")
        student.age = int(input("Podaj wiek studenta: "))
        student.major = input("Podaj kierunek studiów: ")

        while True:
            add = input("Czy chcesz dodać ocenę? (t/n): ").lower()
            if add == "t":
                subject = input("Przedmiot: ")
                grade = float(input("Ocena (2.0–5.0): "))
                student.add_grade(subject, grade)
            else:
                break

        print("\nUtworzono studenta:")
        print(student)
        student.show_grades()

    except ValueError as e:
        print(f"Błąd: {e}")

    print("\n=== TWORZENIE PRACOWNIKA ===")
    employee = Employee()
    try:
        employee.name = input("Podaj imię pracownika: ")
        employee.surname = input("Podaj nazwisko pracownika: ")
        employee.age = int(input("Podaj wiek pracownika: "))
        employee.position = input("Podaj stanowisko: ")

        while True:
            add = input("Czy chcesz dodać umiejętność? (t/n): ").lower()
            if add == "t":
                skill = input("Umiejętność: ")
                employee.add_skill(skill)
            else:
                break

        print("\nUtworzono pracownika:")
        print(employee)
        employee.show_skills()

    except ValueError as e:
        print(f"Błąd: {e}")
