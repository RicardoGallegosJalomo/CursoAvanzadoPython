mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
otra_lista = ["Hola",55,55.66]

resultado = len(mi_lista) #obtiene el largo de la lista

resultado = mi_lista[0] # Obtiene el contenido de la posicion 0 de la lista
resultado1 = mi_lista[0:1] #Obtiene el contenido desde la posicion 0 hasta la posicion 1
resultado2 = mi_lista[0:] #Obtiene el contenido desde la posicion 0 hasta el final de la lista
resultado3 = mi_lista + mi_lista2 #concatena las dos listas

print(type(mi_lista))
print(resultado)
print(resultado3)

resultado3[0] = "Beta" #Reemplaza el contenido de la posicion 0 de la tabla

print(resultado3)

resultado3.append('g') #Adiciona un nuevo elemento a la lista
resultado3.pop() #Si se deja vacio los parentesis interpreta que se quiere eliminar el ultimo
				 # elemento de la lista
resultado3.pop(0) #Elimina el elemento de la lista de la posicion indicada en este caso la 0
eliminado = resultado3.pop(0) # Asi se guarda el elemento elimindado de la lista en una variable

print(resultado3)

lista =['g','o','m','c']

lista.sort() # ordena la lista en orden alfabetico

lista.reverse() # ordena la lista de atras para adelante o en orden inverso

print(lista)

frutas = ["manzana","banana","mango","cereza","sandia"]
frutas.pop(2)
eliminado = frutas
print(eliminado)