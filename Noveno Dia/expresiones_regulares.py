import re


'''texto = 'si necesitas ayuda llama al (658)-598-9977 las 24 horas obtiene ayuda '

palabra = 'ayuda' in texto
print(palabra)


patron = "ayuda"'''

'''busqueda = re.search(patron, texto) # Busca la palabra nada que esta dentro de patron en el texto

print(busqueda.span()) # Nos da la posicion de la palabra buscada

print(busqueda.start()) # Nos da la posicion del comienzo de la palabra

print(busqueda.end()) # Nos da la ubicacion de la posicion final de la palabra buscada
'''

#busqueda = re.findall(patron, texto) # Nos da las veces que se repite la palabra en una lista ['ayuda','ayuda']

#print(busqueda)

'''for hallazgo in re.finditer(patron, texto):
	print(hallazgo.span())'''

'''texto = 'llama al 564-564-9988 ya mismo'
 
 patron = r'\d\d\d-\d\d\d-\d\d\d\d' #cadena especial con la r al principio
 patron1 = r'\d{3}-\d{3}-\d{4}' # modo cuantificadores
 patron1 = r'(\d{3})-(\d{3})-(\d{4})' #Se forma grupos 
 
 
 resultado = re.search(patron, texto)
 resultado1 = re.search(patron1, texto)
 
 print(resultado.group()) # Se obtiene en este caso el telefono solamente
 print(resultado1.group(2)) # Imprimie lo que haya en la posicion 2 del grupo''' 

'''clave = input("Clave :")

patron = r'\D{1}\w{7}' # En este patron la primera letra debe ser mayuscula y las otras 7 alfanumericas

chequear = re.search(patron, clave)

print(chequear)'''

texto = 'No atendemos los lunes por la tarde'

buscar = re.search(r'lunes|martes',texto) # busca lunes o martes
buscar = re.search(r'....demos....',texto)
buscar = re.search(r'^\D',texto) # busca un no digito(numero) al inicio del texto
buscar = re.search(r'\D$',texto) # busca un no digito(numero) al final del texto
buscar = re.findall(r'[^\s]',texto) # lo que se pone adentro de las llaves lo tiene que excluir

print(buscar)