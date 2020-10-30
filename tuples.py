# primera manera de crear una tupla. directament escribiendo
#valores entre parentesis
x = (1,2,3,4,5)
print(x)
print(type(x))

#la segunda manera en con la cfuncion tupla. de manera similar a
#la funcion list, solo acepta un argumento
y = tuple((1,2,3))
print(y)
print(type(y))

#todo lo que puedes hacer con una tupla (metodos)
#print(dir(x))

#una tupa de un solo elemento no se considera una tupla.
# se considera un int

z = (1)
print(type(z))

#si realment al quieres de un solo elemento...
a = (1,)
print(type(a))

#Accede a un dato en particular
print(x[3])

#borrar tupla
del y

# Algun uso para tuplas. La cosa es que son cosas que no
#  deben cambiar su valor
location = {
    (35.12, 39.00) : "Tokyo",
    (45.58, 34.50) : "NYC",
}
print(location)