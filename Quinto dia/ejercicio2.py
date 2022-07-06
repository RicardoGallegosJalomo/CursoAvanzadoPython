def letras_sin_repetir(nombre):

	mi_set = set()
	
	for letra in nombre:

		mi_set.add(letra)

	mi_lista = list(mi_set)
	mi_lista.sort()
	print(mi_lista)
		

letras_sin_repetir("parangaricutirimicuaro")
