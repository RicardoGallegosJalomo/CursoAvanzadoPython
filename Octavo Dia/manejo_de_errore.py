def suma():
	n1 = int(input("numero 1 : "))
	n2 = int(input("numero 2 : "))

	print(n1+n2)
	print("Gracias por sumar")

	
try:   # Si no hay error has esto
	suma()
except: # Si hay un error
	print("Algo no a Salido Bien")
else:
	print("Hiciste todo bien")
finally:
	print("Eso fue todo")


def pedir_numero():

	while True:
		try:
			numero = int(input("Ingresa un numero : "))
		except:
			print('Error ese no es un número')
		else:
			print(f'Ingresaste el número {numero}')
			break
	print("gracias...")

pedir_numero()
