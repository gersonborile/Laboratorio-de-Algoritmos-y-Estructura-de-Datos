from random import choice


palabras = ['elefante', 'guitarra', 'computadora', 'filosofia' , 'departamento' ,'camisa','martillo']

def elegir_palabra():
    return choice(palabras)

def juego_ahorcado():
    palabra = elegir_palabra()
    letras_adivinadas = []
    vidas = 6
    palabra_adivinar = ['_'] * len(palabra)
    
    print("vamos a jugar al ahorcado")
    
    while vidas > 0:
        print("\npalabra:", ' '.join(palabra_adivinar))
        print("vidas restantes:", vidas)
        print("letras usadas:", ' '.join(letras_adivinadas))
        
        letra = input("ingresa una letra: ").lower()
        
        if len(letra) != 1:
            print("solo podes ingresar solo una letra.")
            continue
            
        if letra in letras_adivinadas:
            print("ya usaste esa letra, escribi otra.")
            continue
            
        letras_adivinadas.append(letra)
        
        if letra in palabra:
            print("correcto!")
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_adivinar[i] = letra
        else:
            vidas -= 1
            print("letra incorrecta, perdes una vida.")
        
        if '_' not in palabra_adivinar:
            print("\nganaste!!!")
            print("la palabra era:", palabra)
            break
    
    if vidas == 0:
        print("\nte quedaste sin vidas, perdiste")
        print("la palabra era:", palabra)

juego_ahorcado()