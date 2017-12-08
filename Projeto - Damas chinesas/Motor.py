# UFPB IV - SI
# Emerson Dantas - MATRICULA: 20170050755 - emerson.ruan@dce.ufpb.br - github.com/emersondantas
# Francivaldo Napoleão - MATRICULA: 20170050610 - francivaldo.napoleao@dce.ufpb.br - github.com/NapoleaoHerculano
# coding: utf-8
# outubro/2017
# Projeto - Damas Chinesas

from GUI import *


def AdicionarPecas(tabuleiro, quantidadeJogadores):  # Adiciona peças ao tabuleiro de acordo com a quantidade de jogadores.
    if quantidadeJogadores == 2:
        TwoPlayers(tabuleiro)  # Chama a função que edita o tabuleiro para 2 jogadores

    elif quantidadeJogadores == 3:
        ThreePlayers(tabuleiro)  # Chama a função que edita o tabuleiro para 3 jogadores

    elif quantidadeJogadores == 4:
        ForPlayers(tabuleiro)  # Chama a função que edita o tabuleiro para 4 jogadores

    elif quantidadeJogadores == 6:
        SixPlayers(tabuleiro)  # Chama a função que edita o tabuleiro para 6 jogadores

    return tabuleiro


def TwoPlayers(tabuleiro):  # Função que edita o tabuleiro para 2 jogadores.
    for a, linha in enumerate(tabuleiro[0:4]):  # Esse for, assim como nos proximos, entra no tabuleiro nas linhas especificadas
        for x, letra in enumerate(linha):  # Esse for entra na linha do outro for e edita string por string com a letra e cor escolhida abaixo
            tabuleiro[a][x] = '\033[1;31mA\033[m'  # Esse codigo ANSI é para mudar a cor da 'Peça' do jogador, cada jogador tem uma cor.

    for b, linha in enumerate(tabuleiro[13:17]):  # o range do for esta sendo armazenado em letras (Ex.: a, b, c...). As letras estão diferentes só por estética :P
        for x, letra in enumerate(linha):
            tabuleiro[b + 13][x] = '\033[1;32mB\033[m'


def ThreePlayers(tabuleiro):
    TwoPlayers(tabuleiro)  # Chama a função que edita o tabuleiro para 2 jogadores

    controle = 3  # controla quantos letras serão substituidas na vertical, a cada linha. Nos outros o numero de controle é diferente, com execeções.
    for c, linha in enumerate(tabuleiro[4:8]):  # E edita para +1
        for x, letra in enumerate(linha):
            if x <= controle:
                tabuleiro[c + 4][x] = '\033[1;33mC\033[m'

        controle -= 1


def ForPlayers(tabuleiro):  # Função que edita o tabuleiro para 4 jogadores.
    TwoPlayers(tabuleiro)  # Chama a função que edita o tabuleiro para 2 jogadores e edita para +2

    controle = 3
    for c, linha in enumerate(tabuleiro[4:8]):  # +1 jogador
        for x, letra in enumerate(linha):
            if x <= controle:
                tabuleiro[c + 4][x] = '\033[1;33mC\033[m'

        controle -= 1

    controle = 9
    for d, linha in enumerate(tabuleiro[9:13]):  # +1 jogador
        for x, letra in enumerate(linha):
            if x >= controle:
                tabuleiro[d + 9][x] = '\033[1;34mD\033[m'


def SixPlayers(tabuleiro):  # Função que edita o tabuleiro para 6 jogadores.
    ForPlayers(tabuleiro)  # Chama a função que edita o tabuleiro para 4 jogadores e edita para +2

    controle = 9
    for e, linha in enumerate(tabuleiro[4:8]):  # +1 jogador
        for x, letra in enumerate(linha):
            if x >= controle:
                tabuleiro[e + 4][x] = '\033[1;35mE\033[m'

    controle = 0
    for f, linha in enumerate(tabuleiro[9:13]):  # +1 jogador
        for x, letra in enumerate(linha):
            if x <= controle:
                tabuleiro[f + 9][x] = '\033[1;36mF\033[m'

        controle += 1


