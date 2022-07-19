class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("ja ja")

    def hablar(self):
        print("Que tal")

class Hijo(Padre,Madre):
    pass

class Nieto(Hijo):
    def hablar(self):
        print("Soy el nieto")

mi_nieto = Nieto()
mi_nieto.reir()
mi_nieto.hablar()