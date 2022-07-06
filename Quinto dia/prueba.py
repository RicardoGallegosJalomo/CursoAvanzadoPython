import random

palabra = random.choice(["gato","perro","habitacion","casa","lavadero"])

longitud = len(palabra)

for n in palabra:

	print("_",end=" ")	

print(palabra)