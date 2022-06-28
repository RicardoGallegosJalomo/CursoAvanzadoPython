palabra = 'python'

lista = []

for letra in palabra:	# llena la lista con cada letra de la palabra
	lista.append(letra)

print(lista)

palabra1 = 'Python'

lista1 = [letra for letra in palabra1] # llena la lista con cada letra de la palabra simplificado

print(lista1)

listan = [n for n in range(0,21,2)]
print(listan)
listaf = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]
print(listaf)

pies = [10,20,30,40,50]
metros = [p * 3.8281 for p in pies]

print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [cua ** 2 for cua in valores]
print(valores_cuadrado)

valores1 = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares = [par for par in valores1 if par/2 == 0]
print(valores_pares)

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(c - 32)*(5/9) for c in temperatura_fahrenheit]
print(grados_celsius)