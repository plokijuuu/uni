def gen_primes():
    D = {}
    q = 2

    while True:
        if q not in D:
            yield q
            D[q*q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


primes = gen_primes()

with open("primes_10000.txt", "w") as f:
    for _ in range(10000):
        f.write(str(next(primes)) + "\n")
