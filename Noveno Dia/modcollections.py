from collections import Counter,defaultdict,namedtuple

numeros = [8,6,5,6,7,6,8,9,1,2,2,1,3,4,3,4,3] 

print(Counter(numeros)) # Nos imprime cuantas veces se repite cada numero de la lista
						# en un tipo diccionario(subclase de diccionario)

print(Counter('parangaricutirimicuaro')) # Nos imprime cuantas veces se repite cada letra de la lista
										 # en un tipo diccionario(subclase de diccionario)

frase = 'Al pan pan y al vino vino'
print(Counter(frase.split())) # Split separa las palabras por los espacion

serie = Counter([1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4])

print(serie.most_common()) # Muestra el mas comun en este caso imprime todos 
						   # para elegir el mas comun se pone el numero de aparicion (1 o el 2)


print(list(serie)) # Nos muestra los elementos de serie [1,2,3,4]

mi_dic = defaultdict(lambda: 'nada') #si no existe algun valor pedido imprime 'nada'

mi_dic['uno'] = 'verde'
print(mi_dic['dos'])
print(mi_dic)

mi_tupla = [500,18,65]

print(mi_tupla[1])

Persona = namedtuple('Persona',['nombre','altura','peso']) #Nos permite poner nombre a los elementos
														   # de la lista

ariel = Persona('Ariel',1.70,80)

print(ariel.peso)
print(ariel[1])