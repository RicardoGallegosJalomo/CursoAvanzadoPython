'''
Funciones de la maquina de Turnos
'''

def decorar_saludo(rubro):

	print("\n " + "*" * 23)
	print("Su numero es: ")
	
	if rubro == "P":
		print(next(perfum))
	elif rubro == "F":
		print(next(farma))
	else:
		print(next(cosme))

	print("Espere y sera Atendido")
	print("*" * 23 + "\n ")


def perfumeria():
	for n in range(1,100):
		yield f"P - {n}"

def farmacia():
	for n in range(1,100):
		yield f"F - {n}"

def cosmetica():
	for n in range(1,100):
		yield f"C - {n}"

perfum = perfumeria()
farma = farmacia()
cosme = cosmetica()

