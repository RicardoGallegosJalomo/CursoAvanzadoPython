from random import randint

def lanzar_dados():
	return randint(1,6),randint(1,6)


def evaluar_jugada(dado1,dado2):
	suma_dados = dado1 + dado2
	if suma_dados <= 6:
		return f'La suma de tus dados es {suma_dados}. Lamentablemente '
	elif suma_dados in range(6,10):
		return f'La suma de tus dados es {suma_dados}. tienes chance '
	elif suma_dados >= 10:
		return f'La suma de tus dados es {suma_dados}. jugada ganadora '


dado1,dado2 = lanzar_dados()

print(evaluar_jugada(dado1,dado2))