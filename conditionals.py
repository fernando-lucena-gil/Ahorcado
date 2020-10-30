print('Introduce tu edad:')
x = input()
y = int(x)
print('Tu edad es ' + x)

# >, <, ==

if y > 20:
    print("Tu edad es mayor que 20")
elif y == 20:
    print("Tu edad es exactamente 20")
else:
    print('Tu edad es menor que 20')

print("Escribe un color")
z = input()
print('Has escogido el color ' + z)
if z == "Rojo":
    print('El color que has elegido es mi favorito! El Rojo!')
else:
    print('Oh... Mi color favorito es el rojo, no el ' + z + ".")    


#Puedes meter if statement dentro de otros
Name = 'Fernando'
LastName = 'Lucena'
RealName = 'Fernando'
RealLastName = 'Lucena'

if Name == 'Fernando':
    if LastName == 'Lucena':
        print('Te llamas ' + RealName + ' ' + RealLastName)
    else:
        print('Tu no eres ' + RealName + ' ' + RealLastName)
else:
    print('Tu no eres ' + RealName + ' ' + RealLastName)

#Puedes meter varias condicionales
if y >= 5 and y <=15:
    print('Que sepas que tu edad esta entre 5 y 15.')

# and, not, or
if y >= 5 or y <=15:
    print('Que sepas que tu edad es mayor o igual que 5 o menor o igual que 15.')
if (not(y == 15)):
    print('Tu edad no es 15')
    