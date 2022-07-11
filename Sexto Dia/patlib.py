from pathlib import Path,PureWindowsPath

carpeta = Path('C:/Users/Cassandra/Desktop/Ultimo Curso de Python/Sexto Dia/prueba.txt') # Esta forma sirve para cualquier SO 

rutawindows = PureWindowsPath(carpeta) # Cambia la ruta del directorio para windows

print(rutawindows)

print(carpeta.read_text()) # muestra por pantalla el contenido del archivo

print(carpeta.name) # Nos muestra el nombre del archivo

print(carpeta.suffix) # Nos muestra la extension del archivo

print(carpeta.stem) # Nos muestra el nombre del arhivo sin la extension

if not carpeta.exists(): # Este medoto devuelve un booleano si el archivo existe 
	print("Este Archivo no Existe")
else:
	print("Genial si existe")

