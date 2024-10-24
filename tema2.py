nombres = []
while True:
    nombre = input("Ingrese el nombre del estudiante, 'FIN' para terminar o 'REPETIR' para mostrar los nombres cargados hasta el momento: ")
    if nombre == 'FIN':
        print("Terminó el ingreso de nombres.")
        break
    elif nombre == 'REPETIR':
        print("Los nombres ingresados hasta el momento son: ")
        for n in nombres:
            print(n)
    else:
        while True:
            if not nombre:
                print("El nombre no puede estar vacío.")
            elif nombre.isdigit():
                print("El nombre no puede contener números.")
            elif not nombre.isalpha():
                print("El nombre no puede tener caracteres especiales.")
            else:
                nombres.append(nombre)
                break
            
            nombre = input("Reingrese un nombre valido: ")

while True:
    print("\nMenú de opciones:")
    print("1. Mostrar nombres ingresados")
    print("2. Mostrar nombres en orden alfabetico")
    print("3. Mostrar el nombre más largo y el mas corto")
    print("4. Contar vocales y consonantes")
    print("5. Contar cantidad de palabras en los nombres")
    print("6. Mostrar los nombres invertidos")
    print("7. Buscar nombre por letra")
    print("8. Verificar si un nombre ha sido ingresado")
    print("9. Mostrar cuantos nombres tienen mas de 5 letras")
    print("10. Mostrar todos los nombres en minuscula o en mayuscula")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print("Los nombres ingresados son:")
        for n in nombres:
            print(n)
    elif opcion == '2':
        nombres.sort()
        print("Los nombres ingresados en orden alfabético son:")
        for n in nombres:
            print(n)
    elif opcion == '3':
        if nombres:  
            nombre_mas_largo = nombres[0]
            nombre_mas_corto = nombres[0]
            
            for n in nombres:
                if len(n) > len(nombre_mas_largo):
                    nombre_mas_largo = n
                if len(n) < len(nombre_mas_corto):
                    nombre_mas_corto = n
            
            print(f"El nombre más largo es: {nombre_mas_largo}")
            print(f"El nombre más corto es: {nombre_mas_corto}")
        else:
            print("No hay nombres ingresados.")
    
    elif opcion == '4':
        total_vocales = 0
        total_consonantes = 0
        vocales = "aeiouAEIOU"
        
        for n in nombres:
            for caracter in n:
                if caracter.isalpha(): 
                    if caracter in vocales:
                        total_vocales += 1
                    else:
                        total_consonantes += 1

        print(f"Total de vocales: {total_vocales}")
        print(f"Total de consonantes: {total_consonantes}")
    
    elif opcion == '5':
        print("Cantidad de palabras en cada nombre:")
        for n in nombres:
            cantidad_palabras = len(n.split())
            print(f"{n}: tiene {cantidad_palabras} palabras")    
    
    elif opcion == '6':
        print("Nombres invertidos:")
        for n in nombres:
            nombre_invertido = n[::-1] 
            print(nombre_invertido)
    
    elif opcion=='7':
        
        letra = input("Ingrese una letra: ")  
        nombres_con_letra = []
    
        for n in nombres:
          if letra in n:
            nombres_con_letra.append(n)
    
        if nombres_con_letra:
          print("Nombres que contienen la letra", letra + ":")
        for n in nombres_con_letra:
            print(n)
        else:
           print(f"No se encontraron nombres que contengan la letra '{letra}'.")

    elif opcion == '8':
        nombre_buscar = input("Ingrese un nombre para verificar si esta en la lista: ")
        if nombre_buscar in nombres:
            print(f"El nombre '{nombre_buscar}' esta en la lista")
        else:
            print(f"El nombre '{nombre_buscar}' no esta en la lista")             
    

#Hecho en clase:


    elif opcion== '9':
        nombres_cinco_caracteres=0
        for n in nombres:
            if len(n)>5:
                nombres_cinco_caracteres=n
                print(f"Los nombres que tienen mas de cinco caracteres son: {nombres_cinco_caracteres}")

    elif opcion=='10':
        nombre_minuscula=nombre.lower
        nombre_mayuscula=nombre.upper
        opcion_mayuscula=0
        opcion_minuscula=0
        print("Para ver los nombres en minuscula presione 1 y para ver los nombres en mayuscula presione 2")
        if opcion_minuscula =='1':
           print(f"Los nombres en minuscula serian: {nombre_minuscula}")
        elif opcion_mayuscula =='2':
            print(f"Los nombres en mayuscula serian: {nombre_mayuscula}")

    elif opcion == '0':
        print("Saliendo del programa")
        break
    
    else:
        print("Opción invalida, elija una opcion valida")