class Animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print('este animal nace')

    def hablar(self):
        print('pio')

class Pajaro(Animal):

    def __init__(self,edad,color,altura_vuelo):
        super().__init__(edad,color)#Para heredad edad y colo r de animal para despues poder manipuar dentro de la funcion
        self.altura_vuelo = altura_vuelo
    def hablar(self):
        print('pio')
    def volar(self,metros):
        print(f'el pajaro vola {metros} metros')



'''piolin = Pajaro(2,'amarillo',60)
mi_animal = Animal(10,'rojo')
piolin.hablar()
piolin.volar(100)

print(piolin.color)
piolin.nacer()

print(Pajaro.__bases__)#MUESTRA PADRE
print(Animal.__subclasses__())#MUESTRA HIJO'''

class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('jaja')
    def hablar(self):
        print('que tal')
class Hijo(Padre,Madre):#Primero busca en padre  luego madre porque asi esta puesto
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

print(Nieto.mro())#ORDEN DE HERENCIA
mi_nieto.hablar()
mi_nieto.reir()

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
    def nadar(self):  # Sobrescribir el método nadar para el ornitorrinco
        print("Nadando como un ornitorrinco")
    def poner_huevos(self):  # Sobrescribir el método poner_huevos para el ornitorrinco
        print("Poniendo huevos como un ornitorrinco")

ornitorrinco = Ornitorrinco()
