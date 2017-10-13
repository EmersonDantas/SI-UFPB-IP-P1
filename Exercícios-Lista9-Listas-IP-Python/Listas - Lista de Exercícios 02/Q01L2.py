LA = [["Carol", 4], ["Pedro", 2], ["Laura", 3], ["Alice", 5], ["Luís", 4], ["Ludmila", 6]]
LB = [[7, 2, 5, 1], [9, 4, 3], [6, 8, 0, 2, 1], [4, 5, 10]]
print (LA[3][1] + LB[3][1])
print(LA[LB[0][1]][1] * LA[LB[2][2]][1])
for i in range(LB[1][1]):
    if (LA[i][1] >= 4):
        print(LA[i][0])