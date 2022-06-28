texto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fragmento = texto[4] # extrae solo lo que hay en la posicion 4
fragmento = texto[:9] # extrae desde la posicion de inicio hasta la posicion 9
fragmento = texto[::-1] # extrae toda la cadena pero de izquierda a derecha
fragmento = texto[5:10] # extrae des la posicion 5 hasta la 10
fragmento = texto[5:] # extrae desde la posicion 5 hasta el final
fragmento = texto[5:19:2] # extrae desde la posicion 5 hasta la 19 pero cada dos posiciones
print(fragmento)