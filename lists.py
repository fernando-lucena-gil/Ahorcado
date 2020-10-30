# manera sencilla. dale un valor, ponlo entre corchetes
demo = [1, 'hello', 1.34, True, [1, 2, 3]]
print(demo)

# tambien puedes usar la fundion list, pero solo acepta un
# argumente. si quieres meter mas cosas, tienes que usar una
# tupla u otra lista
numbers_list = list((1,2,3,4))
print(numbers_list)

#range te da la opcion de hacer un rango. llega hasta un numero
#anterior al que se ve
f = list(range(1,11))
print(f)

# dir comando te permite saber que metodos (modificaciones) se
# le puede hacer a un tipo de dato determiando.

colors = ['red', 'green', 'blue']
#text = "hola adios"
#print(type(colors))
#print(type(text))
#print(dir(colors))
#print("HOLA QUE TAL")
#print(dir(text))

#cambiando valores en las lista. basucamente acceded al valor
#[] y asignale un valor nuevo
print(colors)
colors[2] = "violet"
print(colors)

#metodos/modificaciones
# longitud de la lista
print(len(colors))
# que esta en en la position (index) 2?
print(colors[2])
# la lista colors incluye el valor "red"?
print('red' in colors)
# añade un valor, y solamente uno, a la lista. puede ser cualquier
# tipo de valor (int, string, list), pero solo lo añade como una
# unidad entera
colors.append(("yellow", "brown"))
print(colors)

# usa extend para meter mas de un valor. el input es, de nuevo, 
# solo un valor (ya sea string, tupla, lista), pero el output 
# esta dividdo en varios
colors.extend(["pink", "orange"])
print(colors)

# insertar elementos justo en una posicion en especifico
colors = ['red', 'green', 'blue']
print(colors)
colors.insert(1, 'violet')
print(colors)
colors.insert(len(colors), "yellow")
print(colors)

#quitar valores en posicion tal de cual
colors.pop()
print(colors)

colors.pop(0)
print(colors)

# quitar valores cuyo nombre es tal de cual. solo quita el pri
# mero que encuentra

colors = ['red', 'green', 'blue', 'red']
print(colors)
colors.remove('red')
print(colors)

# vacia list
colors = ['red', 'green', 'blue', 'red']
print(colors)
colors.clear()
print(colors)
print("end")

#ordenar alfabeticamente
colors = ['red', 'green', 'blue', 'red']
print(colors)
colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)

# saca el indice
colors = ['red', 'green', 'blue', 'red']
print(colors)
print(colors.index('red'))

#cuantas veces sale ese indice
print(colors.count('red'))