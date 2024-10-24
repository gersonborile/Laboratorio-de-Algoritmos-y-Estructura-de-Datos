#ejercicio 1
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumno in alumnos_clase:
    print(f"Hola {alumno}")

#ejercicio 2

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros=0
for numero in lista_numeros:
    suma_numeros=suma_numeros+numero
print(suma_numeros)

#ejercicio 3

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares=0
suma_impares=0
for numero in lista_numeros:
    if numero % 2 ==0:
       suma_pares=suma_pares+numero
    else:
         suma_impares=suma_impares+numero       

print(f"La suma total de los numeros pares es: {suma_pares}")
print(f"La suma total de los numeros impares es: {suma_impares}")

#ejercicio 5

numero = 10
while numero >= 0:
    
    print(numero)
    numero=numero-1

#ejercicio 6 
print("ejercicio 6")
numero = 50

while numero >= 0:
    if numero % 5 == 0: 
        print(numero)    
    numero=numero- 1  

    
#ejercicio 7
print("ejercicio 7")
lista_numeros = [4, 5, 8, 7, 6, 9, 8, 2, 4, 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]

for numero in lista_numeros:
    if numero < 0:  
        break  
    print(numero)  

#ejercicio 8
print("ejercicio 8")
for numero in range(2500,2586,1):
    lista= numero
    print(lista)

#ejercicio 9
print("ejercicio 9")
mi_lista= list(range(3,301,3))

#ejercicio 10

print("ejercicio 10")

suma_cuadrados=0
for numero in range(1,16):
    cuadrado  = numero **2
    suma_cuadrados = suma_cuadrados + cuadrado
print (suma_cuadrados)    

#ejercicio 11
print("ejercicio 11")

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')


#ejercicio 12
print("ejercicio 12") 

lista_indices = list(enumerate("Python"))
print(lista_indices)

#ejercicio 13
print("ejercicio 13") 
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"): 
        print(indice) 
