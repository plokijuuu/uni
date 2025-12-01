class InvalidData(Exception):
    """Wyjątek zgłaszany, gdy dane są niepoprawne (np. długości ≤ 0)."""
    pass


class Rectangle:
    def __init__(self, length, height):
        if length <= 0 or height <= 0:
            raise InvalidData("Długość i wysokość muszą być dodatnie.")
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height

    def __str__(self):
        return f"Prostokąt: długość = {self.length}, wysokość = {self.height}, pole = {self.area()}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.length}, {self.height})"


class Cuboid(Rectangle):
    def __init__(self, length, height, width):
        if width <= 0:
            raise InvalidData("Szerokość musi być dodatnia.")
        super().__init__(length, height)
        self.width = width

    def area(self):
        base_area = super().area()
        return 2 * (base_area + self.length * self.width + self.height * self.width)

    def volume(self):
        return super().area() * self.width

    def __str__(self):
        return (f"Prostopadłościan: długość = {self.length}, wysokość = {self.height}, "
                f"szerokość = {self.width}, pole całkowite = {self.area()}, objętość = {self.volume()}")


def main():
    filename = "dane.txt"
    print(f"Odczyt danych z pliku: {filename}\n")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue

                try:
                    parts = line.split()
                    figure_type = int(parts[0])

                    if figure_type == 1:
                        if len(parts) != 3:
                            raise ValueError("Niepoprawna liczba parametrów dla prostokąta.")
                        length, height = map(float, parts[1:3])
                        rect = Rectangle(length, height)
                        print(rect)

                    elif figure_type == 2:
                        if len(parts) != 4:
                            raise ValueError("Niepoprawna liczba parametrów dla prostopadłościanu.")
                        length, height, width = map(float, parts[1:4])
                        cuboid = Cuboid(length, height, width)
                        print(cuboid)

                    else:
                        print(f"[Linia {line_number}] Nieznany typ figury: {figure_type}")

                except ValueError as ve:
                    print(f"[Linia {line_number}] Błąd formatu danych: {ve}")
                except InvalidData as ide:
                    print(f"[Linia {line_number}] Błąd danych: {ide}")

    except FileNotFoundError:
        print("Błąd: Plik 'dane.txt' nie został znaleziony.")
    except IOError:
        print("Błąd podczas odczytu pliku.")


if __name__ == "__main__":
    main()
