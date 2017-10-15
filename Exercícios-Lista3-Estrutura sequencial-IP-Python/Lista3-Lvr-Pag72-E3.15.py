#EMERSON DANTAS S.I-IP-P1
QCFPD=int(input('Quantos cigarros você fuma por dia?'))
QAF=int(input('Por quantos anos você fumou?'))
DP1=QCFPD*(QAF*365)#QUANTIDADE DE CIGARROS QUE ELE FUMOU NA VIDA
DP2=DP1*10#QUANTIDADE DE MINUTOS PERDIDOS
DP3=DP2/1440#DIAS PERDIDOS
print('Por ter fumado %d cigarros por dia, durante %d anos, você perdeu %d dias de vida.'%(QCFPD, QAF, DP3))
