def jogoDeCraps():
    return random.jogo(2,12)

continuar = True
while continuar:
    res = jogoDeCraps()
    if res == 7 or res == 11:
        print('Você ganhou!')
        
    
