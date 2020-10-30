print("Hola! Como te llamas?")
Nombre = input()
print("Bueno, " + Nombre.capitalize() + ", estoy pensando un numero estre el 1 y el 20")
print("Intenta adivinarlo")
from random import randint
NumeroCorrecto = randint(1,20)
NumeroAdivino = input()
NumeroAdivinoInt = int(NumeroAdivino)
Intentos = 1
while (NumeroCorrecto != NumeroAdivinoInt):
    if NumeroCorrecto > NumeroAdivinoInt:
        print("Tu estimacion es muy baja")
        NumeroAdivino = input()
        NumeroAdivinoInt = int(NumeroAdivino)
    elif NumeroCorrecto < NumeroAdivinoInt:
        print("Tu estimacion es muy alta")
        NumeroAdivino = input()
        NumeroAdivinoInt = int(NumeroAdivino)  
    Intentos = Intentos + 1
else:
    IntentosStr = str(Intentos)
    if Intentos == 1:
        print("Buen trabajo, " + Nombre + "! Has adivinado el numero en " + IntentosStr + " intento!")
    else:
        print("Buen trabajo, " + Nombre + "! Has adivinado el numero en " + IntentosStr + " intentos!")