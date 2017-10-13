def testaVogal(letra): #Testanto se o caractere informado é uma vogal
    vogal = ['a', 'e', 'i', 'o', 'u']
    if letra.isalpha():
        for i in range(len(vogal)):
            if letra == vogal[i]:
                return True
            else:
                return False
    else:
        return False

def calculaMaior(num1, num2):
    if num1 > num2:
        maior = num1
    else:
        maior = num2
    return maior

def testaMultiplo4(num):
    if num % 4 == 0:
        return True
    else:
        return False

def testaDivisor(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False