# ejercicio 1
class Personaje:
    pass
harry_potter = Personaje()

# ejercicio 2

class Dinosaurio:
    pass
velociraptor = Dinosaurio()
tirosaurio_rex = Dinosaurio()
braquiosaurio = Dinosaurio()

# ejercicio 3

class PlataformaStreaming:
    pass
netflix = PlataformaStreaming()
hbo_max = PlataformaStreaming()
amazon_prime_video = PlataformaStreaming()

# ejercicio 4
class Casa():
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa("blanco", 4)

print(f"La casa es de color {casa_blanca.color} y tiene {casa_blanca.cantidad_pisos} pisos.")

# ejercicio 5

class Cubo():
    caras = 6

    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo("rojo")

print(f"El cubo tiene {cubo_rojo.caras} caras y su color es {cubo_rojo.color}.")

# ejercicio 6

class Personaje():
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje("Humano", True, 17)

print(f"Especie: {harry_potter.especie}, Magico: {harry_potter.magico}, Edad: {harry_potter.edad}")


# ejercicio 7

class Perro():
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("Guau!")

mi_perro = Perro("Rex")

print(f"Mi perro se llama {mi_perro.nombre}")
mi_perro.ladrar()

# ejercicio 8

class Mago():
    def __init__(self, nombre):
        self.nombre = nombre

    def lanzar_hechizo(self):
        print("¡Abracadabra!")

merlin = Mago("Merlin")

print(f"El mago se llama {merlin.nombre}")
merlin.lanzar_hechizo()



# ejercicio 9

class Alarma():
    def __init__(self):
        pass

    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido postergada {cantidad_minutos} minutos")

mi_alarma = Alarma()

mi_alarma.postergar(10)


# ejercicio 10

class Mascota():
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")


Mascota.respirar()


# ejercicio 11

class Jugador():
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True

jugador = Jugador()
print(f"El jugador está vivo? {jugador.vivo}")
jugador.revivir()
print(f"El jugador está vivo? {jugador.vivo}")


# ejercicio 12

class Personaje():
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1

personaje = Personaje(5)
print(f"Cantidad de flechas antes de lanzar: {personaje.cantidad_flechas}")
personaje.lanzar_flecha()
print(f"Cantidad de flechas después de lanzar: {personaje.cantidad_flechas}")


# ejercicio 13

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

alumno = Alumno("Juan", 20)
print(f"Nombre: {alumno.nombre}, Edad: {alumno.edad}")


# ejercicio 14

class Mascota():
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass

perro = Perro(3, "Rex", 4)
print(f"Nombre: {perro.nombre}, Edad: {perro.edad}, Patas: {perro.cantidad_patas}")


# ejercicio 15

class Vehiculo():
    def acelerar(self):
        pass

    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass

auto = Automovil()
auto.acelerar()
auto.frenar()


# ejercicio 16

class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")
class Hija(Padre, Madre):
    pass

hija = Hija()
hija.trabajar()
hija.reir()



# ejercicio 17

class Padre():
    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")

class Hija(Padre, Madre):
    pass

hija = Hija()
hija.reir()
hija.trabajar()


# ejercicio 18

class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
    pass

ornitorrinco = Ornitorrinco()
ornitorrinco.poner_huevos()
ornitorrinco.nadar()
ornitorrinco.caminar()
ornitorrinco.amamantar()
print(f"Tiene pico: {ornitorrinco.tiene_pico}")
print(f"Es vertebrado: {ornitorrinco.vertebrado}")
print(f"Es venenoso: {ornitorrinco.venenoso}")


# ejrcicio 19

class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"

class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"

hijo = Hijo()
print(hijo.hobby())


# ejercicio 20

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for objeto in [palabra, lista, tupla]:
    print(len(objeto))


# ejercicio 21

class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

personajes = [Arquero(), Mago(), Samurai()]

for personaje in personajes:
    personaje.atacar()


# ejercicio 22

class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

def personaje_defender(personaje):
    personaje.defender()

# Ejemplo de uso
mago = Mago()
arquero = Arquero()
samurai = Samurai()

personaje_defender(mago)
personaje_defender(arquero)
personaje_defender(samurai)


# ejercicio 23

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

# ejercicio 24

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
    def __len__(self):
        return self.cantidad_paginas

# ejercicio 25

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
    def __del__(self):
        print("Libro eliminado")