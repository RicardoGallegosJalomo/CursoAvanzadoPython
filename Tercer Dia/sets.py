miset = set([1,2,3,4,5])
print(type(miset))
print(len(miset)) # nos da el tamaño de nuestro set

print(2 in miset) # nos devuelve un booleano osea True o False si se encuentra en este caso el 2

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2) # sirve para unir dos sets

print(s3)
s1.add(4) # adiciona un elemento al set
s1.remove(3) # remueve de el set el elemento que esta dentro del parentesis
s1.discard(6) #descarta el elemento del set que esta dentro del parentesis
s1.pop() # en este caso elimina al azar un elemento del set
s1.clear() # vacia el set
print(s1)



otroset = {1,2,3}
print(otroset)
print(type(otroset))

print(miset)