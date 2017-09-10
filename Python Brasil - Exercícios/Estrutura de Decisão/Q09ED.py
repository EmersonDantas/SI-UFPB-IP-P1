num1 = float(input('Digite o primeiro número:\n'))
num2 = float(input('Digite o segundo número:\n'))
num3 = float(input('Digite o terceiro número:\n'))
if num1 < num2:
    num1,num2 = num2,num1
if num1 < num3:
    num1,num3 = num3,num1
if num2 < num3:
    num2,num3 = num3,num2
print(num1,num2,num3)
