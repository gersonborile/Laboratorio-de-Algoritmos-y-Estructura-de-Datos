#ejercicio 1
palabra="ordenador"
resultado= palabra.index("a")
print (resultado)

#ejercicio 2

frase="En teoría, la teoría y la práctica son los mismos. En la practica, no lo son."
indice=frase.index("practica")
print (indice)

#ejercicio 3
frase="En teoría, la teoría y la práctica son los mismos. En la practica, no lo son."
indice=frase.rindex("practica")
print (indice)

#ejercicio 4

frase="Controlar la complejidad es la esencia de la programación"
fragmento=frase[0:10]
print(fragmento)

#ejercicio 5

frase="Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fragmento=frase[8::3]
print(fragmento)

#ejercicio 6

frase="Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmento=frase[::-1]
print(fragmento)

#ejercicio 7

texto ="Imprime el siguiente texto en mayúsculas, empleando el método específico de strings"
print(texto.upper())

#ejercicio 8

lista_palabras = ["La","legibilidad","cuenta."]
lista_string=" ".join(["La","legibilidad","cuenta."])
print(lista_string)

#ejercicio 9 

frase="Si la implementación es dificil de explicar, puede que sea una mala idea.".replace("dificil","facil").replace("mala","buena")
print(frase)
