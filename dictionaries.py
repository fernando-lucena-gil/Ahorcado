#para grandes cantidades de datos que tienen propiedades, 
# se pueden usar listas, pero para eso mejor son los diccionarios.

# cart =[
# ["book", 3, 4.99, "descripcion", 3.99]
# ["book", 3, 4.99]
# ["book", 3, 4.99]
# ["book", 3, 4.99]
# ["book", 3, 4.99]
# ]

product = {
'name': 'book',
'quantity':3,
'price':4.99
}

person = {
    'firs_name': 'Ryan',
    "last_name": "Smith"
}

print(type(product))
print(type(person))
#print(dir(person))

# enseñame las claves
print(person.keys())
# enseñame todo lo que tiene el diccionario
print(person.items())

# #borra diccionario
# del person
# print(person)

# person = {
#     'firs_name': 'Ryan',
#     "last_name": "Smith"
# }

#borrra el contenido de diccionario
print(person)
person.clear()
print(person)

#como acceder a los valor de unallave en particular
print(product['name'])
print(product.get('name', "esta clave no existe"))
print(product.get('editorial', "esta clave no existe"))

#recuerda que una lista puede tener cualquier tipo de dato 
#dentro. como varios diccionarios
products = [
{"name": 'book', 'price': 10.99},
{"name": 'laptop', 'price': 1000}
]
print(products)























