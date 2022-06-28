def saludar_persona(nombre):
	print("hola " + nombre)

saludar_persona('Ricardo')


def cuadrado(un_numero):
    print(un_numero ** 2)

cuadrado(8)

def multiplicar(numero1,numero2):
	total = numero1*numero2
	return total

resultado = multiplicar(5,10)
print(resultado)

def potencia(base,exponente):
	resultado = base ** exponente
	print(resultado)
	return resultado

potencia(3,4)

def usd_a_eur(valor):
	dolares = valor * .90
	return dolares

usd_a_eur(20)

def invertir_palabra(palabra): # queda pendiente de resolver 
	
	palabra = palabra.split()
	print(palabra)
	#palabra.reverse()
	palabra = "".join(palabra).upper()
	print(palabra)

	return palabra

nombre = "nohtyp"
invertir_palabra(nombre)