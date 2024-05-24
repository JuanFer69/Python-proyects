def for1():
    lista = ['a','b','c']
    for letra in lista:
        print("letra")
def for2():
    lista = ['a','b','c']
    for letra in lista:
        numeroletra = lista.index(letra)+ 1
        print(f"{numeroletra} letra {letra}")
def for3():
    lista = ['Andres','Camilo','Laura','Luisa']
    for nombre in lista:
        if nombre.startswith('L'):
            print(nombre)
def for4():
    numeros = [1,2,3,4,5]
    mi_valor = 0
    for numero in numeros:
        mi_valor = mi_valor + numero
        print(mi_valor)
def for5():# Lista dentro de lista
    for a,b in [[1,2],[3,4],[5,6]]:
        print(a)#Elemento a de cada lista
def for6():# Diccionario
    dic = {'clave1':1,'clave2':2,'clave3':3}
    for a,b in dic.items():
        print(a,b)
def ejerciciofor1():
    alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
    for nombre in alumnos_clase:
        print("Hola " + nombre)
def ejerciciofor2():
    lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
    suma_numeros = 0
    for numeros in lista_numeros:
        suma_numeros = suma_numeros + numeros
    print(suma_numeros)
def ejercicio3():
    lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
    suma_pares = 0
    suma_impares = 0
    for numeros in lista_numeros:
        if numeros%2 == 0:
            suma_pares += numeros
        else:
            suma_impares += numeros
    print(suma_pares)
    print(suma_impares)

ejercicio3()






