# UFPB IV - SI
# Emerson Dantas - MATRICULA: 20170050755 - emerson.ruan@dce.ufpb.br - github.com/emersondantas
# Francivaldo Napoleão - MATRICULA: 20170050610 - francivaldo.napoleao@dce.ufpb.br - github.com/NapoleaoHerculano
# coding: utf-8
# outubro/2017
# Projeto - Damas Chinesas

import time

def logoSI():
    LimparTela()

    logo = [['                         ,AAAAAAA.              "AA                                     '],
            ['                     .AAAAAAAAAAAAAAA.          AAAAAAA                                 '],
            ['                 AAAAAAAAAAAAAAAAAAAAAAAA       AAAAAAAAAAA                             '],
            ['               CCAAAAAAAAAAAAAAAAAAAAAAAAA      AAAAAAAAAAAAAA                          '],
            ['               CCCCCAAAAAAAAAAAAAAAAAAA"        AAAAAAAAAAAAAAA                         '],
            ['               CCCCCCCCCAAAAAAAAAA!"            AAAAAAAAAAAAAAA                         '],
            ['               CCCCCCCCCCCCCAAA"                CAAAAAAAAAAAAAA                         '],
            ['               CCCCCCCCCCCCCCCCC                CCCAAAAAAAAAAAA                         '],
            ['               CCCCCCCCCCCCCCCCCCCCC            CCCCCC3AAAAAAAA                         '],
            ['               CCCCCCCCCCCCCCCCCCCCCCCCC        CCCCCCCCCC%AAAA                         '],
            ['               CCCCCCCCCCCCCCCCCCCCCCCCCCCC=    CCCCCCCCCCCCCC$                         '],
            ['                   CCCCCCCCCCCCCCCCCCCCCCCCC    CCCCCCCCCCCCCCC                         '],
            ['                       CCCCCCCCCCCCCCCCCCCCC    CCCCCCCCCCCCCCC                         '],
            ['                           CCCCCCCCCCCCCCCCC    CCCCCCCCCCCCCCC                         '],
            ['                           AAAACCCCCCCCCCCCC    CCCCCCCCCCCCCCC                         '],
            ['                       AAAAAAAAAAAACCCCCCCCC    CCCCCCCCCCCCCCC                         '],
            ['                   AAAAAAAAAAAAAAAAAAAACCCCC    CCCCCCCCCCCCCCC                         '],
            ['                AAAAAAAAAAAAAAAAAAAAAAAAAACC    CCCCCCCCCCCCCCC                         '],
            ['                 "AAAAAAAAAAAAAAAAAAAAAA"        "CCCCCCCCCCCCC                         '],
            ['                     "AAAAAAAAAAAAAA"                "CCCCCCCCC                         '],
            ['                         "AAAAAA"                        "CCCCC                         ']]


    for i, linha in enumerate(logo):
        for x in linha:
            print(25 * ' ',x, end = '')
        print()
        time.sleep(0.05)
    print(10 * '\n')
    time.sleep(2)
    LimparTela()


def MenuInicial():
    logoSI()
    instrucoes = [['╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗'],
                  ['║                                                           Damas Chinesas                                                           ║'],
                  ['║ By: Emerson Dantas; Francivaldo Napoleão                                       OBS.: Jogar no termial ou na IDE(não jogue no IDLE) ║'],
                  ['╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝'],
                  ['╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗'],
                  ['║                                                             Instruções:                                                            ║'],
                  ['║                                                                                                                                    ║'],
                  ['║            O tabuleiro contém 121 casas, e possui o formato da estrela de Davi (6 pontas). Cada uma das casas faz vizinhança       ║'],
                  ['║        com 6 outras casas (exceto as casas que ficam na borda do tabuleiro, que podem fazer vizinhança com 2, 4 ou 5 casas).       ║'],
                  ['║        -Cada jogador tem 10 peças ao seu dispor. Ao começar o jogo, estas 10 peças de um jogador estão juntas em um dos tri-       ║'],
                  ['║        ângulos que formam as pontas das estrelas. Cada equipe de 10 peças tem uma coloração diferente que distingue de outro       ║'],
                  ['║        jogador. - Só deve haver uma peça por casa.                                                                                 ║'],
                  ['║                                                                                                                                    ║'],
                  ['║                                                              Objetivo:                                                             ║'],
                  ['║                                                                                                                                    ║'],
                  ['║                                        É ser o primeiro a movimentar as peças até o triangulo oposto.                              ║'],
                  ['║                                                                                                                                    ║'],
                  ['║                                                       Movimentos permitidos:                                                       ║'],
                  ['║                                                                                                                                    ║'],
                  ['║        Como no jogo clássico de damas, cada jogador deve mover somente uma peça por turno. Um movimento é válido quando:           ║'],
                  ['║                                                                                                                                    ║'],
                  ['║                *Há uma casa adjacente livre;                                                                                       ║'],
                  ['║                *Saltando uma casa adjacente ocupada por outra peça (seja própria ou do adversário), e colocando na casa se-        ║'],
                  ['║                 guinte (na mesma direção) se está livre. Vários saltos seguidos podem ocorrer de uma só vez se a disposição        ║'],
                  ['║                 das peças permitir;                                                                                                ║'],
                  ['║                                                                                                                                    ║'],
                  ['║        OBS.: **Todas as peças permanecem até o fim do jogo (ao contrário do jogo de damas tradicional).                            ║'],
                  ['╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝']]

    for x,linha in enumerate(instrucoes): # Printa cada linha da instrução com efeito delay
        if x == 4: # Quando completar o nome do jogo, esperar 5 segundos
            time.sleep(3)
        print(linha[0])
        time.sleep(0.05) # Printar cada linha da lista instrucoes com delay de 0.05s

    print()
    tempo = 0.05
    ImprimirTabuleiro(CriarTabuleiro(), tempo) # Imprime o tabuleiro, como exemplo

    print()

    input('Entendido? Digite ENTER para continuar...') # Verifica se o jogador(ou grupo de jogadores) leram as instruções

    print()

    return RecebeJogadores() #Chama a função que recebe o numero de jogadores
    

