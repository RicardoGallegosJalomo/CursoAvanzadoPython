import random

print("Este es el juego del ahorcado sin ahorcado")
print("\n Descurbre cual es la PALABRA escondida")
print("\n Tienes solo 6 oportunidades para hacerlo")
print("\n Que te Diviertas y Mucha Suerte....")

vidas = 6

def pedir_letra(self):

	self.letra = input("\n Escribe una letra....: ").lower()
	validar_letra()

def validar_letra():

	if letra.isalpha():
		
	else:
		print("Ese no es un caracter valido.....")
		print("Intentalo de Nuevo......")
		pedir_letra()

def chequear_letra(letra):

	palabra = random.choice(["gato","perro","habitacion","casa","lavadero"])

	busca_letra = palabra.find(letra)

	if busca_letra > 0:		

		for n in palabra:

			print("_",end=" ")

		pedir_letra()

	else:

		vidas -= 1
		print(f"Lo siento la letra no existe pierdes una vida te quedan {vidas} vidas")

chequear_letra()