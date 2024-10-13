
texto = input("Ingrese un texto: ")


letra1 = input("Ingrese la primera letra: ").lower()
letra2 = input("Ingrese la segunda letra: ").lower()
letra3 = input("Ingrese la tercera letra: ").lower()


texto_lower = texto.lower()
conteo1 = texto_lower.count(letra1)
conteo2 = texto_lower.count(letra2)
conteo3 = texto_lower.count(letra3)

print(f"La letra '{letra1}' aparece {conteo1} veces en el texto.")
print(f"La letra '{letra2}' aparece {conteo2} veces en el texto.")
print(f"La letra '{letra3}' aparece {conteo3} veces en el texto.")

lista=texto.split()
cantidad_palabras=len(lista)
print(f"El texto tiene una cantidad de {cantidad_palabras} palabras")
primera_letra=texto[0]
ultima_letra=texto[-1]
print(f"La primera letra del texto es '{primera_letra}' y  la ultima letra del texto es '{ultima_letra}'")
texto_invertido=lista.reverse()
texto_invertido=" ".join(lista)
print("El texto invertido se veria de la siguiente forma: ")
print(texto_invertido)

palabra_buscada = "Python"
encontrada = palabra_buscada in texto


resultado = {
    True: f"La palabra '{palabra_buscada}' se encuentra en el texto.",
    False: f"La palabra '{palabra_buscada}' NO se encuentra en el texto."
}

mensaje = resultado[encontrada]
print(mensaje)