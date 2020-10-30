#Grandes partes de codigo preconstruidas y perfeccionas a lo largo
# de los años.

#Hay 3 tipos de modulos:
# - Los que creas tu
# - Los que obtienes de alguien mas (internet, etc)
# - Los que vienen ya con Python

#Son como funciones a gran escala.

#Vamos a usar un modulo prederterminado de Python. La fecha y ho
# ra. Puedes buscar la manera de obtenerlo tu, crear tu propio
# codigo, pero para que?
#Se pueden buscar en internet Python Modules

#Primero importas el modulo
import datetime
#depues su metodo date.today
print(datetime.date.today())
print(datetime.timedelta(minutes = 90))

#tambion puedes accerder permanentemene al un metodo con la sin
# taxis from (inserta metodo) import (inserta funcion)
from datetime import timedelta
print(timedelta(minutes = 80))

#o puedes importar varios metodos a la vez
from datetime import timedelta, date
print (timedelta(minutes = 100))
print (date.today())

#implementando tus propias funciones
import fmath
fmath.add(1,2)
fmath.substract(1,2)

from fmath import add, substract
add (3,2)
substract(3,2)
