class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_de_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_de_cuenta = numero_de_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\n" \
               f"Numero de cuenta: {self.numero_de_cuenta}\n" \
               f"Balance: ${self.balance:.2f}"

    def Depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print(f"Depositaste ${cantidad:.2f}. Balance actualizado: ${self.balance:.2f}")
        else: 
            print("La cantidad a depositar tiene que ser mayor a cero")

    def Retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.balance:
                self.balance -= cantidad
                print(f"Retiraste ${cantidad:.2f}. Balance actualizado: ${self.balance:.2f}")
            else:
                print("No tenes suficiente dinero para retirar.")
        else:
            print("La cantidad a retirar debe ser mayor que cero")

def crear_cliente():
    nombre = input(" ingresa el nombre del cliente: ")
    apellido = input(" ingresa el apellido del cliente: ")
    numero_de_cuenta = input(" ingresa el numero de cuenta: ")
    balance_inicial = float(input(" ingresa el balance inicial de la cuenta: "))

    cliente = Cliente(nombre, apellido, numero_de_cuenta, balance_inicial)
    return cliente

def inicio():
    print("Bienvenido")
    cliente = crear_cliente()

    while True:
        print("\nElige una opcion")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Mostrar balance")
        print("4. Salir")
        opcion = input("Elige una opcion 1-2-3-4: ")

        if opcion == "1":
            cantidad = float(input("cuanto dinero deseas depositar? $"))
            cliente.Depositar(cantidad)
        elif opcion == "2":
            cantidad = float(input("cuannto dinero deseas retirar? $"))
            cliente.Retirar(cantidad)
        elif opcion == "3":
            print(cliente)
        elif opcion == "4":
            print("Saliendo")
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    inicio()
