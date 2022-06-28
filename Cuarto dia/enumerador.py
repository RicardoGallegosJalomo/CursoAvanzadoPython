lista = ['a','b','c']
indice = 0

#for item in lista: # modo tradicional
#	print(indice,item)
#	indice += 1

#for item in enumerate(lista):
#	print(item)

#mis_tuples = list(enumerate(lista))

#print(mis_tuples)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
tupla = list(enumerate(lista_nombres))
print(tupla)

for indice,nombre in enumerate(lista_nombres):
	print(f'{nombre} se encuentra en el indice {indice}')
	

