'''O if da linha 4 deverá ser substituido por elif(pdf)'''
#correção
rendaAnual = float (input())
if (rendaAnual <= 12000):
    imposto = 0
elif (rendaAnual > 60000):
    imposto = rendaAnual*0.07
else:
    imposto = rendaAnual*0.03
print(imposto)
