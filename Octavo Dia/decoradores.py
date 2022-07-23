'''def cambiar_letras(tipo):

	def mayuscula(texto):
		print(texto.upper())

	def minuscula(texto):
		print(texto.lower())


	if tipo == "may":
		return mayuscula
	elif tipo == "min":
		return minuscula

operacion = cambiar_letras("may")

operacion('palabra')'''


def decorar_saludo(funcion): # Esta funcion va a decorar cualquier funcion que le pasemos

	def otra_funcion(palabra):
		print("hola")
		funcion(palabra)
		print("adios")
	return otra_funcion

#@decorar_saludo     Decorador normal
def mayuscula(texto):
		print(texto.upper())

#@decorar_saludo     Decorador normal
def minuscula(texto):
	print(texto.lower())

minuscula("Python")

mayuscula_decorada = decorar_saludo(mayuscula) # Hace la funcion del decorador sin el decorador @

mayuscula_decorada('fede')