from random import *

import os

number_machine = randint(1,100)
cont = 0

while cont <= 8:

	os.system ("cls") 

	print("                        Adivinale el número a la maquina... ")
	print("                              Solo tienes 8 intentos")
	number = int(input("\nEscribe el número....: "))

	if number < 1 or number > 100:
		print("\nEl número esta fuera de rango debe ser entre 1 y 100")
	elif number < number_machine:
		print("\nEl número capturado es menor al de la maquina")
	elif number > number_machine:
		print("\nEl numero capturado es mayor al de la maquina")
	elif number == number_machine:
		print(f"\n     Acertaste el número al {cont} intento....F E L I C I D A D E S.....")
		print(f"\n                   Fin del Juego Hasta la Vista")
		break
	option = input("\n            Desea intentarlo de nuevo.....")

	if option == "s":
		cont += 1
		#continue
	elif option == "n":
		print("\n                        Suerte para la proxima")
		break

	if cont == 8:
		print("\n             Lo sentimos se agotaron tus oportunidades...")
		#os.system ("cls") 
		break