archivo = open("prueba1.txt",'w') # 's' solo lectura,'w' escritura,'a'escritura a partir de la ultima
								 # linea
'''archivo.write('bienvenido') # si se utiliza la 'a' escribe en el archivo al final
archivo.write("soy el nuevo texto\n") # Salto de linea al final
archivo.write("""hola
	mundo
	como
	estas""") # Genera un salto de linea escribe el texto en diferente linea
archivo.writelines(['Hola','Mundo','aqui','estoy']) # Escribe en una linea sin espacios entrepalabras

lista = ['Hola','Mundo','aqui','estoy']

for p in lista:

	archivo.writelines(p + '\n')
'''
archivo = open("prueba1.txt",'a')
archivo.write('Otro texto Mejorado ejorado')
archivo.close()
archivo = open("prueba1.txt",'r')
print(archivo.read())


archivo.close()