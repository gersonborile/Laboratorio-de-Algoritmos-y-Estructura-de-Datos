import os
from pathlib import Path

def mostrar_bienvenida():
    print("Bienvenido al sistema de recetas")

def obtener_ruta():
    return Path.home() / "Recetas"

def mostrar_categorias(ruta_recetas):
    categorias = [categoria.name for categoria in ruta_recetas.iterdir() if categoria.is_dir()]
    for idx, categoria in enumerate(categorias, 1):
        print(f"{idx}. {categoria}")
    return categorias

def contar_recetas(ruta_recetas):
    total_recetas = 0
    for categoria in ruta_recetas.iterdir():
        if categoria.is_dir():
            total_recetas += len(list(categoria.glob("*.txt")))
    return total_recetas

def leer_receta(ruta_recetas, categoria):
    categoria_path = ruta_recetas / categoria
    recetas = [receta.name for receta in categoria_path.glob("*.txt")]
    for idx, receta in enumerate(recetas, 1):
        print(f"{idx}. {receta}")
    receta_elegida = int(input("Elige la receta a leer: ")) - 1
    with open(categoria_path / recetas[receta_elegida], 'r') as archivo:
        print(archivo.read())

def crear_receta(ruta_recetas, categoria):
    categoria_path = ruta_recetas / categoria
    nombre_receta = input("Escribe el nombre de la receta: ")
    contenido = input("Escribe el contenido de la receta: ")
    with open(categoria_path / nombre_receta, 'w') as archivo:
        archivo.write(contenido)
    print(f"Receta '{nombre_receta}' creada")

def crear_categoria(ruta_recetas):
    nueva_categoria = input("Nombre de la nueva categoria: ")
    categoria_path = ruta_recetas / nueva_categoria
    categoria_path.mkdir(exist_ok=True)
    print(f"Categoria '{nueva_categoria}' creada")

def eliminar_receta(ruta_recetas, categoria):
    categoria_path = ruta_recetas / categoria
    recetas = [receta.name for receta in categoria_path.glob("*.txt")]
    for idx, receta in enumerate(recetas, 1):
        print(f"{idx}. {receta}")
    receta_elegida = int(input("Elige la receta a eliminar: ")) - 1
    (categoria_path / recetas[receta_elegida]).unlink()
    print(f"Receta '{recetas[receta_elegida]}' eliminada")

def eliminar_categoria(ruta_recetas):
    categorias = mostrar_categorias(ruta_recetas)
    categoria_elegida = int(input("Elige la categoria a eliminar: ")) - 1
    categoria_path = ruta_recetas / categorias[categoria_elegida]
    for receta in categoria_path.glob("*.txt"):
        receta.unlink()
    categoria_path.rmdir()
    print(f"Categoria '{categorias[categoria_elegida]}' eliminada")

def menu():
    ruta_recetas = obtener_ruta()
    while True:
        mostrar_bienvenida()
        print(f"\nRuta de acceso: {ruta_recetas}")
        print(f"Total de recetas: {contar_recetas(ruta_recetas)}\n")
        print("1. Leer una receta")
        print("2. Crear una nueva receta")
        print("3. Crear una nueva categoria")
        print("4. Eliminar una receta")
        print("5. Eliminar una categoria")
        print("6. Salir")
        
        opcion = int(input("Elige una opcion (1-6): "))
        
        if opcion == 1:
            categorias = mostrar_categorias(ruta_recetas)
            categoria = categorias[int(input("Elige la categoria: ")) - 1]
            leer_receta(ruta_recetas, categoria)
        elif opcion == 2:
            categorias = mostrar_categorias(ruta_recetas)
            categoria = categorias[int(input("Elige la categoria: ")) - 1]
            crear_receta(ruta_recetas, categoria)
        elif opcion == 3:
            crear_categoria(ruta_recetas)
        elif opcion == 4:
            categorias = mostrar_categorias(ruta_recetas)
            categoria = categorias[int(input("Elige la categoria: ")) - 1]
            eliminar_receta(ruta_recetas, categoria)
        elif opcion == 5:
            eliminar_categoria(ruta_recetas)
        elif opcion == 6:
            print("Saliendo")
            break
        else:
            print("Opcion no valida")
        
        input("\nPresiona cualquier tecla para volver al menu")

    menu()
