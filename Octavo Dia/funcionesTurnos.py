'''
Funciones de la maquina de Turnos
'''

def saludo(funcion):

	def saludos_turnos():
		
		print("Su turno es")
		funcion(turno)
		print("Espere su turno")

	return saludos_turnos

def perfumeria(turno):

	yield turno += 1

	print


