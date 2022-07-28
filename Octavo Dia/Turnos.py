'''
Despachador de Turnos para una Farmacia
'''

import funcionesTurnos

def pregunta():

	print(' Bienvenido a la Farmacia de Python \n')
	print(" A que área desea pasar? \n")

	while True:

		print("""                          Perfumeria [P] 
			  Farmacia   [F]
			  Cosmetica  [C]
			  \n""")

		try:

			mi_rubro = input("Eloja su robro: ").upper()

			["P","F","C"].index(mi_rubro)
		except ValueError:
			print("Esa no es una opcion valida")
		else:
			break

	funcionesTurnos.decorar_saludo(mi_rubro)

def inicio():

	while True:

		pregunta()

		try:
			otro_turno = input("Quieres sacar otro turno? [S/N]: ").upper()
			["S", "N"].index(otro_turno)
		except ValueError:
			print("Esa no es una opcion Valida... ")
		else:
			if otro_turno == "N":
				print("Gracias por su Visita...")
				break

inicio()