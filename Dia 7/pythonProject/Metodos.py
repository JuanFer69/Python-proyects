class Pajaro:
    alas = True

    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio','mi color es {}'.format(self.color))

    def volar(self,metros):
        print(f'El pajaro ha volado {metros} metros')

piolin = Pajaro('amarillo','canario')
piolin.piar()
piolin.volar(50)

class Perro:
    def ladrar(self):
        print("Guau!")

# Crear una instancia de Perro
mi_perro = Perro()

# Llamar al método ladrar() para que el perro ladre
mi_perro.ladrar()  # Esto imprimirá "Guau!" en la pantalla

class Mago:
    def lanzar_hechizo(self):
        print('¡Abracadabra!')
merlin = Mago()
merlin.lanzar_hechizo()


class Alarma:
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
alarma1 = Alarma()
alarma1.postergar(60)