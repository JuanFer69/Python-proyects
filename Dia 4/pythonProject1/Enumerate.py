def enumerate1():
    lista = ['a','b','c','d']
    for indice,item in enumerate(lista):
        print(indice,item)

def enumerate2():
    lista = ['a', 'b', 'c', 'd']
    mistuples = list(enumerate(lista))
    print(mistuples[0][1])
def ejercicio1():
    lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
    for indice,nombre in enumerate(lista_nombres):
        print(f'{nombre} se encuentra en el índice {indice}')
def ejercicio2():
    cadena = "Python"
    fragmentos = []
    for letra in enumerate (cadena):
        fragmentos.append(letra)
    print(fragmentos)

def ejercicio3():
    lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
    for indice,nombre in enumerate(lista_nombres):
        if nombre.startswith('M'):
            print(indice,nombre)
ejercicio3()