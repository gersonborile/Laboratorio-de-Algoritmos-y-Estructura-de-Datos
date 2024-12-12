#EJERCICIO 1
import random

def lanzar_dado():
    lista = [1,2,3,4,5,6]
    valor1 = random.choice(lista)
    valor2 = random.choice(lista)

def evaluar_jugada():
    lista = [1,2,3,4,5,6]
    valor1 = random.choice(lista)
    valor2 = random.choice(lista)
    suma_dados = valor1 + valor2
    if suma_dados <= 6:
        print(f"La suma de tus dados es {suma_dados} lamentable")
    elif suma_dados > 6 and suma_dados < 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    elif suma_dados >= 10:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

lanzar_dado()
evaluar_jugada()

#EJERCICIO 2

def lanzar_moneda():
    moneda = random.choice(["Cara", "Cruz"])
    return moneda

lista_numeros = [1,2,3,4,5,6]

def probar_suerte(lanzar_moneda, lista_numeros)
    if lanzar_moneda() == "Cara":
        print("La lista se autodestruira")
    elif lanzar_moneda() == "Cruz":
        print("La lista fue salvada")
        print(lista_numeros)
        return lista_numeros

lanzar_moneda()
probar_suerte(lanzar_moneda, lista_numeros)

#EJERCICIO 3

def suma_menores():
    lista_numeros = [500,4,1001,1]
    suma = 0
    for numero in lista_numeros:
        if 0<numero and numero< 1000:
            suma += numero
    print(f"El resultado de la suma de los números en la lista es {suma}")

suma_menores()

#ejercicio 4

class Mago():
    def defender (self):
        print("Escudo magico")
        
class Arquero():
    def defender (self):
        print("Esconderse")
    
class Samurai():
    def defender (self):
        print("bloqueo")
        

def personaje_defender(personaje):
    personaje.defender()


mago = Mago()
personaje_defender(mago)

#ejercicio 5

class Personaje():
    real= False

Harry_Potter=Personaje()
 
def __innit__(self,especie,magico,edad):
    self.especie= "Humano"
    self.magico= True
    self.edad= 17
     
     





    
    
    
    
    












