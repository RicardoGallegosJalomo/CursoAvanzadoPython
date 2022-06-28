'''def suma(*args):
	total = 0

	for arg in args:
		total += arg
	return total

print(suma(5,6,9,8,7,45,9,6,5,889,6))
'''
def suma_cuadrados(*args):

	total = 0

	for arg in args:
		total += arg**2

	return total

print(suma_cuadrados(1,2,3))