def ImprimeJogadoresETabuleiro(tabuleiro, dadosJogadores, vencedores):  # Printa o nome dos jogadores com suas cores, e o tabuleiro
    LimparTela()
    print('╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗', end = '')
    for i in range(len(dadosJogadores)):# Esse for printa o nome dos jogadores com suas cores especificas, sua letra, quantidade de passos e caso tenham vencido, sua colocação.
        print('\n║ Jogador {}: {};{}N° de jogadas: {}{}║'.format(dadosJogadores[i][1], dadosJogadores[i][0], (35 - len(dadosJogadores[i][0])) * ' ', dadosJogadores[i][2], 78 * ' '), end='')
    for a in range(len(vencedores)):
        print('\n║ Jogador {}: {};{}N° de jogadas: {} |-> {}° a ganhar!{}║'.format(vencedores[a][1], vencedores[a][0], (35 - len(vencedores[a][0])) * ' ', vencedores[a][2], vencedores[a][3], 61 * ' '), end='')
    print('╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝', end = '')

    print((11 - (len(dadosJogadores) + len(vencedores))) * '\n')  # Pula 12 linhas
    tempo = 0
    ImprimirTabuleiro(tabuleiro,tempo)  # Imprime o tabuleiro editado conforme o número de jogadores e os movimentos feitos
    print(7  * '\n')  # Pula 8 linhas


def IniciarJogo():  # Função que inicia o jogo
    vencedores = []
    jogadores = MenuInicial()
    LimparTela()
    players = ['A', 'B', 'C', 'D', 'E', 'F']
    tabuleiro = CriarTabuleiro()  # Chama o tabuleiro não formatado
    tabuleiro = AdicionarPecas(tabuleiro, len(jogadores))  # Edita e retorna o tabuleiro formatado com peças

    dadosJogadores = []
    for i in range(len(jogadores)):  # adiciona a uma lista com listas contendo: nome do jogador, letra do jogador. Ambas formatadas com cor
        jogador = '\033[1;3{}m{}\033[m'.format(i + 1, jogadores[i])  # colorindo o nome do jogador
        letraCor = '\033[1;3{}m{}\033[m'.format(i + 1, players[i])  # colorindo a letra do jogador
        dadosJogadores.append([jogador, letraCor, 0, 0, 0])  # Aqui é adicionado uma lista contendo o nome do jogador e sua letra na lista dadosJogadores

    ImprimeJogadoresETabuleiro(tabuleiro, dadosJogadores, vencedores)  # Chama a função pra printar
    JogadorDaVez(tabuleiro, dadosJogadores, vencedores)  # Recebe a localização da peça a mover


def JogadorDaVez(tabuleiro, dadosJogadores, vencedores):  # Recebe a localização da peça a mover
    quantidadeJogadores = len(dadosJogadores)

    for jogador in range(len(dadosJogadores)):  # Pede e testa a posição. Jogador por jogador.
        CondicaoDeGanhador(tabuleiro, dadosJogadores, vencedores)
        if len(vencedores) < (quantidadeJogadores - 1):
            erro = ''

            RecebePeca(tabuleiro, dadosJogadores, erro, jogador, vencedores)

        else: #Se todos os jogadores menos o ultimo ganharam, o jogo acaba, é mostrada a mensagem de ganhador e o jogo reinicia
            MensagemDeGanhador(tabuleiro, dadosJogadores, vencedores)
            IniciarJogo()

    JogadorDaVez(tabuleiro, dadosJogadores, vencedores)


