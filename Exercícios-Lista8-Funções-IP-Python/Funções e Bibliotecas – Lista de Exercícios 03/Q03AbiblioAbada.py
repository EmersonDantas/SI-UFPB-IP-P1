def calculaComissao(quantidade):
    return quantidade*0.07*80

def calculaBonus(quantidade):
    if quantidade > 50:
        return 70
    else:
        return 0
