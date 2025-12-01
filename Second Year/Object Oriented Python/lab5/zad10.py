def estimate_e():
    n = 0
    factorial = 1
    current_sum = 0.0

    while True:
        current_sum += 1 / factorial
        yield current_sum
        n += 1
        factorial *= n

gen = estimate_e()
for _ in range(5):
    print(next(gen))


def approx_e(eps):
    gen = estimate_e()
    prev = next(gen)
    terms = 1

    for current in gen:
        terms += 1
        if abs(current - prev) < eps:
            return current, terms
        prev = current

value, n_terms = approx_e(1e-6)
print(value, n_terms)
