menor = min(58,30,98,23,84)
mayor = max(58,30,98,23,84)

print(menor)
print(mayor)

lista = [58,30,98,23,84]
print(max(lista))
print(f'El menor es {min(lista)} y el mayor es {max(lista)} ')

nombres = ['juan','pablo','alicia','carlos']

print(min(nombres))

nombre = "Carlos"

print(min(nombre))

dic = {'c1': 45,'c2':11}

print(min(dic)) #Imprime la clave c1
print(min(dic.values())) #Imprime el valor menos en este caso 11

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)
print(valor_maximo)

lista_numeros1 = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

minimo = min(lista_numeros1)
maximo = max(lista_numeros1)
rango = maximo - minimo

print(rango)

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)

print(edad_minima)
print(ultimo_nombre)