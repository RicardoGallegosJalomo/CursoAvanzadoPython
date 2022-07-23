'''def suma(num1,num2):
    
    try :
        print(num1+num2)
    except:
        print("Error inesperado")

suma(3,9)

def cociente(num1,num2):

    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe se cero")

cociente(8,2)'''

def abrir_archivo(nombre_archivo):
    archivo = open(nombre_archivo)

    try:
        print("Abriendo Exitosamente")
    except FileNotFoundError:
        print("El Archivo no fue Encontrado")
    except:
        print("Error desconocido")

    print("Finalizando ejecución")

abrir_archivo("manejo_de_errore")