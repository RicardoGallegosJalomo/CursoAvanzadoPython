from pathlib import Path

base = Path.home() # Obtienes el directorio base de tu sistema Operativo
guia = Path(base,"Barcelona","Sagrada_Familia") # Construye un objeto que parezca una ruta de acceso 
print(guia)
guia = Path(base,"Europa","España",Path("Barcelona","Sagrada_Familia.txt"))
print(guia)
guia2 = guia.with_name("La_pedrera.txt") # Se construye una ruta igual pero cambiando el archivo destino
print(guia2)

'''
print(guia.parent.parent) # Devuelve el antecesor mas inmediato al archivo en este caso España

guia = Path(Path.home(),"Europa")

for txt in Path(guia).glob("**/*.txt"): #Muestra todos los archivos txt de las carpetas y subcarpetas
	print(txt)

guia = Path("Europa","españa","Barcelona","Sagrada_Familia.txt")
en_europa = guia.relative_to(Path("Europa"))  # Muestra solo este directorio "Europa" y el archivo txt
en_espania = guia.relative_to(Path("Europa","España")) # Muestra desde el home hasta España el archivo txt

ruta = Path('c:/Users/Usuarios/Desktop/Curso Python') / 'Cueationario Día 6' / 'Pregunta 1'
Carpeta = ruta.parents[3]
'''