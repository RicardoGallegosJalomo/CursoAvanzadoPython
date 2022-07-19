class Pajaro:

	alas = True # atributo de clase

	def __init__(self,color,especie):
		self.color = color					#atributos de instancia
		self.especie = especie

	def piar(self):
		print('pio, mi color es {}'.format(self.color))

	def volar(self,metros):
		print(f'El pajaro a volado {metros} metros')

piolin = Pajaro('amarillo','canario')

piolin.piar()
piolin.volar(50)

Herencia

Polimorfismo

Cohesión

Acoplamiento

Abstracción

Encapsulamiento