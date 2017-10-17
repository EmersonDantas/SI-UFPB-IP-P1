resultado = 0
def binarioFlutuanteDecimal(lista, resultado):
	lista = lista.get()
	soma=0
	flut = 0
	lista = str(lista)
	lista = list(lista)
	ListaFlut=[]
	lista.reverse()
	ponto = False
	
	for x,i in enumerate(lista):
		if i == "." or i == ",":
			listaFlut = lista[:x]
			lista = lista[x+1:]
			ponto = True
			break

	if ponto == True:
		x = len(listaFlut)
		for i in listaFlut:
			if i == "1":
			  flut += int(i)*(1/(2**x))

		x-=1

	for x,i in enumerate(lista):
	  if i == "1":
	    soma += int(i)*2**x
	resultado['text'] = soma+flut
	
def decimalFlutuanteBinario(lista, resultado):
	lista = lista.get()
	ponto = False
	for x,i in enumerate(lista):
		if i == "." or i == ",":
			listaFlut = lista[x+1:]
			lista = lista[:x]
			ponto = True
			break

	quant = 10**len(listaFlut)
	listaFlut = float(listaFlut)/quant
	vetor2 = []

	if ponto == True:
		peg = int(listaFlut)


		while True:
			listaFlut = listaFlut*2
			peg = int(listaFlut)
			if peg == 0:
				vetor2.append(str(peg))
			elif peg == 1:
				vetor2.append(str(peg))
				inti = int(listaFlut)
				listaFlut -= inti

			if listaFlut == 0:
				break

	vet = "".join(vetor2)
	lista = int(lista)
	vetor = []
	
	while True:
		resto = lista%2
		lista = lista//2
		vetor.append(str(resto))

		if lista == 1 or lista == 0:
			vetor.append(str(lista))
			vetor.reverse()
			decimal="".join(vetor)
			res = decimal+"."+vet
			resultado['text'] = res
