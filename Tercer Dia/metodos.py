texto = "Este es el texto de Federico"

resultado = texto.upper() #convierte todo el texto en mayusculas
resultado3 = texto[2].upper() #convierte solo la posicion 2 en mayusculas
resultado1 = texto.lower() #convierte todo el texto en minusculas
resultado4 = texto.split() #convierte el texto en una lista
resultado5 = texto.split("t") #convierte el texto en una lista tomando a la letra t como separador

print(resultado)
print(resultado3)
print(resultado1)
print(resultado4)
print(resultado5)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d]) # une el contenido de las variables a,b,c,d y coloca un espacio entre ellas
						# lo deja como una cadena o string abcd
print(e)

resultado7 = texto.find("s") #Busca un caracter en una cadena de texto en este caso la "s" y devuelve
							 #la posicion donde lo encuentra

print(resultado7)

resultado8 = texto.replace("texto","orale") # reemplaza un caracter o una palabra por otra en este caso
											# reemplaza "texto" por "orale"
resultado9 = texto.replace("e","y") #reemplaza todas las letras "e" por la "y"
print(resultado8)
print(resultado9)

print(texto.upper())

lista = ["La","legibilidad","cuenta."]
resul = " ".join(lista)
print(resul)

