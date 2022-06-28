from random import shuffle

# Lista inicial

palitos = ['-','--','---','----']

#Funcion mezclar palitos

def mezclar(lista):
	shuffle(lista)
	return lista

#Funcion Pedir intento de elegir

def probar_suerte():
	intento = ''

	while intento not in ['1','2','3','4']:
		intento = input("Elige un nuero del 1 al 4: ")

	return int(intento)

#Funcion comprobar el intento 1,2,3,...9

def chequear_intento(lista,intento):
	if lista[intento - 1] == "-":
		print("A lavar los platos")
	else:
		print("Esta vez te has salvado")

	print(f"Te a tocado {lista[intento-1]}")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)

