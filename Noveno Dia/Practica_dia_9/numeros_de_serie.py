import re 
import os 
import time
import datetime
import math
from pathlib import Path

inicio = time.time()

ruta = 'C:\\Users\\Cassandra\\Desktop\\Ultimo Curso de Python\\Noveno Dia\\Practica_dia_9\\Mi_Gran_Directorio'
mi_patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
numeros_encontrados = []
archivo_encotrados = []

def buscar_numero(archivo,patron):
	este_archivo = open(archivo,'r')
	texto = este_archivo.read()
	if re.search(patron,texto):
		return re.search(patron,texto)
	else:
		return ''

def crear_listas():
	for carpeta,subcarpeta,archivo in os.walk(ruta):
		for a in archivo:
			resultado = buscar_numero(Path(carpeta, a),mi_patron)
			if resultado != '':
				numeros_encontrados.append(resultado.group())
				archivo_encotrados.append(a.title())

def mostrar_todo():
	indice = 0
	print('-'*50)
	print(f'Fecha de busqueda : {hoy.day}/{hoy.month}/{hoy.year}')
	print('\n')
	print('ARCHIVO\t\t\tNUM. SERIE')
	print('-------\t\t\t----------')
	for a in archivo_encotrados:
		print(f'{a}\t{numeros_encontrados[indice]}')
		indice += 1
	print('\n')
	print(f'Numeros encotrados : {len(numeros_encontrados)}')
	fin = time.time()

	duracion = fin - inicio
	print(f'Duracion de la busqueda : {math.ceil(duracion)} segundos')
	print('-'*50)

crear_listas()
mostrar_todo()