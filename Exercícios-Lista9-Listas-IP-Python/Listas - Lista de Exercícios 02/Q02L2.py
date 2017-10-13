LA = [["Carol", 4], ["Pedro", 2], ["Laura", 3], ["Alice", 5], ["Luís", 4], ["Ludmila", 6]]
LB = [[7, 2, 5, 1], [9, 4, 3], [6, 8, 0, 2, 1], [4, 5, 10]]
LA[1][1] = 3
LA.append(['Bruno',1])
LB[2].append(7)
print(LA)
print(LB)
for i in range(len(LA)):
    if LA[i][1] < 4:
        print(LA[i][0])
for a in range(len(LB)):
    print(LB[a][0])
