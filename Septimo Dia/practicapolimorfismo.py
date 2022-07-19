
'''palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

objetos = palabra,lista,tupla

for num in objetos:
	print(len(num))
'''
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

personajes = Arquero(),Mago(),Samurai()

for ataque in personajes:
	ataque.atacar()