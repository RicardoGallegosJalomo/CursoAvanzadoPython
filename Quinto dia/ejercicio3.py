def ceros_vecinos(*args):

	contador = 0

	for num in args:

		if contador + 1 == len(args):
			return False

		elif args[contador] == 0 and args[contador + 1] == 0:
			return True
		else:
			contador += 1

	return False

print(ceros_vecinos(0,1,6,4,6,5,8,6,2,9,6,0))