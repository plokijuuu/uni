def collatz(n: int):
    if n <= 0:
        raise ValueError("n musi być liczbą dodatnią.")
    while True:
        yield n
        if n == 1:
            break
        n = n // 2 if n % 2 == 0 else 3 * n + 1


class CollatzSequence:

    def __init__(self, n: int):
        if n <= 0:
            raise ValueError("n musi być liczbą dodatnią.")
        self.current = n

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current
        if value == 1:
            self.current = None
            return value

        self.current = value // 2 if value % 2 == 0 else 3 * value + 1
        return value

def stopping_time(n: int) -> int:
    count = 0
    for x in collatz(n):
        if x == 1:
            return count
        count += 1

def max_value(n: int) -> int:
    return max(collatz(n))

best_n = None
best_time = -1

for i in range(1, 101):
    t = stopping_time(i)
    if t > best_time:
        best_time = t
        best_n = i

print(f"Największy stopping_time ma n = {best_n}, długość = {best_time}")
