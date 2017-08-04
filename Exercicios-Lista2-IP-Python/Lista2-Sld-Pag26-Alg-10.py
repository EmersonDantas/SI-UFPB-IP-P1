SEGD= 67000
if SEGD >= 60:
    MIN=SEGD/60
    SEG=SEGD%60
else :
    print('Duração:',SEGD,'s')
if MIN >= 60:
    HOR=MIN/60
    MINF=MIN%60
    print(int(HOR),'h''\n',int(MINF),'m''\n',int(SEG),'s')
else :
    print('Duração:', int(MIN),'m')
    




