res = 1
Sos = ['Windows Server','Unix','Linux','Netware','Mac OS','Outro']
lisPont = [0,0,0,0,0,0]
while res != 0:
    res = int(input('Qual o melhor Sistema Operacional para uso em servidores?\n'
                    '0- para parar\n'
                    '1- Windows Server\n'
                    '2- Unix\n'
                    '3- Linux\n'
                    '4- Netware\n'
                    '5- Mac OS\n'
                    '6- Outro\n'))
    if res != 0:
        lisPont[res-1] += 1

    print()

tot = sum(lisPont)
print('******************* R E S U L T A D O **************************')
for i,so in enumerate(Sos):
    print('{} : {} : {:.0f}%'.format(so,lisPont[i],lisPont[i]*100/tot))
