def flatten(seq):
    for elem in seq:
        if isinstance(elem, (list, tuple)) and not isinstance(elem, (str, bytes)):
            yield from flatten(elem)
        else:
            yield elem


data = ([1, 'kot'], 3, (4, 5, [7, 8, 9]))

result = list(flatten(data))
print(result)
