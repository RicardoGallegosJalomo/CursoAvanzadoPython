print("Calculo de Ganancias por Vendedor")

name_seller = input("Escribe tu Nombre..: ")
ventas = float(input("Captura tus ventas..: "))

resultado = ventas * 13/100

print(f"Para el Vendedor {name_seller} le corresponde una comision de ${round(ventas * 13/100,2)}")

print(f"Para el Vendedor {name_seller} le corresponde una comision de ${round(resultado,2)}")