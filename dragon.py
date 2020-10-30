import random
import time

def introduction():
  print('Estas en una tierra llena de dragones.')
  print('Frente a ti hay dos cuevas')
  print('En una, hay un dragon bueno, en la otra, uno malo')

def eligeTuCueva():
  teeligoati = ''
  while teeligoati != '1' and teeligoati != '2':
    print('A que cueva quieres entrar? 1 o 2.')
    #input return a string not an int
    teeligoati = input()
  return teeligoati
  
def resultado(y):
  print('Te aproximas a la cueva...')
  time.sleep(2)
  print('Es oscura y espeluznante...')
  time.sleep(2)
  print('Un dragon enorme aparece frente a ti...y...')
  time.sleep(2)
  x = random.randint(1,2)
  #converting x to str to be able to compare to y
  x = str(x)
  if y == x:
    print('Te da su tesoro!')
  else:
    print('Te devora de un bocado!')

repetir = 'Si'
while repetir == 'Si':
  introduction()
  #esto va a ser un string porque eligo cueva devuelve un strin
  cuevaelegida = eligeTuCueva()
  resultado(cuevaelegida)
  print('Juegas otra vez? Si o no.')
  repetir = input()
  repetir = repetir.capitalize()