def RecebePeca(tabuleiro, dadosJogadores, erro, jogador, vencedores):

    local = str(input('{}\n'
                      '\033[1;3{}m╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\033[m'
                      '\033[1;3{}m║\033[m \033[1;33mDireção: l = left, r = right, ul = up left, ur = up right, dl = down left, dr = down right.\033[m                                        \033[1;3{}m║\033[m\n'
                      '\033[1;3{}m║\033[m Jogador {}: {}, qual a linha, peça e a posição que você dejesa mover no formato: linha-posiçãoNaLinha-Direção:{}\033[1;3{}m║\033[m\n'
                      '\033[1;3{}m╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝\033[m\n'
                      .format(erro, jogador + 1, jogador + 1, jogador + 1, jogador + 1,dadosJogadores[jogador - len(vencedores)][1], dadosJogadores[jogador - len(vencedores)][0], (34 - len(dadosJogadores[jogador - len(vencedores)][0])) * ' ', jogador + 1, jogador + 1)))
    
    orientacao = ValidaPecaEscolhida(dadosJogadores, tabuleiro, local, jogador)  # Verifica se a posição é verdadeira,  retorna um valor booleano
    validaPosicaoInicial = orientacao[0]

    if validaPosicaoInicial == True: #Se a posição inicial for válida, entra
        linhaInicial, colunaInicial, direcao = orientacao[1], orientacao[2], orientacao[3]
        dadosParaSalto = DaLinhaEColunaFinais(tabuleiro, linhaInicial, colunaInicial, direcao)
        validaPosicaoFinal = dadosParaSalto[0]

        if validaPosicaoFinal == True: #Se a posição final for válida, entra
            linhaFinal, colunaFinal = dadosParaSalto[1], dadosParaSalto[2]
            validaSalto = VerificaMudancaDePeca(tabuleiro, linhaFinal, colunaFinal)

            if validaSalto == True: #Se o salto for válido, entra
                MudaPeca(tabuleiro, linhaInicial, linhaFinal, colunaInicial, colunaFinal, jogador, dadosJogadores)
                LimparTela()   # Só Limpa
                ImprimeJogadoresETabuleiro(tabuleiro, dadosJogadores, vencedores)

            else:
                ImprimeJogadoresETabuleiro(tabuleiro, dadosJogadores, vencedores)
                erro = '\033[1;31mSalto Inválido!, Escolha um salto válido.\033[m'
                return RecebePeca(tabuleiro, dadosJogadores, erro, jogador, vencedores)

        else:
            ImprimeJogadoresETabuleiro(tabuleiro, dadosJogadores, vencedores)
            erro = '\033[1;31mDireção Inválida!, Escreva uma direção válida.\033[m'
            return RecebePeca(tabuleiro, dadosJogadores, erro, jogador, vencedores)

    else:
        ImprimeJogadoresETabuleiro(tabuleiro, dadosJogadores, vencedores)
        erro = '\033[1;31mlocal Inválido!, Escreva o local corretamente.\033[m'
        return RecebePeca(tabuleiro, dadosJogadores, erro, jogador, vencedores)

def ValidaPecaEscolhida(dadosJogadores, tabuleiro, local, jogador): #Verifica a peça inicial
    quantidadeTracos = 0
    dados = [False] #Se não for uma posição válida, retornara o valor inicial, que é False

    for caractere in local:  # Verifica quantos - há no local
        if caractere == '-':
            quantidadeTracos += 1

    if quantidadeTracos >= 2: #Verifica a quantidade de tracos
        cordenadas, listaPassos = SeparaSaltosEPosicaoinicial(local) #Separa os saltos da posição inicial
        linha, coluna = cordenadas.split('-')

        if linha.isdigit() and coluna.isdigit():  # Verifica se são int
            linha, coluna = int(linha), int(coluna)  # Muda para int
            if 1 <= linha <= 17:
                if 1 <= coluna <= len(tabuleiro[linha - 1]): #Se a posição é maior que 1 e menor que as colunas da linha inicial
                    if tabuleiro[linha - 1][coluna - 1] == dadosJogadores[jogador][1]:  # Se a linha e posição escolhida estiver a mesma letra do jogador
                        dados = [True, linha, coluna, listaPassos]

    return dados


def SeparaSaltosEPosicaoinicial(local): #Separa a posição inicial dos passos
    quantidadeTracos = 0
    for i,caractere in enumerate(local): #Se orienta pelos traços
        if caractere == '-':
            quantidadeTracos += 1

        if quantidadeTracos == 2 and caractere == '-': #Quando a quantidade de traços for 2, separa os passos e as cordenadas
            passos = local[i+1:]
            cordenadas = local[0:i] #Posição Inicial
            listaPassos = (passos.split('-'))
            break

    return cordenadas, listaPassos


