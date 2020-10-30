myStr = "Hello Darkness My Old Friend"

#print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())

print(myStr.replace('hello', 'bye'))

#you can put functions inside other functions, or string them
print(myStr.replace('hello', 'bye').upper())

#Numero de caracteres de la forma l
print(myStr.count('l'))

#empieza este string con ...?
print(myStr.startswith('hola'))

#Termina este string con...?
print(myStr.endswith('d'))

#split string to several pieces, making a list
#deault to spaces, or specify in between characters
print(myStr.split('e'))

#la funcion find te da la posicion del valor, empezando en 0
# de la misma manera, la funcion index tb, pero da "valueerror"
#en vez de -1 cuando no encuentra soluccion
print(myStr.find('l'))
print(myStr.index('l'))

print("Con error")
print(myStr.find('z'))
#print(myStr.index('z'))

#como de larga es la string?
print(len(myStr))

#true or false. letra o numero?
print(myStr.isnumeric())
print(myStr.isalpha())

#dame el valor en la posicion 4, o el ultimo valor (-1)
print(myStr[4])
print(myStr[-1])

#No te olvides de la concatenaciones
print('My favorite song is ' + myStr)
print(f"My favorite song is {myStr}")
print('My favorite song is {0}'.format(myStr))