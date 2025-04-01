vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list1 = []
list2 = [j for sub in vec for j in sub]

for i in vec:
    for j in i:
        list1.append(j)

print(list1)
print(list2)

