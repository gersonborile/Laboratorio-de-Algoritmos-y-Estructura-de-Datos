#ejercicio1
lista_1 = ["Perro","Gato","Hamster","Loro","Pez"]

#ejericio2

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motociceta")
print(medios_transporte)

#ejercicio3

frutas = ["manzana","banana","mango","cereza","sandia"]
print(frutas.pop(3))
eliminado="cereza"

#practicadiccionarios1

mi_dic= {"nombre":"Karen","apellido":"Jurgens","edad":35,"ocupacion":"Periodista"}

#practicadiccionarios2

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][2])

#practicadiccionarios3

mi_dic= {"nombre":"Karen","apellido":"Jurgens","edad":35,"ocupacion":"Periodista"}
mi_dic["pais"] ="Colombia"
print(mi_dic)

#practica tuplas 1
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
cantidad_de_dos=mi_tupla.count(2)
print(cantidad_de_dos)

#practica tuplas 2
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista=list(mi_tupla)
print(mi_lista)

# practica tuplas 3

mi_tupla=(1,2,3,4)
a,b,c,d=mi_tupla
print(a,b,c,d)