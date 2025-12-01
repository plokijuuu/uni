class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        if not (0 <= value <= 23):
            raise ValueError("Godzina musi być w zakresie 0-23.")
        self._hour = value

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        if not (0 <= value <= 59):
            raise ValueError("Minuta musi być w zakresie 0-59.")
        self._minute = value

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, value):
        if not (0 <= value <= 59):
            raise ValueError("Sekunda musi być w zakresie 0-59.")
        self._second = value

    def set_time(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        return f"Time(hour={self.hour}, minute={self.minute}, second={self.second})"

    def __str__(self):
        suffix = "AM"
        display_hour = self.hour
        if self.hour == 0:
            display_hour = 12
        elif self.hour == 12:
            suffix = "PM"
        elif self.hour > 12:
            display_hour = self.hour - 12
            suffix = "PM"
        return f"{display_hour:02}:{self.minute:02}:{self.second:02} {suffix}"


# Test klasy Time
try:
    t = Time(23, 45, 10)
    print("Repr:", repr(t))
    print("Str:", str(t))

    t.set_time(7, 5, 30)
    print("\nPo zmianie czasu:")
    print("Repr:", repr(t))
    print("Str:", str(t))

    print("\nPróba ustawienia błędnej wartości:")
    t.hour = 25

except ValueError as e:
    print("Błąd:", e)
