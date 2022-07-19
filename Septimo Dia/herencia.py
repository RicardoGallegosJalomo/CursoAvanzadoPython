class Animal:

	def __init__(self, edad, color): # Atributos

		self.edad = edad
		self.color = color

	def nacer(self):
		print('Esta animal a nacido')

	def hablar(self):
		print('Este animal emite un sonido')

class Pajaro(Animal):

	def __init__(self,edad,color,altura_vuelo):
		super().__init__(edad,color)
		self.altura_vuelo = altura_vuelo

	def hablar(self): # metodo heredado pero modificado
		print('pio')

	def volar(self,metros):
		print(f'El pajaro vuela {metros} metros')



piolin = Pajaro(3,'amarillo',100)

mi_animal = Animal(5,'negro')

piolin.volar(50)

'''
class Vehiculo:
	def acelerar():
		pass 
	def frenar():
		pass 
class Automovil(Vehiculo):
	pass '''