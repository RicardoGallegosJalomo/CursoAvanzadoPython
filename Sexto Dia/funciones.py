# Aqui se encuentran todas las funciones de la app Recetario
from pathlib import Path

import os

def categorias():

	os.system('cls')

	directory = 'C:/Users/Cassandra/Desktop/Ultimo Curso de Python/Sexto Dia/Recetas'
	with os.scandir(directory) as ficheros:
		subdirectorys = [fichero.name for fichero in ficheros if fichero.is_dir()]

	key = 0
	global cate

	while key != 6:

		print("*"*63)
		print("*"*20+ " Categorias de Recetas " + "*"*20)
		print("*"*63)

		num = 1
		for cat in subdirectorys:

			print(str([num])+" - "+cat)
			num += 1

		key = int(input("Elige una opcion de las Categorias.... ( 5 para salir )"))

		if key == 1:
			cate = subdirectorys[0]
			recetario1()
		elif key == 2:
			cate = subdirectorys[1]
			recetario1()
		elif key == 3:
			cate = subdirectorys[2]
			recetario1() 
		elif key == 4:
			cate = subdirectorys[3]
			recetario1()
		elif key >= 6:
			print("\n\n Opcion invalida vuelva a intentarlo...")
			keys = input("Presiones cualquier tecla para volver a intentarlo... ")
			os.system('cls')
		elif key == 5:
			os.system('cls')
			break


def categorias_crear_recetas():
	
	os.system('cls')

	directory = 'C:/Users/Cassandra/Desktop/Ultimo Curso de Python/Sexto Dia/Recetas'
	with os.scandir(directory) as ficheros:
		subdirectorys = [fichero.name for fichero in ficheros if fichero.is_dir()]

	key = 0
	global cate

	while key != 6:

		print("*"*63)
		print("*"*20+ " Categorias Crear Recetas " + "*"*20)
		print("*"*63)

		num = 1
		for cat in subdirectorys:

			print(str([num])+" - "+cat)
			num += 1

		key = int(input("Elige una opcion de las Categorias.... ( 5 para salir )"))

		if key == 1:
			cate = subdirectorys[0]
			crea_receta_op1()
		elif key == 2:
			cate = subdirectorys[1]
			crea_receta_op1()
		elif key == 3:
			cate = subdirectorys[2]
			crea_receta_op1() 
		elif key == 4:
			cate = subdirectorys[3]
			crea_receta_op1()
		elif key >= 6:
			print("\n\n Opcion invalida vuelva a intentarlo...")
			keys = input("Presiones cualquier tecla para volver a intentarlo... ")
			os.system('cls')
		elif key == 5:
			os.system('cls')
			break
			

def recetario1():
	os.system('cls')
	nume = 1
	directory = Path('C:/Users/Cassandra/Desktop/Ultimo Curso de Python/Sexto Dia/Recetas/',Path(cate))
	directory2 = directory.with_name(cate)
	receta_leer = []
	numero_lista = []

	while nume != 4:

		print("*"*63)
		print(f" Recetario de {cate} \n")
		print("*"*63)

		for txt in Path(directory).glob("**/*.*"): #Muestra todos los archivos txt de las carpetas y subcarpetas
			
			receta_con_ext = txt.name
			receta = txt.stem
			receta_leer.append(receta_con_ext)
			print(str([nume]) + " - " + receta)
			numero_lista.append(nume) 
			nume += 1
		
		numero_receta = int(input("\n Elija una receta para ver su contenido...: "))

		if numero_receta-1 == numero_lista.index(numero_receta):

			os.system('cls')
			print("si entre")
			texto_receta = receta_leer[numero_receta-1]
			directory = Path('C:/Users/Cassandra/Desktop/Ultimo Curso de Python/Sexto Dia/Recetas/',Path(cate),Path(texto_receta))
			
			if not directory.exists(): # Este medoto devuelve un booleano si el archivo existe 

				print("\n Este Archivo no Existe")
			else:
				
				print(directory.read_text())
				key = input("\n Oprima una tecla para continuar...")
				os.system('cls')
		elif numero_receta == 2:

			os.system('cls')
			texto_receta = receta_leer[1]
			directory = Path('C:/Users/Cassandra/Desktop/Ultimo Curso de Python/Sexto Dia/Recetas/',Path(cate),Path(texto_receta))
			
			if not directory.exists(): # Este medoto devuelve un booleano si el archivo existe 

				print("\n Este Archivo no Existe")
				key = input("\n Oprima una tecla para continuar...")
				os.system('cls')

			else:
				
				print(directory.read_text())
				key = input("\n Oprima una tecla para continuar...")
				os.system('cls')
		else:
			os.system('cls')
			print("\n La opcion no existe vuelva a intentarlo....")
			key = input("\n Oprima cualquie tecla para continuar...")
			os.system('cls') 
			nume = 1

def crea_receta_op1():
	os.system('cls')
	nume = 1
	directory = Path('C:/Users/Cassandra/Desktop/Ultimo Curso de Python/Sexto Dia/Recetas/',Path(cate))

	print("*"*63)
	print(f" Nueva Receta de la categoria {cate} \n")
	print("*"*63)

	nombre_receta = input("\n Elija un nombre para su receta...: ")
	nombre_receta = nombre_receta+".txt"
	archivo = open(Path(directory,Path(nombre_receta)),'w')

	contenido_receta = input("\n Escriba el contenido de su Receta...: ")
	archivo.write(contenido_receta)
	archivo.close()
	print(f"Tu receta se creo con exito en la categoria {cate} ")
	pause = input("\n Oprima cualquier tecla para continuar...")
	os.system('cls')

def recetario3():
	pass 
def recetario4():
	pass 