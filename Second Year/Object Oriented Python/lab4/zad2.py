def numbers():
    i = 1
    while True:
        yield i
        i += 1


def squares():
    for n in numbers():
        yield n * n


def select(iterable, n):
    it = iter(iterable)
    result = []
    for _ in range(n):
        result.append(next(it))
    return result


def pythagorean_triples():
    c = 1
    while True:
        for b in range(1, c):
            for a in range(1, b):
                if a*a + b*b == c*c:
                    yield (a, b, c)
        c += 1


print(select(numbers(), 10))

print(select(squares(), 10))

triples = pythagorean_triples()
first_15 = select(triples, 15)
for t in first_15:
    print(t)


