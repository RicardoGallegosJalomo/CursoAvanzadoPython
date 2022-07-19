class CD:

	def __init__(self,autor,titulo,canciones):

		self.autor = autor
		self.titulo = titulo
		self.canciones = canciones

	def __str__(self):
		return f'Album {self.titulo} de {self.autor}'

	def __len__(self):
		return self.canciones

	def __del__(self):
		print(f"Se ha eliminado el CD {self.titulo}")

mi_cd = CD('pink floyd','The Wall',24)

print(len(mi_cd))

del mi_cd