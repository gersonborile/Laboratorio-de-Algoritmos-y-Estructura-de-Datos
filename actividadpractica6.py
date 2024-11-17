#ejercicio 1
mi_archivo = open('texto.txt', 'r')
print(mi_archivo.read())
mi_archivo.close()

#ejercicio 2

mi_archivo = open('texto.txt', 'r')
primera_linea = mi_archivo.readline()
print(primera_linea)
mi_archivo.close()

# ejercicio 3

mi_archivo = open('texto.txt', 'r')
mi_archivo.readline()
segunda_linea = mi_archivo.readline()
print(segunda_linea)
mi_archivo.close()

#ejercicio 4
mi_archivo = open('mi_archivo.txt', 'w')
mi_archivo.write('Nuevo texto')
mi_archivo.close()
mi_archivo = open('mi_archivo.txt', 'r')
contenido = mi_archivo.read()
print(contenido)
mi_archivo.close()

#ejercicio 5

mi_archivo = open('mi_archivo.txt', 'a')
mi_archivo.write('\nNuevo inicio de sesión')
mi_archivo.close()
mi_archivo = open('mi_archivo.txt', 'r')
contenido = mi_archivo.read()
print(contenido)
mi_archivo.close()

#ejercicio 6

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
mi_archivo = open('registro.txt', 'a')
mi_archivo.writelines([f"{item}\t" for item in registro_ultima_sesion])
mi_archivo.write("\n")
mi_archivo.close()
mi_archivo = open('registro.txt', 'r')
contenido = mi_archivo.read()
print(contenido)
mi_archivo.close()
