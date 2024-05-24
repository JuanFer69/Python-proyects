class Pajaro:

    alas = True

    def __init__(self,color,especie):
        self.color = color
        self.especie = especie
mi_pajaro = Pajaro('negro','Tucan')

print(f'mi pajaro es un {mi_pajaro.especie},y es de color: {mi_pajaro.color}')
print(Pajaro.alas)
print(mi_pajaro.alas)


class Personaje:
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad
harry_potter = Personaje('Humano', True, 17)
print(f'harry_potter es un {harry_potter.especie} ,es magico :{harry_potter.magico},y tiene {harry_potter.edad} años y no es real:{harry_potter.real}')
