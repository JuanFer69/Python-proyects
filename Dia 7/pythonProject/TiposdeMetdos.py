class Pajaro:
    alas = True

    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio')

    def volar(self,metros):
        print(f'El pajaro ha volado {metros} metros')
        self.piar()
    #metodo de instancia
    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora nuestro pajaro es de color {self.color}')

    #Metodo de clase
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f'Puso {cantidad} de huevo')
        cls.alas = False
        print(Pajaro.alas)
    #No deja apelar a las variables de una funcion pero si de clase

    #Metodo static
    @staticmethod
    def mirar():
        print('el pajaro mira')
#no deja cambiar ni funcion ni clase (Atributos)

mi_pajaro = Pajaro('amarillo','canario')

mi_pajaro.poner_huevos(4)

mi_pajaro.mirar()