def DaLinhaEColunaFinais(tabuleiro, linhaInicial, colunaInicial, listaPassos): #Da a linha e coluna finais, com salto simples ou composto
    linhaFinal = linhaInicial
    colunaFinal = colunaInicial
    controleColuna = 4 #Deslocamento
    salto = 1 #Se for se deslocar para +1 ou -1
    validador = True #Inicialmente
    
    if len(listaPassos) >= 2: #Verifica se o salto é composto
        saltoComposto = True
    else:
        saltoComposto = False

    for direcao in listaPassos: #Testa cada passo, inclusive se houver sómente um
        tentativa = 0 #Cada tentativa de passo será contada
        direcao = str.lower(direcao)
        verificarPasso = True #Para iniciar os testes

        while verificarPasso: #Testa o passo carregado no for
            if direcao == 'l' and colunaInicial > 1: # Se a direção for l e a coluna inicial for maior que 1, retorna colina final
                colunaFinal = colunaInicial - salto

            elif direcao == 'r' and colunaInicial < len(tabuleiro[linhaFinal - 1]): # Se a direção for r e a coluna inicial for maior que a quantidade de elementos na linha atual, retorna colina final
                colunaFinal = colunaInicial + salto

            elif direcao == 'ul': # Se a direção for ul
                linhaFinal = linhaInicial - salto # faz subir de linha

                if linhaInicial == 5 and 6 <= colunaInicial <= 9: # CASO ESPECIAL, a coluna inicial precisa estar entre 6 e 9 e usar o controle de coluna
                    colunaFinal = colunaInicial - controleColuna - salto

                elif linhaInicial == 14: #CASO ESPECIAL, na linha 14 é preciso usar o controle de coluna
                    colunaFinal = colunaInicial + controleColuna

                elif (1 <= linhaInicial <= 4 or 10 <= linhaInicial <= 13) and colunaInicial > 1: #Caso padrão: linhas de 1 a 4 ou 10 a 13 tendo coluna inicial maior que 1. Parte /\ da estrela
                    colunaFinal = colunaInicial - salto

                elif 6 <= linhaInicial <= 9 or 15 <= linhaInicial <= 17: #Caso padrão: linhas de 6 a 9 ou 15 a 17. Parte \/ da estrela
                    colunaFinal = colunaInicial

                else:
                    validador = False #Para todos, se não se enquadrar em um salto válido, o validador será False

            elif direcao == 'ur':
                linhaFinal = linhaInicial - salto # faz subir de linha
                if linhaInicial == 5 and 5 <= colunaInicial <= 8: # CASO ESPECIAL, a coluna inicial precisa estar entre 5 e 8 e usar o controle de coluna
                    colunaFinal = colunaInicial - controleColuna

                elif linhaInicial == 14: #CASO ESPECIAL, na linha 14 é preciso usar o controle de coluna
                    colunaFinal = colunaInicial + salto + controleColuna

                elif (1 <= linhaInicial <= 4 or 10 <= linhaInicial <= 13) and colunaInicial <= len(tabuleiro[linhaFinal - 1]): #Caso padrão: linhas de 1 a 4 ou 10 a 13 tendo coluna inicial menor que a quantidade de elementos na linha inicial. Parte /\ da estrela
                    colunaFinal = colunaInicial

                elif 15 <= linhaInicial <= 17 or 6 <= linhaInicial <= 9: #Caso padrão: linhas de 6 a 9 ou 15 a 17. Parte \/ da estrela
                    colunaFinal = colunaInicial + salto

                else:
                    validador = False #Para todos, se não se enquadrar em um salto válido, o validador será False

            elif direcao == 'dl':
                linhaFinal = linhaInicial + salto # faz descer de linha

                if linhaInicial == 4: #CASO ESPECIAL, na linha 4 é preciso usar o controle de coluna
                    colunaFinal = colunaInicial + controleColuna

                elif linhaInicial == 13 and 6 <= colunaInicial <= 9: #CASO ESPECIAL, na linha 13 é preciso usar o controle de coluna e a coluna deve estar entre 6 e 9
                    colunaFinal = colunaInicial - controleColuna - salto

                elif 1 <= linhaInicial <= 3 or 9 <= linhaInicial <= 12: #Caso padrão: linhas de 1 a 3 ou 9 a 12. Parte /\ da estrela
                    colunaFinal = colunaInicial

                elif (5 <= linhaInicial <= 8 or 14 <= linhaInicial <= 17) and colunaInicial > 1: #Caso padrão: linhas de 5 a 8 ou 14 a 17 com coluna inicial > 1. Parte \/ da estrela
                    colunaFinal = colunaInicial - salto

                else:
                    validador = False #Para todos, se não se enquadrar em um salto válido, o validador será False

            elif direcao == 'dr':
                linhaFinal = linhaInicial + salto # faz descer de linha
                if linhaInicial == 4: #CASO ESPECIAL, na linha 4 é preciso usar o controle de coluna
                    colunaFinal = colunaInicial + salto + controleColuna

                elif linhaInicial == 13 and 5 <= colunaInicial <= 8: #CASO ESPECIAL, na linha 13 é preciso usar o controle de coluna e a coluna inicial deve estar entre 5 e 8
                    colunaFinal = colunaInicial - controleColuna

                elif 1 <= linhaInicial <= 3 or 9 <= linhaInicial <= 12: #Caso padrão: linhas de 1 a 3 ou 9 a 12. Parte /\ da estrela
                    colunaFinal = colunaInicial + salto

                elif (5 <= linhaInicial <= 8 or 14 <= linhaInicial <= 17) and colunaInicial < len(tabuleiro[linhaInicial - 1]): #Caso padrão: linhas de 5 a 8 ou 14 a 17 com coluna inicial < que a quantidade de elementos na linha inicial. Parte \/ da estrela
                    colunaFinal = colunaInicial

                else:
                    validador = False #Para todos, se não se enquadrar em um salto válido, o validador será False

            else:
                validador = False #Para todos, se não se enquadrar em um salto válido, o validador será False

            tentativa += 1 #A cada tentativa, será acrescentado 1 a tentativa
            if validador == True and tentativa <= 2: #Se for uma direção válida, e a tentaiva for menor que 2
                testePecaFinal = VerificaMudancaDePeca(tabuleiro, linhaFinal, colunaFinal) #Verifica se a peça final é uma peça vazia 'O'

                if testePecaFinal == True: #Se sim, entra.
                    if saltoComposto == True: #Se for salto composto
                        if tentativa == 1: #Se, no salto composto, der certo o primeiro pulo simples, então o salto composto é inválido.
                            validador = False
                            return [validador, linhaFinal, colunaFinal]
                        else: #Se for mais de uma tentativa, ele tenta denovo, dentro do limite de 2 tentativas
                            verificarPasso = False
                            linhaInicial, colunaInicial = linhaFinal, colunaFinal
                    else: #Se o salto não for composto, quebra o while e retorna os dados
                        verificarPasso = False
                else: #Se a peça final não for vazia, tenta denovo
                    linhaInicial, colunaInicial = linhaFinal, colunaFinal        
            else: #Se não for um passo válido ou tiver tentado mais de 2 vezes ele retorna passo inválido
                validador = False
                return [validador, linhaFinal, colunaFinal]

    return [validador, linhaFinal, colunaFinal] #Se der tudo certo, ele retorna aqui


