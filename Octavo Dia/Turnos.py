'''
Despachador de Turnos para una Farmacia
'''

#from funcionesTurnos import *


def saludo(funcion):

	def saludos_turnos():
		
		print("Su turno es")
		funcion(turno)
		print("Espere su turno")

	return saludos_turnos

def perfumeria(turno):

	yield turno = turno + 1

	print


opcion = ""

while True:

	print(' Bienvenido a la Farmacia de Python \n')
	print(" A que área desea pasar? \n")

	print(""" Perfumeria [P] 
			  Farmacia   [F]
			  Cosmetica  [C]
			  Salir      [S] \n""")

	opcion = input("A que área desea dirigirse... \n")

	if opcion == "P":

		turno = saludo(perfumeria) 
		turno(saludo)

	elif opcion == "F":
		pass 
	elif opcion == "C":
		pass 
	else:
		print("\n Gracias por su visita, Vuelva pronto...")
		break

