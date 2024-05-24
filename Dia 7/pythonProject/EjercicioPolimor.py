class Mago:
    def atacar(self):
        print("Ataque mágico")

class Arquero:
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai:
    def atacar(self):
        print("Ataque con katana")

class IteradorAtaque:
    def __init__(self, personajes):
        self.personajes = personajes
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice < len(self.personajes):
            personaje = self.personajes[self.indice]
            self.indice += 1
            return personaje
        else:
            raise StopIteration

# Crear instancias de los personajes
arquero = Arquero()
mago = Mago()
samurai = Samurai()

# Construir el iterable (lista) de personajes en el orden deseado
personajes = [arquero, mago, samurai]

# Crear el iterador
iterador_ataque = IteradorAtaque(personajes)

# Ejecutar el ataque conjugado
for personaje in iterador_ataque:
    personaje.atacar()