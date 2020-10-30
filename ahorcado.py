LISTOFWORDS = 'mono elefante gorila tigre perro fresa manzana pera cereza sandia calabaza pepino tomate lechuga cebolla coche bicicleta avion barco tren montaña bosque pantano llanura isla rojo amarillo azul verde morado'.split()
#print(LISTOFWORDS)

IMAGES = ('''

  +---+
  |   |
      |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
  |   |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
  |   |
 /    |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
  |   |
 / \  |
=========''')
#print(IMAGES)

ALPHABET = 'a b c d e f g h i j k l m n ñ o p q r s t u v w x y z'.split()
#print(ALPHABET)

import random

#Esta funcion devuelve una opcion al azar de la secuencia que se le da.
def GetRandomOption(sequency):
  x = random.randint(1, len(sequency)-1)
  return sequency[x]
#print(GetRandomOption(LISTOFWORDS))

#range(x,y,z) --> Devuelve una secuencia de valores que empieza en x, termina en y-1, en incrementos de z.
#for x in y --> Recorre toda la y(y debe de ser una secuencia, como es una lista o un string), de principio a fin, empezando con x=el valor en el indice 0, y terminando con x= el valor en el ultimo indice en y.
#Combinando range and for te devuelve una lista de numeros secuenciales dependiendo de los parametros que pongas en el range.
#Genera un secuencia del 0 al 10, avanzando de uno en uno.
#F = range(0,11,1)
#Para todos los valores que hay en F (tiene 11 valores ahora mismo), imprime ese valor.
#for L in F:
  #print(L)

#Esta funcion te muestra la imagen de tu ahorcado, tus letras fallidas, el estado actual de la palabra a adivinar, y te pide que introduzcas otra letra. Devuelve una lista con las letras adivinadas y con "_" en las posiciones que no han sido adivinadas.
def ShowGameArea(imagenes, numberoffails, chosenletters, word):
#imagenes, hiddenword y chosenletters deben ser secuenciales
#numberoffails debe ser un int
  #Muestra la imagen
  print(imagenes[numberoffails])
  #Muestra las letras ya elegidas que no estan en la palabra
  print('Letras incorrectas: ', end='')
  for x in chosenletters:
    if x in word:
      continue
    else:
      print(x + ' ', end='')
  #Skip line with an empty print
  print('')
  #Crea una lista "vacia" tan larga como la palabra a adivinar
  hiddenword = []
  for x in range(0,len(word),1):
    hiddenword.append('_')
  #print(hiddenword)
  #Rellena la lista "vacia" con las letras
  for x in chosenletters:
    index = 0
    for y in word:
      if x == y:
        hiddenword[index] = x
        index = index +1      
      else:
        index = index + 1
  #Muestra la lista "vacia" de manera legible
  for z in hiddenword:
    print(z + ' ', end='')
  return hiddenword

#Si quieres que una funcion devuelva varios valores, lo puedes hacer con el comando return. Mira abajo para ver como devolver una lista o una tupla. Una vez fuera de la funcion, puedes extraer los datos.
#def Sample():
  #x = 'hola'
  #y = 30
  #z = ('f', 'l', 'g')
  #Usa este return para trabajar con una tupla (metodo 1)
  #return x,y,z
  #Usa este return para trabajar con una lista (metodo 2)
  #return [x,y,z]
#Asignando una tupla (metodo 1)
#x, y, z = Sample()
#Asignando una lista (metodo 2)
#listwithvalues = Sample()

#Esta funcion pregunta por una letra, y se ASEGURA que te devuelta una lista actualizada con todas las letras pedidas.
def UserGuess(alphabet, chosenletters):
  print('Adivina una letra')
  repeat = 0
  while repeat == 0:
    guess = input()
    guess = guess.lower()
    if (guess in alphabet) and (guess not in chosenletters):
      chosenletters.append(guess)
      repeat = 1
    elif (guess in alphabet) and (guess in chosenletters):
      print('Esa letra ya la habias elegido! Prueba otra letra')
    else:
      print('Introduce una LETRA!')
  return chosenletters

#Programa pricipal. Seguramente puedas hacer una funcion para volver a jugar, pero bueno.
#Establece el valor que te va a permitir repetir el programa
jugardenuevo = 'si'
#Aqui empieza el loop del juego. Solo se evalua si quieres jugar de nuevo.
while jugardenuevo == 'si':
  #Titulo
  print('A H O R C A D O')
  #Crea las variables vacias que se iran llenando poco a poco.
  chosenletters = []
  word = GetRandomOption(LISTOFWORDS)
  numberoffails = 0
  #Aqui empieza el loop que evalue si tu letra esta en la palabra, y te da toda la infomacion. Solo se evalua si tu numero de fallos es igual a la longitud de la lista IMAGENES, porque la posicion de la ultima imagen (6) es cuando mueres. Creo que esto ni se necesita porque tienes un BREAK en el codigo abajo, pero esta bien dejarlo asi para asegurarse de que el loop no es infinito.
  while numberoffails < len(IMAGES):
    #Ejecuta la funcion de abajo. Arriba te explica lo que hace.
    hiddenword = ShowGameArea(IMAGES, numberoffails, chosenletters, word)
    #Junto antes de preguntar otra letra, evaluamos aqui si hemos ganado, o hemos perdido. Si no, continuamos.
    #Si nuestra palabra (word) es exactamente igual a lo que la funcion ShowGameArea nos ha devuelto (pero en forma de string, por eso la funcion join()), entonces hemos ganado. Damos la enhorabuena, y salimos del while loop.
    if ''.join(hiddenword) == word:
      print('')
      print('Has ganado! La palabra era ' + word.upper())
      break
    #Si hemos fallado tantas veces como de largo es la lista de IMAGENES, hemos perdido. Salimos del while loop con un mensaje de consolacion. Por este BREAK aqui es por lo que creo que la condicion del while principal no hace falta. Antes de que la condicion del while se cumpla, el loop se rompe aqui.
    if numberoffails == (len(IMAGES)-1):
      print('')
      print('Oh... Has perdido! La palabra era ' + word.upper())
      break
    #Un salto de linea
    print('')
    #Ejecuta la funcion de abajo. Mira arriba para ver lo que hace (Basicamente pregunta por una letra, y te devuelve una lista con todas las letras preguntadas)
    chosenletters = UserGuess(ALPHABET,chosenletters)
    #De nuevo, creo que esto no es necesario, pero es parte de la condicion para que se rompa el while loop principal.
    if chosenletters[len(chosenletters)-1] not in word:
      numberoffails = numberoffails + 1

  #Si estas aqui es porque has ganado o has perdido, asi que te da la opcion de jugar de nuevo.
  print('Quieres jugar de nuevo? (Si o no)')
  #Y esto en un loop sencillo que se asegura de que respondas si o no, y reinicia el program si quieres jugar otra vez.
  repeat = 0
  while repeat == 0:
    jugardenuevo = input()
    jugardenuevo = jugardenuevo.lower()
    if jugardenuevo == 'si' or jugardenuevo == 'no':
      repeat = 1
    else:
      print('Me tienes que decir SI o NO!')

# Perico el de los palotes