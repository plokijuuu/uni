import sys


class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a >= self.n:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value


def fibonacci_gen(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


def fibonacci_infinite():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib_slice(start, stop):
    gen = fibonacci_infinite()
    for _ in range(start):
        next(gen)
    for _ in range(stop - start + 1):
        yield next(gen)


numbers = fib_slice(100000, 100020)

sys.set_int_max_str_digits(2_000_000)

with open("fib_output.txt", "w") as f:
    for num in numbers:
        f.write(str(num) + "\n")
