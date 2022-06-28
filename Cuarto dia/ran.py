from random import randint

aleatorio = randint(1,50)
print(aleatorio)

from random import *

aleatorio = randint(1,50) # imprime un numero entre 1 y 50 aleatoriamente
print(aleatorio)

aleatorio = round(uniform(1,5),1) # imprime un numero decimal entre 1 y 5 aleatoriamente
print(aleatorio)

aleatorio = random() # Imprime un numero float enre 0 y 1 aleatoriamente
print(aleatorio)

colores = ['azul','verde','rojo','amarillo']
aleatorio = choice(colores)
print(aleatorio) # Imprime un elemento de la lista aleatoriamento

numeros = list(range(5,50,5))

shuffle(numeros) # imprime los numeros entre 5 y 50 de 5 en 5 aleatoriamente
print(numeros)