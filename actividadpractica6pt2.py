#ejercicio 1

from pathlib import Path
ruta_base = Path.home()
print(ruta_base)


#ejercio 2

from pathlib import Path
ruta = Path('Curso Python') / 'Día 6' / 'practicas_path.py'
print(ruta)


#ejercicio 3

from pathlib import Path
ruta_base = Path.home()
ruta = ruta_base / 'Curso Python' / 'Día 6' / 'practicas_path.py'
print(ruta)

#ejercicio 4

def abrir_leer(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido


#ejercicio 5

def sobrescribir(nombre_archivo):
    archivo = open(nombre_archivo, 'w')
    archivo.write("contenido eliminado")
    archivo.close()

#ejercicio 6

def registro_error(nombre_archivo):
    archivo = open(nombre_archivo, 'a')
    archivo.write("se registro un error de ejecución\n")
    archivo.close()
