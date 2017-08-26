#EMERSON DANTAS S.I IP-P1
QP = int(input('Quantas pessoas:'))
QO = QP // 42
QOR = QP % 42
QV = QOR // 20
QVR = QOR % 20
if QVR <= 20:
    QV += 1
VO = QO * 350
VV = QV * 200
VT = (VO + VV) / QP
if QV >= 1 and QO <= 0:
    print('{QV} van(s)\nR${VT:.2f} por pessoa.'.format(QV=QV, VT=VT))
elif QO >=1 and QV <= 0:
    print('{QO} ônibus\nR${VT:.2f} por pessoa.'.format(QO=QO, VT=VT))
else:
    print('{QO} ônibus e {QV} van(s)\nR${VT:.2f} por pessoa.'.format(QO=QO,QV=int(QV), VT=VT))
