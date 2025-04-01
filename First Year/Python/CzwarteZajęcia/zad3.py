matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
list1 = []
list2 = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

for i in range(len(matrix[0])):
    temp = []
    for j in range(len(matrix)):
        temp.append(matrix[j][i])
    list1.append(temp)

print(list1)
print(list2)