nombres = ['Ana','Hugo','Valeria']
edades = [34,22,51]
ciudades = ['Madrid','Brasil','Mexico']

combinados = list(zip(nombres,edades,ciudades)) #combina las listas que querramos y las combierte en tuplas

print(combinados)

for nombre,edad,ciudad in combinados:
	print(f"{nombre} tiene {edad} años y vive en {ciudad}")

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinados = list(zip(paises,capitales))
for pais,capital in combinados:
    print(f"La capital de {pais} es {capital}")

marcas = ['Nike','Nissan','Samsung']
productos = ['Tenis','Sentra','Celular']

mi_zip = list(zip(marcas,productos))

num1 = ['uno','um','one']
num2 = ['dos','dois','two']
num3 = ['tres','três','three']
num4 = ['cuatro','quatro','four']
num5 = ['cinco','cinco','five']

numeros = num1+num2+num3+num4+num5

print(numeros)