def VerificaMudancaDePeca(tabuleiro, linhaFinal, colunaFinal): #Verifica se a proxima peça é um lugar vazio
    if tabuleiro[linhaFinal - 1][colunaFinal - 1] == 'O':
        valida = True
    else:
        valida = False

    return valida


def MudaPeca(tabuleiro, linhaInicial, linhaFinal, colunaInicial, colunaFinal, jogador, dadosJogadores): #Muda a peça e conta, no jogador, quantas peças ele mudou
    tabuleiro[linhaFinal - 1][colunaFinal - 1] = tabuleiro[linhaInicial - 1][colunaInicial - 1]
    tabuleiro[linhaInicial - 1][colunaInicial - 1] = 'O'
    dadosJogadores[jogador][2] += 1


def CondicaoDeGanhador(tabuleiro, dadosJogadores, vencedores): #Testa se os estremos da estrela estão ocupados pelas peças que dão a condição de vencedor
    totalJogadores = len(dadosJogadores) + len(vencedores)

    for jogador in dadosJogadores: #Limpa os testes
        jogador[4] = 0

    
    for a, linha in enumerate(tabuleiro[0:4]): #Parte A da estrela
        for x, letraTabuleiro in enumerate(linha):
            if letraTabuleiro == '\033[1;32mB\033[m':
                dadosJogadores[1][4] += 1
    
    for b, linha in enumerate(tabuleiro[13:17]): #Parte B da estrela
        for x, letraTabuleiro in enumerate(linha):
            if letraTabuleiro == '\033[1;31mA\033[m':
                dadosJogadores[0][4] += 1

            elif letraTabuleiro == '\033[1;33mC\033[m' and totalJogadores == 3:
                dadosJogadores[2][4] += 1
    
    controle = 3
    for c, linha in enumerate(tabuleiro[4:8]): #Parte C da estrela
        for x, letraTabuleiro in enumerate(linha):
            if x <= controle:
                if letraTabuleiro == '\033[1;34mD\033[m':
                    dadosJogadores[3][4] += 1
                elif letraTabuleiro == '\033[1;32mB\033[m' and totalJogadores == 3:
                    dadosJogadores[1][4] += 1

        controle -= 1

    controle = 9
    for d, linha in enumerate(tabuleiro[9:13]): #Parte D da estrela
        for x, letraTabuleiro in enumerate(linha):
            if x >= controle:
                if letraTabuleiro == '\033[1;33mC\033[m':
                    dadosJogadores[2][4] += 1

    controle = 9
    for e, linha in enumerate(tabuleiro[4:8]): #Parte E da estrela
        for x, letraTabuleiro in enumerate(linha):
            if x >= controle:
                if letraTabuleiro == '\033[1;36mF\033[m':
                    dadosJogadores[5][4] += 1

    controle = 0
    for f, linha in enumerate(tabuleiro[9:13]): #Parte F da estrela
        for x, letraTabuleiro in enumerate(linha):
            if x <= controle:
                if letraTabuleiro == '\033[1;35mE\033[m':
                    dadosJogadores[4][4] += 1

        controle += 1

    for i,quantidade in enumerate(dadosJogadores): #Testa quantas partes estão com todas as peças certas
        if quantidade[4] >= 10:
            quantidadeGanhadores = len(vencedores) + 1
            dadosJogadores[i][3] = quantidadeGanhadores
            vencedores.append(dadosJogadores[i])
            del dadosJogadores[i]


