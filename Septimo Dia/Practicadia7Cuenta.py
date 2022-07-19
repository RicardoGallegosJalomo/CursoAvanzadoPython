class Persona:

	def __init__(self,nombre,apellido):

		self.nombre = nombre
		self.apellido = apellido

class Cliente(Persona):

	def __init__(self,nombre,apellido,numero_cuenta,balance=0):
		super().__init__(nombre,apellido)
		self.numero_cuenta = numero_cuenta
		self.balance = balance

	def __str__(self):

		return f"Cliente: {self.nombre} {self.apellido}\n Balance de cuenta {self.numero_cuenta}: ${self.balance}"

	def depositar(self,monto_deposito):
		
		self.balance += monto_deposito
		print("Deposito Aceptado")

	def retirar(self,monto_retiro):

		if self.balance >= monto_retiro:
			self.balance -= monto_retiro
			print("Retiro Exitoso")
		else:
			print("Fondos Insuficientes...")

def crear_cliente():
	
	print("Bienvenido a Crear un Nuevo Cliente") 
	nombre_cl = input("Ingresa tu nombre........: ")
	apellido_cl = input("Ingresa tu apellido....: ")
	numero_cuenta = input("Ingres tu Número de Cuenta.....: ")
	cliente = Cliente(nombre_cl,apellido_cl,numero_cuenta)
	return cliente

def inicio():

	mi_cliente = crear_cliente()
	print(mi_cliente)
	opcion =""

	while opcion != "S":

		print(""" Que movimientos deseas realizar 


			      Depositar a tu Cuenta....: [D]
			      Retirar Dinero...........: [R]
			      Imprimir.................: [I]
			      Salir....................: [S]

			      Elige la opción deseada..: """)

		opcion = input()

		if opcion == "D":
			monto_dep = int(input("Monto a depositar : "))  
			mi_cliente.depositar(monto_dep)

		elif opcion == "I":
			pass #imprimir_cliente()
		elif opcion == "R":
			monto_ret = int(input("Monto a retirar : ")) 
			mi_cliente.retirar(monto_ret) 
		
		print(mi_cliente)

	print("Gracias por operar en este Banco...")

inicio()