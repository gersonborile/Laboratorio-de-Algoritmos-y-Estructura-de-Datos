#ejercicio 1
num1 = 36
num2 = 17
mi_bool=num1>=num2
print(mi_bool)

#ejercicio 2

num1 = 25 **0.5
num2 = 5
mi_bool=num1==num2
print(mi_bool)

#ejercicio 3

num1= 64 *3
num2 =24 * 8
mi_bool= num1!=num2
print(mi_bool)

#ejercicio 4

num1=36
num2=72/2
num3=48
mi_bool= num1>num2 and num1<num3
print(mi_bool) 

#ejercicio 5 

num1=36
num2=72/2
num3=48
mi_bool= num1>num2 or num1<num3
print(mi_bool)

#ejercicio 6

palabra1 = "éxito"
palabra2 = "tecnología"
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
mi_bool= palabra1 not in frase and palabra2 not in frase
print(mi_bool)

#ejercicio 7

if num1>num2:
    print(f"{num1} Es mayor que {num2}")
elif num2>num1:
    print(f"{num2} Es mayor que {num1}")
else:
    print (f"{num1} y {num2} son iguales")

#ejercicio 8

edad = 16
tiene_licencia = False

if edad>18:
    print("Puedes conducir")
elif edad<18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
      print("No puedes conducir. Necesitas contar con una licencia")

#ejercicio 9

habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python:
    print( "Cumples con los requisitos para postularte") 
elif habla_ingles and not sabe_python:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")    
elif not habla_ingles and sabe_python:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif not sabe_python and habla_ingles:
    print("Para postularte, necesitas saber programar en Python")        

