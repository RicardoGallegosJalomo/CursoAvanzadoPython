from pathlib import Path
import os

ruta = os.getcwd() #obtiene el directorio de trabajo actual

ruta = os.chdir('C:\\Users\\Cassandra\\Desktop\\Prueba') # permite cambiar de directorio como CD\

archivo = open('prueba.txt')

ruta = os.makedirs('C:\\Users\\Cassandra\\Desktop\\Prueba\\otra') # sirve para crear directorios como MD

ruta = 'C:\\Users\\Cassandra\\Desktop\\Ultimo Curso de Python\\Sexto Dia\\prueba.txt'

elemento = os.path.basename(ruta) # obtiene el nombre de base de nuestra ruta en este caso devolvera PRUEBA.TXT
print(elemento)
elemento = os.path.dirname(ruta) # obtiene toda la ruta de los directorios

elemento = os.path.split(ruta) # obtiene toda la ruta y el archivo pero los pasa a una tupla

#os.rmdir('C:\\Users\\Cassandra\\Desktop\\Prueba\\otra') # Borra un directorio

otro_archivo = open('C:\\Users\\Cassandra\\Desktop\\Ultimo Curso de Python\\Sexto Dia\\prueba.txt')

print(otro_archivo.read())

print(elemento)

#print(archivo.read())

carpeta = Path('C:/Users/Cassandra/Desktop/Prueba') # Esta forma sirve para cualquier SO 
archivo = carpeta  / 'prueba.txt' # Concatena la ruta + el archivo que se desea obtener

mi_archivo = open(archivo)
print(mi_archivo.read())