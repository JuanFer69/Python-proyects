def set1():
    mi_set = {1,2,3,4,5}
    print(mi_set)
    print(type(mi_set))
    print(2 in mi_set)
def set2():#Union de sets
    s1 = {1,2,3}
    s2 = {3,4,5}
    s3 = {6, 7, 8}
    s4 = s1.union(s2,s3)
    print(s4)
def set3():#Add un sets
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    s3 = {6, 7, 8}
    s4 = s1.union(s2, s3)

    # Agregar el elemento 9 al conjunto s4
    s4.add(9)

    # Imprimir el conjunto actualizado
    print(s4)
def set4():#Add varios sets
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    s3 = {6, 7, 8}
    s4 = s1.union(s2, s3)

    # Agregar el elemento 9 al conjunto s4
    s4.update([9,'diez'])

    # Imprimir el conjunto actualizado
    print(s4)
def set5(): # eliminar
    s1 = {1, 2, 3}
    s1.remove(6)
    print(s1)
def set6(): # eliminar
    s1 = {1, 2, 3}
    s1.discard(6)
    print(s1)
def set7(): # eliminar elemento aleatorio
    s1 = {1, 2, 3}
    sorteo = s1.pop()
    print(sorteo)
def set8(): # clear set
    s1 = {1, 2, 3}
    s1.clear()
    print(s1)
def Ejercicio1():
    mi_set_1 = {1, 2, "tres", "cuatro"}
    mi_set_2 = {"tres", 4, 5}
    mi_set_3 = mi_set_1.union(mi_set_2)
    print(mi_set_3)
def Ejercicio2():
    sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
    azar = sorteo.pop()
    print(azar)
def Ejercicio3():
    sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
    sorteo.add('Damián')
    print(sorteo)

set6()