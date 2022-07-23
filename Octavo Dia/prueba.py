import unittest
import practicaUnittest


class ProbarCambiarTexto(unittest.TestCase):

	def test_mayusculas(self):
		palabra = 'buen dia'
		resultado = practicaUnittest.todo_mayusculas(palabra)
		self.assertEqual(resultado, 'Buen Dia')


if __name__ == '__main__':
	unittest.main()
