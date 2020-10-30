#los sets son listas desordenadas sin indice
#se crean con corchetes

colors = {'red', 'green', 'blue'}

print('imprime colors y dime que tipe de dato es:')
print(colors)
print(type(colors))

print("esta red en el set colors?")
print('red' in colors)

#se añade de forma aleatoria
print("añade violeta:")
colors.add('violet')
print(colors)

print('quita blue')
colors.remove("blue")
print(colors)

#haz una copia
print('haz una copia de colors y llamala copy colors. muestrala')
copycolors = colors.copy()
print(copycolors)

#limpia la lista
print('limpia la lista copycolors, e imprime ambas')
copycolors.clear()
print(copycolors)
print(colors)

#borra una lista
print('elimina una lista con del command')
del copycolors
print(copycolors)