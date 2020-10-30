# funciones son literalmene como funciones matematicas.
# les dan un input, y transforman este input a un output, 
# que es lo que te dan

#algunas son ya predeterminadas, como estas que hemos usado.
#print(), dir(), type(), len()

#creado nuestra propia funcion. entre parentesis, nuestro paramentro
#FirstName = input('Me dices tu nombre, por favor. ')
FirstName = 'Fernando'

def hello(Name='Don Nadie'):
    print('Hello ' + Name)

#llamando a la funcion. Entre parentesis el valor que quieres que
#el parametro llame
hello(FirstName)
hello('Ryan')
hello('Gabriela')
#Si una funcion require un argumente pero no se lo das, puedes po
#ner uno por defecto, como el que he puesto arriba con Name=Don Nadie
hello()

#Otra ejemplo de Funcion del que te devuelte el valor de la suma
# de dos numero que le des
def Add(n1,n2):
    return n1 + n2

print(Add(2,4))
print(Add(69,420))

#Usando funciones creando lambda. mas sencillas, una linea,
#la funcion ya sabe que debe devolver un valor
add = lambda numberOne, numberTwo: numberOne + numberTwo

print(add(10,30))