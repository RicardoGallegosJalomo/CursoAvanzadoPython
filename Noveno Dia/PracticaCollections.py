import collections
from collections import Counter,defaultdict,deque

'''lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)

print(contador)

defaultdict
mi_diccionario  = defaultdict(lambda: 'Valor no hallado')
mi_diccionario['edad'] = 44
print(mi_diccionario)'''

# deque : Nos permite adicionar por derecha o izquierda elementos a la lista y tambien eliminarlos
# por ambos lados

lista = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

lista_ciudades = collections.deque(lista)

lista_ciudades.appendleft("Mexico")

print(lista_ciudades)

lista_ciudades.append("Penjamo")

print(lista_ciudades)

lista_ciudades.pop()

print(lista_ciudades)

lista_ciudades.popleft()

print(lista_ciudades)