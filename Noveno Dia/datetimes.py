import datetime
from datetime import datetime,date

'''mi_hora = time(17, 35)
mi_dia = datetime.date(2025,12,30)

print(mi_dia.today()) # Imprime la fecha actual
print(mi_hora)'''

'''mi_fecha = datetime(2025,5,15,22,10,15,2500)

mi_fecha = mi_fecha.replace(month = 11) # Cambia el mes de la fecha

print(mi_fecha)'''

nacimiento = date(1995,3,5)
defuncion = date(2095,6,19)

vida = defuncion-nacimiento

print(vida)

despierta = datetime(2022,10,5,7,30)
duerme = datetime(2022,10,5,23,45)

vigilia = duerme-despierta

print(vigilia)

hoy = datetime(1995,3,5)
print(hoy.today())