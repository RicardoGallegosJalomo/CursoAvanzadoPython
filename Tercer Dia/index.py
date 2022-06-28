mi_texto = "Esta es una prueba"
resultado = mi_texto[4] # nos da el caracter que se encuentre en la posicion 4
resultado = mi_texto.index("a",5,19) #busca de derecha a izquierda empezando en la posicion 5 hasta la 19
resultado = mi_texto.rindex("a") # busca de izquierda a derecha

print(resultado)

frase = "En teoria, la teoria y la practica son los mismos. En la practica, no lo son."
resultado = frase.index("practica")
print(resultado)