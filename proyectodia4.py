from random import *

nombre = input("ingresa tu nombre: ")

numero_aleatorio = randint(1, 100)  

intentos_maximos = 8
intentos_realizados = 0
adivinado = False

print(f"\nbueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo {intentos_maximos} intentos para adivinarlo.")

while intentos_realizados < intentos_maximos and not adivinado:
    intento = int(input("\nIngresa tu número: "))
    intentos_realizados += 1
    
    if intento < 1 or intento > 100:
        print("error, el numero debe ser entre 1 y 100")
        intentos_realizados -= 1  
    
    elif intento < numero_aleatorio:
        print("respuesta incorrecta. elegiste un numero menor al numero que tenes que adivinar.")
        print(f"te quedan {intentos_maximos - intentos_realizados} intentos.")
    
    elif intento > numero_aleatorio:
        print("respuesta incorrecta, elegiste un numero mayor al numero que tenes que adivinar.")
        print(f"te quedan {intentos_maximos - intentos_realizados} intentos.")
    
    else:
        print(f"\nfelicidades {nombre} ganaste!")
        print(f"encontraste el número en {intentos_realizados} intentos.")
        adivinado = True

if not adivinado:
    print(f"\ {nombre}, usaste tus {intentos_maximos} intentos.")
    print(f"el numero a adivinar era {numero_aleatorio}.")