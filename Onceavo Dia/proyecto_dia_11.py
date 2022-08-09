import bs4
import requests

# Exploramos varias paginas dentro de un WEB SITE

url_base = 'http://books.toscrape.com/catalogue/page-{}.html' # Guardamos la url sin numero de pagina

# Lista de titulos con 4 o 5 estrellas

titulos_rating_alto = []

#iterar paginas

for pagina in range(1,51):

	#crear soup en cada pagina

	url_pagina = url_base.format(pagina)
	resultado = requests.get(url_pagina)
	soup = bs4.BeautifulSoup(resultado.text,'lxml')

	# seleccionar datos de los libros

	libros = soup.select('.product_pod')

	#iterar libros

	for libro in libros:

		# checar que tengan 4 o 5 estrellas

		if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')):

			# Guardar titulo en una variable

			titulo_libro = libro.select('a')[1]['title']

			# agregar el libro a la lista

			titulos_rating_alto.append(titulo_libro)

# Ver los libros de 4 y 5 extrellas en consola

for t in titulos_rating_alto:
	print(t)





'''resultado = requests.get(url_base.format('1'))
soup = bs4.BeautifulSoup(resultado.text,'lxml')

libros = soup.select('.product_pod')

ejemplo = libros[0].select('a')[1]['title']

print(ejemplo)'''

'''for n in range(1,11):
	print(url_base.format(n)) # extrae todas la urls desde la pagina 1 hasta la pagina 10
'''

