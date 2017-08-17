#EMERSON DANTAS S.I IP-P1
QP = int(input('Quantas pessoas:'))
QO = int(QP / 42)#1.92
QOR = QP % 42 #39
QV = int(QOR / 20)#1.95
QVR = QOR % 20 #19
if QVR <= 20:
    QV = QV + 1
VO = QO * 350
VV = QV * 200
VT = (VO + VV) / QP
print('{QO} ônibus e {QV} van(s)\nR${VT:.2f} por pessoa.'.format(QO=QO,QV=int(QV), VT=VT))