food = ['apples', 'bread', 'cheese', 'milk', 'grapes']

# print(food[0])
# print(food[1])
# print(food[2])
# print(food[3])

# print('Ahora vamos a usar loops:')

#Hay otro tipo de bucle en Python: el bucle for-in, que se puede 
# leer como ✭✭para todo elemento una serie, hacer. . .✮✮.

# for "introduce variable, puede ser nueva" en "lista, dupla, string existentes..."
# este bucle siempre recorre todo el elemento
for x in food:
    print(x)
    if x == 'cheese':
        print('delicious')
    if x == 'cheese':
        break

# break para el loop. puede ser util ponerlo en condicional
# la palabra clave continue hace que el bucle pare para el valor
# que este corriendo en ese momento, y salta al siguiente
for x in food:
    if x == 'cheese':
        continue
    print(x)

#los bucles funcionan en numeros y strings
for number in range(1, 8):
    print(number)

string = 'hello'
for letter in string:
    print(letter)

# while loop. este es el mas tracional que tu recuerdas
# **Siempre que variable "loquesea", sea ==, <, >, etc... repite
# este loop indefinidamente
Numero = 0
while Numero < 11:
    print(Numero)
    Numero = Numero + 1
