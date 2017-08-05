#EMERSON DANTAS S.I-IP-P1
QCFPD=int(input('Quantos cigarros você fuma por dia?'))
QAF=int(input('Por quantos anos você fumou?'))
DP1=QCFPD*QAF
DP2=DP1*10
DP3=DP2/1440
print('Por ter fumado %d cigarros por dia, durante %d anos, você perdeu %d dias de vida.'%(QCFPD, QAF, DP3))
