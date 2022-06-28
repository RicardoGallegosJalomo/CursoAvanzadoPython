'''nombre = ['Juan','Ana','Carlos','Belen','fran']
for elemento in nombre:
	print("hola" + " " + elemento)

lista1 = ['a','b','c']

for letra in lista1:
	numero_letra = lista1.index(letra) + 1
	print(f"Letra {numero_letra}: {letra}")

lista = ['pablo','laura','fede','luis','julia']

for nombre in lista:
	if nombre.startswith('l'):
		print(nombre)

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
	mi_valor = mi_valor + numero

print(mi_valor)

palabra = 'python'

for letra in palabra:
	print(letra)

for a,b in [[1,2],[3,4],[5,6],[6,7]]:
	print(a)
	print(b)

dic = {'clave1':'a','clave2':'b','clave3':'c'}

for item in dic: # Imprime solo clave1, clave2, clave 2
	print(item) 

dic = {'clave1':'a','clave2':'b','clave3':'c'}

for item in dic.values(): # imprime los valores del dic
	print(item)

dic = {'clave1':'a','clave2':'b','clave3':'c'}

for item in dic.items(): # imprime los valores del dic
	print(item)

dic = {'clave1':'a','clave2':'b','clave3':'c'}

for a,b in dic.items(): # imprime los valores del dic con sus items clave1,clave2, clave3
	print(a,b) '''

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
	if numero %2 == 0:
		suma_pares = suma_pares + numero
	elif numero %2 != 0:
		suma_impares = suma_impares + numero
print(suma_pares)
print(suma_impares)