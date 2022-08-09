import bs4
import requests

resultado = requests.get('https://escueladirecta.com/courses')
soup = bs4.BeautifulSoup(resultado.text,'lxml')

#parrafo_Especial = sopa.select('p')[3].getText() #Extrae un parrafo de una pagina web

'''parrafo = soup.select('.r-snippetized')

for pa in parrafo:
	print(pa.getText())

print(parrafo)'''

#print(parrafo_Especial)

#print(sopa.select('title')[0].getText()) # Estrae el titulo de la pagina

imagenes = soup.select('.course-box-image')[0]['src'] # Extraer imagenes

#for imagen in imagenes:
#	print(imagen)

print(imagenes)

imagen1 = requests.get(imagenes)
#print(imagen1.content)

f = open('mi_imagen.jpg','wb')
f.write(imagen1.content)
f.close()