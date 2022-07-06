mi_archivo = open('prueba.txt')

#print(mi_archivo.read())  #lee lo que tnga todo el archivo
#print(mi_archivo.readline().rstrip()) # lee solo la primera linea del archivo y quita el salto de linea
									  # siguiente
'''
for linea in mi_archivo:
	print("Aqui dice: " + linea)
'''
todas = mi_archivo.readlines()

todas = todas.pop(1)

print(todas)

mi_archivo.close()