def MensagemDeGanhador(tabuleiro, dadosJogadores, vencedores): #Mensagem que aparecerá quando todos vencerem
    LimparTela()
    
    ImprimeJogadoresETabuleiro(tabuleiro, dadosJogadores, vencedores)
    print('\n\n\033[1;32m╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\033[m'
          '\033[1;32m║\033[m                                                            \033[1;33mFIM DE JOGO!\033[m                                                            \033[1;32m║\033[m\n'
          '\033[1;32m╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝\033[m')
    time.sleep(5)

    imagem = [['▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄'],
              ['░░░░ ░░░░▀█▄▀▄▀██████░▀█▄▀▄▀████▀'],
              ['░░░ ░░░░░░░▀█▄█▄███▀░░░▀██▄█▄█▀']]

    for i, linha in enumerate(imagem): #printa cada caractere de cada linha com delay 
        for x in linha:
            print(50 * ' ',x , end = '')
        print()
        time.sleep(0.5)

    for i,jogador in enumerate(vencedores): # Printa a colocação dos jogadores
        print('\n{}{}°: jogador {}:{} quantidade de saltos: {}'.format(51 * ' ', i + 1, vencedores[i][1], vencedores[i][0], vencedores[i][2]))
        time.sleep(0.5)

    print('\n{}{}°: jogador {}:{} quantidade de saltos: {}'.format(51 * ' ', len(vencedores) + 1, dadosJogadores[0][1], dadosJogadores[0][0], dadosJogadores[0][2]))
    time.sleep(0.5)

    print('\n{}Parabéns jogador {}, {}\n{}Você ganhou em 1° lugar!'.format(51 * ' ',vencedores[0][1], vencedores[0][0], 60 * ' ')) #Primeiro lugar
    time.sleep(0.5)

    for i in range(30):
        print()
        time.sleep(0.5)

    time.sleep(15) 