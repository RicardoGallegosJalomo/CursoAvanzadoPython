import zipfile

import shutil

'''mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w') #Crea el archivo zip en modo escritura

mi_zip.write('mi_texto_A.txt') # Se graban los archivos en el archivo zip
mi_zip.write('mi_texto_B.txt') # Se graban los archivos en el archivo zip

zip_abierto = zipfile.ZipFile('archivo_comprimido.zip','r')

zip_abierto.extractall()

#mi_zip.close()'''

#carpeta_origen = 'C:\\Users\\Cassandra\\Desktop\\Ultimo Curso de Python\\Noveno Dia\\Recetas\\'

#archivo_destino = 'Todo_comprimido' # Este es el nombre de la carpeta a crear con los zip

#shutil.make_archive(archivo_destino,'zip',carpeta_origen) # se crea el archivo zip 

#shutil.unpack_archive('Todo_comprimido.zip','Extraccion_terminada','zip') # descomprime en la carpeta que se le asigna

shutil.unpack_archive('ProyectoDia9.zip','Practica_dia_9','zip')
