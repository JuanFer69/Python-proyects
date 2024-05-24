
class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self,nombre,apellido,numero_cuenta, balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nNúmero de cuenta: {self.numero_cuenta}\nBalance: {self.balance}"

    def depositar(self, cantidad):
        self.balance += cantidad
        print(f"Se han depositado {cantidad} unidades. Nuevo balance: {self.balance}")

    def retirar(self, cantidad):
        if cantidad > self.balance:
            print("No tienes suficientes fondos para retirar esa cantidad.")
        else:
            self.balance -= cantidad
            print(f"Se han retirado {cantidad} unidades. Nuevo balance: {self.balance}")

def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    numero_cuenta = input("Ingrese el número de cuenta del cliente: ")
    balance = float(input("Ingrese el balance inicial del cliente: "))
    return Cliente(nombre, apellido, numero_cuenta, balance)

def inicio(cliente):

    while True:
        print("\n--- Menú de opciones ---")
        print("1. Mostrar información del cliente")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción que desea realizar: ")


        if opcion == "1":
            print(cliente)
        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad de dinero que desea depositar: "))
            cliente.depositar(cantidad)
        elif opcion == "3":
            cantidad = float(input("Ingrese la cantidad de dinero que desea retirar: "))
            cliente.retirar(cantidad)
        elif opcion == "4":
            print("Saliendo de la cuenta...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Ejemplo de uso
if __name__ == "__main__":
    cliente = crear_cliente()
    inicio(cliente)