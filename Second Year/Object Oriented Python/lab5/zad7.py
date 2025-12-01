def permute(items):
    if len(items) == 0:
        return
    if len(items) == 1:
        yield tuple(items)
        return

    for i in range(len(items)):
        current = items[i]
        rest = items[:i] + items[i+1:]
        for p in permute(rest):
            yield (current,) + p

for p in permute([1, 2, 3]):
    print(p)
