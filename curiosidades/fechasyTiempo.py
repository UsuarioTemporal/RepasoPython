import time
import datetime
print('Tiempo sin formato')
print(time.time())
print('\nTiempo con formato,24h')
print(time.strftime('%H : %M : %S')) # dandole formato

print('\nTiempo con formato,12h')
print(time.strftime('%I : %M : %S'))

print('\nFechas')
print(time.strftime('%d / %m / %Y'))# %y

tiempo1= time.strftime('%H : %M : %S')
tiempo2 = time.strftime('%I : %M : %S')
print(type(tiempo1)," ",type(tiempo2))

"""
 formato = "%c" -> fecha y tiempo
 formato = %x and %X
"""

print(time.strftime("%x"))
print(time.strftime("%X"))
print(time.strftime("%c"))



print("\nExtraccion de porciones d fecha\n")
ahora = datetime.datetime.now()

print("Fecha total : ",ahora)
print("Mes : ",ahora.month)
print("Dia : ",ahora.day)
print("Ano ",ahora.year)
print("Hora ", ahora.hour)
print("Minuto ",ahora.minute)
print("Segundo ",ahora.second)