def RecebeJogadores():
    # Recebe a quantidade de jogadores e verifica se é veridica
    quantidadeJogadores = input('Digite o número de jogadores:\n(2, 3, 4 ou 6): ')
    if quantidadeJogadores.isdigit(): # Verifica se a string é somente número
        quantidadeJogadores = int(quantidadeJogadores) # Muda a variavel de string para int
        jogadores = []
        if quantidadeJogadores >= 2 and quantidadeJogadores <= 6 and quantidadeJogadores != 5: # Verifica se o número satisfaz as regras do jogo
            for indice in range(quantidadeJogadores): # Recebe o nome dos jogadores e garda em uma lista
                while True:
                    jogador = str(input('Qual o nome do jogador {}:\n'.format(indice + 1)))
                    if len(jogador) <= 23: #Limite para o nome do jogador
                        jogadores.append(jogador)
                        break
                    else:
                        print('\033[1;31mNome muito grande! Escreva um nome menor.\033[m\n')

            return jogadores # Retorna a lista com nome dos jogadores

        else:
            print('\033[1;31mNúmero de jogadores inválido!\033[m\n')
            return RecebeJogadores() #Chama recursivamente a mesma função

    else:
        print('\033[1;31mEntrada inválida!\033[m\n')
        return RecebeJogadores() #Chama recursivamente a mesma função


def LimparTela(): # Pula 50 linhas
    print(50 * '\n')

def CriarTabuleiro(): # Cria uma lista com listas contendo 'O's de acordo com o formato da
                      # estrela, é somente uma lista com outras listas dentro, não contem espaços ou números
    tabuleiro = []
    # CIMA - Crista da estrela
    for linha in range(4):
        tabuleiro.append([])
        for coluna in range(linha + 1):
            tabuleiro[len(tabuleiro)-1].append("O")
    # MEIO A - Parte do meio superior, inclusive a linha meio
    for linha in range(13,8,-1):
        tabuleiro.append([])
        for coluna in range(linha):
            tabuleiro[len(tabuleiro)-1].append("O")
    # MEIO B - Parte do meio inferior
    for linha in range(10,14):
        tabuleiro.append([])
        for coluna in range(linha):
            tabuleiro[len(tabuleiro)-1].append("O")
    # BAIXO - Parte inferior
    for linha in range(4,0,-1):
        tabuleiro.append([])
        for coluna in range(linha):
            tabuleiro[len(tabuleiro)-1].append("O")

    return tabuleiro

def ImprimirLinhaComEspaco(tabuleiro, linha, espaco): # Recebe os dados a ser impresso, linha por linha
    print(50 * ' ',linha + 1, espaco * ' ', end = '') # Printa: 50 linhas(para deixar a estrela no meio), o numero da linha e a quantidade de espaços para formar a estrela, tudo sem pular linha.
    for linha in tabuleiro[linha]: # Entra na linha do tabuleiro, 'linha' recebe os 'O's e printa cada um sem pular linha
        print(linha, end = ' ')
    print() #Pula uma linha

def ImprimirTabuleiro(tabuleiro, tempo): # Manda os dados para serem impressos, linha por linha
    espaco = [13,12,11,10,1,2,3,4,5,3,2,1,0,9,10,11,12] # Quantidade de espaços para deixar a estrela bunitinha :3
    for linha in range(len(tabuleiro)): # Um for com range 17, que é a quantidade de linhas que o tabuleiro tem
        ImprimirLinhaComEspaco(tabuleiro, linha, espaco[linha]) # Chama a função e manda os dados necessários para ela printar a linha
        time.sleep(tempo) # Efeito visual de delay
