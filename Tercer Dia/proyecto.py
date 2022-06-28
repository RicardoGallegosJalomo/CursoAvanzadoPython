'''texto = input("Ingresa un Texto Largo...: ")

letra1 = input("Ingresa una Letra a su eleccion...: ")
letra2 = input("Ingresa una Letra a su eleccion...: ")
letra3 = input("Ingresa una Letra a su eleccion...: ")

texto_lista = texto.split(":")

print(type(texto_lista))

resultado = texto.find(letra1)

print(resultado)

#cuantas veces cada una de las letras que escribio pasando todas las letras a minusculas
# decir al usuario cuantas palabras hay en todo el texto
#primera y ultima letra
# invertir el orden de las palabras 
# decir si la palabra python esta dentro del texto

lista_texto = []
lista_texto.append(letra1)
lista_texto.append(letra2)
lista_texto.append(letra3)

print(type(lista_texto))
print(lista_texto)'''

texto = input("Ingresa un texto a Eleccion : ")
letras = []

texto = texto.lower()

letras.append(input("Ingresa la primera Letra : ").lower())
letras.append(input("Ingresa la segunda Letra : ").lower())
letras.append(input("Ingresa la tercera Letra : ").lower())

print("\n")

print("Cantidad de Letras")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}'' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}'' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}'' repetida {cantidad_letras3} veces")

print("\n")

print("Cantidad de Palabras")

palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print("\n")

print("Letras de Inicio y Fin")

letra_inicio = texto[0]
letra_final = texto[-1]

print(f"La primeraletra de tu texto es '{letra_inicio}'' y la letra final es '{letra_final}' ")

print("\n")

print("Texto Invertido")

palabras.reverse()
texto_invertido = ' '.join(palabras)

print(f"Si ordenamos tu texto al reves va a decir '{texto_invertido}' ")

print("\n")

print("Buscando la Palabra Python")

buscar_python = 'python' in texto

dic = {True:"si",False:"no"}

print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto ")