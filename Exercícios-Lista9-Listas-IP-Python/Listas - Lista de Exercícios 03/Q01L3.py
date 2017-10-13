quant = 5
Lista = []
for i in range(quant):
    x = i + 2
    Lista.append(x)#[2,3,4,5,6]
print(Lista)
for i in range(quant):
    if (Lista[i] % 2 == 0):
        Lista[i] = Lista[i] + 3

print(Lista)
#[5,3,7,5,9]
print(Lista[3] * 2)
#10
print(Lista[0] - Lista [4])
#-4