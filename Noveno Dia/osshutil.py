import os
import shutil
import send2trash

'''archivo = open('curso.txt', 'w')
archivo.write("Esto es una prueba")
archivo.close()

print(os.listdir()) # Lista los archivos que tenemos dentro del directorio donde nos econtramos'''

#shutil.move('curso.txt',"C:\\Users\\Cassandra\\Desktop") # mueve el archivo .txt a la ruta especificada

#send2trash.send2trash('curso.txt') # Elimina archivos 

ruta = 'C:\\Users\\Cassandra\\Desktop\\Ultimo Curso de Python'

for carpeta,subcarpeta,archivo in os.walk(ruta):
	print(f'En la carpeta : {carpeta}')
	print(f'Las subcarpetas son : ')
	for sub in subcarpeta:
		print(f'\t {sub}')
	print(f'Los archivos son :')
	for arch in archivo:
		print(f'\t {arch}')
	print('\n')