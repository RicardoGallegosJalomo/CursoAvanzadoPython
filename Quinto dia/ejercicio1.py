
def devolver_distintos(num1,num2,num3):
	lista = [num1,num2,num3]
	suma = num1+num2+num3

	if suma > 15:

		mayor15 = max(lista)
		print(f'La suma es mayor a 15 es ---> {mayor15} y la suma es {suma}')

	elif suma < 10:

		menor10 = min(lista)
		print(f'La suma es menor a 10 es ---> {menor10} y la suma es {suma}')

	elif suma >10 and suma < 15:

		print(f'La suma esta entre 10 y 15 es ---> {suma}')

devolver_distintos(8,6,4)