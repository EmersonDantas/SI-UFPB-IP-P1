n = int(input('N:\n'))
s = 0
m = 1
for i in range(1,n+1):
    s += i/m
    m += 2
print(s)
