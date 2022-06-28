def suma(**kwargs):
	print(type(kwargs)) #devuelve un diccionario

suma(x=2,y=4,z=9)

def suma(**kwargs):

	total = 0

	for clave,valor in kwargs.items():
		print(f"{clave} = {valor}")

		total += valor

	return total

print(suma(x=2,y=4,z=9))

def prueba(num1,num2,*args,**kwargs):

	print(f"El primer valor es {num1}")
	print(f"El segundo valor es {num2}")

	for arg in args:
		print(f"arg = {arg}")

	for clave,valor in kwargs.items():
		print(f"{clave} = {valor}")

args = [100,200,300,400]
kwargs = {'x':'uno','y':'dos','z':'tres'}

prueba(12,24,*args,**kwargs)