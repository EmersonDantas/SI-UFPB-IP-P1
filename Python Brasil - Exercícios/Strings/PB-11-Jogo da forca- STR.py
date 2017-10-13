import random
palavras = ['agua','chocolate','bacon','python','linux','UFPB','hidratado']
palavra = str.upper(palavras[random.randint(0,len(palavras)-1)])
tracos = []
usados = []
erros = 6
acertos = 0

for i in range(len(palavra)):
    tracos.append('_')

def visual():
    for a in range(len(tracos)):
        print(tracos[a],end=' ')
    print()

print('Jogo da forca')

while erros != 0:
    tentativa = str.upper(input('Qual o seu palpite:\n'))

    if tentativa in palavra and tentativa not in usados and tentativa.isalpha():
        for i in range(len(palavra)):
            if palavra[i] == tentativa :
                tracos[i] = tentativa
                usados.append(tentativa)
                acertos += 1

        print('\nPARABÉNS, está quase lá!\nA palavra é:')
        visual()

        if acertos == len(palavra):
            print('\nVocê acertou a palavra!')
            break

    else:
        erros -= 1
        print('Você errou!\nVocê pode errar mais {} vezes.\n'.format(erros))
