def mi_funcion():
	lista = []

	for x in range(1,5):
		lista.append(x * 10)
	return lista

def mi_generador():
	
	for x in range(1,5):
		yield x * 10

print(mi_funcion())

g = mi_generador()

print(next(g))
print(next(g))

'''def mi_generador():
	x = 1
	yield x
	x +=1
	yield x

	x += 1

	yield x

g = mi_generador()

print(next(g))
print(next(g))
print(next(g))'''

'''def secuencia_infinita():

	num = 0

	while True:
		num +=1
		print(next(num))
		yield num

generador = secuencia_infinita()'''

'''def multiplos_siete():
    num = 1
    while True:
        yield 7*num
        num += 1
 
generador = multiplos_siete()

def mensaje():
    x = "Te quedan 3 vidas"
    yield x
    
    x = "Te quedan 2 vidas"
    yield x
 
    x = "Te queda 1 vida"
    yield x
    
    x = "Game Over"
    yield x
 
perder_vida = mensaje()'''