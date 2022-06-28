def chequear_3_cifras(lista):

	lista_3_cifras = []

	for n in lista:
		if n in range(100,1000):
			lista_3_cifras.append(n)
		else:
			pass

	return lista_3_cifras

resultado = chequear_3_cifras([555,99,600])
print(resultado)

def todos_positivos(lista):

	lista_numeros = []

	for n in lista:
		if n > 0:
			lista_numeros.append(n)
		elif n < 0:
			lista_numeros.append(n)
		print(lista_numeros)
		

todos_positivos([1,2,3,4,5,-1])

#crear una funcion(sua_menores) que sume los numeros de una lista (alacenada en la variable lista_numeros)
#siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma

#Crean una funcion (cantidad_pares) que cuente la cantidad de numeros pares que existen en un alista
#(lista_numero), y devueva el resultado de dicha cuenta
