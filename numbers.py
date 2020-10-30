print(type(9))
print(type(9.5))

# #al hacer una operacion, si uno de los dos numeros es decimal
#el resultado tb lo es
# de la misma manera, python te devuelve un decimal si al dividir
# el resulto debe ser decimal

print(type(10))
print(type(5))
print(type(10+5))
print(type(5.0))
print(type(10+5.0))
print(10+5.0)
print(type(3/2))

#suma con +, resta con -, multiplica con *, divide con /

#potencia
print(2**3)

# para forzar a que una division de el numero exacto (sin el resto)
# usa //

print(3/2)
print(3//2)

# para obtener el resto, usa %

print('13/5')
print(13/5)
print(13%5)

# las reglas basicas de orden de operation de matematicas se
# aplican. Pero puede poner parentesis para forzar el orden,
# como tambien se enseña en primaria

AGE = input("Insert your age:")
# muy importante saber que todo lo que se inserta a un programa
#osea, inputs, son STRINGS
print(AGE)
# vamos a convertir el string a un numero. tb puedes hacerlo float
AGE = int(AGE)
#ahora si se puede sumas dos numeros
new_age= AGE + 5
print(new_age)
print(type(new_age))