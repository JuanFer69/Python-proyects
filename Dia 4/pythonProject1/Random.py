from random import *

def random1():
    aleatorio = randint(1,50)
    print(aleatorio)
def random2():
    colores = ['azul','rojo','amarillo','purpura']
    respuesta = input('dime si quieres generar un color aleatorio')
    while respuesta == 'si':
        aleatorio = choice(colores)
        print(aleatorio)
        respuesta = input('dime si quieres generar un color aleatorio')
    print('termina programa')
def random3():#mezcla numeros
    numeros = list(range(5,50,5))
    shuffle(numeros)
    print(numeros)
def ejercicio1():
    aleatorio = random()
    print(aleatorio)
def ejercicio2():
    nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
    sorteo = choice(nombres)
    print(sorteo)
ejercicio2()
