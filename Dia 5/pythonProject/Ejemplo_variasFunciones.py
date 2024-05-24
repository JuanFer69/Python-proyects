from random import shuffle
#Lista inicial
palitos = ['-','--','---','----']
#mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return (lista)
#pedirle intento
def probarsuerte():
    opcion = 0
    while opcion not in range(1,5):
        opcion = int(input('Elige un numero del 1 al 4'))
    return opcion
def compruebaintento(lista,opcion):
    if lista[opcion - 1] == '-':
        print('¡Perdiste!')
    else:
        print('¡Te salvaste!')
    print('Palito seleccionado:', lista[opcion - 1])

palitos_mezaclados = mezclar(palitos)
seleccion = probarsuerte()
compruebaintento(palitos_mezaclados,seleccion)