class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")
mi_perro = Mascota()
mi_perro.respirar()

class Jugador:

    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True



class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        if self.cantidad_flechas > 0:
            self.cantidad_flechas -= 1
            print("¡Flecha lanzada!")
            print("Cantidad de flechas restantes:", self.cantidad_flechas)
        else:
            print("No quedan flechas.")

# Ejemplo de uso
personaje1 = Personaje(5)  # Crear una instancia con 5 flechas
personaje1.lanzar_flecha()  # Lanzar una flecha
personaje1.lanzar_flecha()  # Lanzar otra flecha

