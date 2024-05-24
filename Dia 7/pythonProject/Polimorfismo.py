class Vaca:

    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice MUuuu')

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice beee')

vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')


def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)




class ObjetoIterable:
    def __init__(self, *args):
        self.objetos = args
        self.posicion = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.posicion < len(self.objetos):
            objeto_actual = self.objetos[self.posicion]
            self.posicion += 1
            return len(objeto_actual)
        else:
            raise StopIteration

# Definir los objetos palabra, lista y tupla
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

# Crear una instancia del iterador
iterador = ObjetoIterable(palabra, lista, tupla)

# Recorrer el iterador y mostrar la longitud de cada objeto
for longitud in iterador:
    print("Longitud:", longitud)



    