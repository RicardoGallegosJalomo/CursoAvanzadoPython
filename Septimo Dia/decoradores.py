class Pajaro:

	alas = True # atributo de clase

	def __init__(self,color,especie):
		self.color = color					#atributos de instancia
		self.especie = especie

	def piar(self):
		print('pio, mi color es {}'.format(self.color))

	def volar(self,metros):
		print(f'El pajaro a volado {metros} metros')
		self.piar()

	def pintar_negro(self):
		self.color = 'negro'
		print(f'Ahora el pajaro es {self.color}')

	@clasmethod
	def poner_huevos(cls,cantidad):
		print(f'puso {cantidad} huevos')
		cls.alas = False
		print(Pajaro.alas)

	@staticmethod
	def mirar():
		print("El pajaro mira")


piolin = Pajaro('amarillo','canario')


