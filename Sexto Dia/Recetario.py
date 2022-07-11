import os
from funciones import categorias_crear_recetas,categorias

os.system('cls')

opcion = 0

while opcion != 6:

	print("*" * 130)
	print("*" * 50 + " BIENVENIDOS A SUS RECETARIOS " + "*" * 50)
	print("*" * 130)

	print("[1] - Leer Receta ")
	print("[2] - Crear Receta ")
	print("[3] - Crear Categoria ")
	print("[4] - Eliminar Receta ")
	print("[5] - Eliminar Categoria ")
	print("[6] - Finalizar Programa")

	opcion = input("Elija una Opcion.....: ")
	key = ""

	if not opcion.isdigit():
		print("\n\n Opcion invalida vuelva a intentarlo...")
		key = input("Presiones cualquier tecla para volver a intentarlo... ")
	else:
		if int(opcion) == 1:
			categorias()
		elif int(opcion) == 2:
			categorias_crear_recetas()
		elif int(opcion) == 3:
			pass 
		elif int(opcion) == 4:
			pass 
		elif int(opcion) == 5:
			pass 
		elif int(opcion) >= 7:
			print("\n\n Opcion invalida vuelva a intentarlo...")
			key = input("Presiones cualquier tecla para volver a intentarlo... ")
		else:
			os.system('cls')
			print("Hasta Luego y gracias por usar nuestro recetario... ")
			break

	os.system('cls')


