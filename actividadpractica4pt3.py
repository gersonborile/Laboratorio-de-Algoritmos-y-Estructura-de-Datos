#ejercicio 1
print("ejercicio 1")

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

for capital,pais in zip(capitales,paises):
    print(f"{capital} es la capital de {pais}")


#ejercicio 2 

print(" ejercicio 2")

marcas = ["ford","chevrolet","lancia","audi","fiat","volkswagen","IKA"]
productos =["mustang","corvette","delta integrale","S4","125 bialbero","gol power","torino tsx"]

mi_zip= list(zip(marcas,productos))

for marca,producto in mi_zip:
    print(f"{producto} es de la marca {marca}")

#ejercicio 3
print(" ejercicio 3")   
numeros_espaniol = ['uno','dos','tres','cuatro','cinco'] 
numeros_portugues = ['um','dois','três',"quatro","five"]
numeros_ingles = ['one','two','three','four','five']

mi_zip=list(zip(numeros_espaniol,numeros_portugues,numeros_ingles))
print(mi_zip)

# ejercicio 4
print("ejercicio 4")

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo= max(lista_numeros)
print(valor_maximo)

# ejercicio 5
print("ejercicio 5")

lista_numeros =[44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
valor_maximo = max(lista_numeros)
valor_minimo = min(lista_numeros)
rango = valor_maximo-valor_minimo
print(rango)

#ejercicio 6 
print("ejercicio 6")

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())
print("Edad mínima:", edad_minima)  
print("Último nombre en posicion alfabetica:", ultimo_nombre)  

#ejercicio 7
print("ejercicio 7")
from random import *
aleatorio = randint(1,10)
print(aleatorio)

#ejercicio 8
print("ejercicio 8")

from random import *
aleatorio = uniform(0,1)
print (aleatorio)

#ejercicio 9
print("ejercicio 9")
from random import * 
sorteo= ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
aleatorio = choice(sorteo)
print(aleatorio)