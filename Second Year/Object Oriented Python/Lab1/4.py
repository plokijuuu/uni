class Matrix:
    def __init__(self, row, col, value=None):
        self._row = row
        self._col = col
        self._matrix = [[value for _ in range(col)] for _ in range(row)]

    @property
    def size(self):
        return self._row, self._col

    def _check_index(self, row, col):
        if not (0 <= row < self._row) or not (0 <= col < self._col):
            raise IndexError("Indeks poza zakresem macierzy.")

    def get_cell(self, row, col):
        self._check_index(row, col)
        return self._matrix[row][col]

    def set_cell(self, row, col, value):
        self._check_index(row, col)
        self._matrix[row][col] = value

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self._matrix])


# Test klasy Matrix
try:
    m = Matrix(3, 4, 0)
    print("Macierz początkowa:")
    print(m)

    print("\nWymiar macierzy:", m.size)

    m.set_cell(1, 2, 9)
    print("\nPo zmianie elementu (1,2) na 9:")
    print(m)

    print("\nOdczyt komórki (1,2):", m.get_cell(1, 2))

    print("\nPróba odczytu komórki spoza zakresu:")
    print(m.get_cell(5, 5))

except IndexError as e:
    print("Błąd:", e)
