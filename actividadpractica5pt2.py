#ejercicio 1
from random import *

def lanzar_dados():
    dado1 = randint(1, 6)  
    dado2 = randint(1, 6)  
    return dado1, dado2  

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2  
    if suma_dados <= 6:
        return print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif 6 < suma_dados < 10:
        return print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else:  
        return print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

#ejercicio 2

def reducir_lista(lista):
    lista_sin_duplicados = []  
    for num in lista:
        if num not in lista_sin_duplicados: 
            lista_sin_duplicados.append(num)  
    if lista_sin_duplicados:  
        lista_sin_duplicados.remove(max(lista_sin_duplicados))  
    return lista_sin_duplicados 

def promedio(lista):
    if len(lista) == 0:  
        return 0
    return sum(lista) / len(lista)  

lista_numeros = [1, 20, 5, 4, 13]

#ejercicio 3
from random import *
def lanzar_moneda():
    return choice(["Cara", "Cruz"])

def probar_suerte(lanzamiento_moneda,lista_numeros):
    

    if lanzamiento_moneda == "Cara":
     print("La lista se autodestruira")
     return []
    else:
         print("La lista fue salvada")
         return lista_numeros

lista_numeros=[5,10,15,20]

# ejercicio 4

def suma_cuadradados( *args):
    return sum(x**2 for x in args)

resultado=suma_cuadradados(2,4,9)
print(resultado)

#ejercicio 5
print("ejercicio 5")
def suma_absolutos(*args):
    return sum(abs(x) for x in args)  

resultado = suma_absolutos(-1, 2, -3, 4)
print(resultado)  

#ejercicio 6
print("ejercicio 6")

def numeros_persona(nombre, *args):
    suma = sum(args)  
    return f"{nombre}, la suma de tus números es {suma}"


mensaje = numeros_persona("Juan", 1, 2, 3)
print(mensaje)  

#ejercicio 7

print("ejercicio 7")

def cantidad_atributos(**kwargs):
    return len(kwargs)  # Devuelve la cantidad de parámetros

# Ejemplo de uso
resultado = cantidad_atributos(nombre="Juan", edad=30, ciudad="Madrid")
print(resultado)  # Imprime 3

    



