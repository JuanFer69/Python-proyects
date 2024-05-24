def lista1():
    mi_lista = ['a','b','c']
    resultado  = mi_lista[::-1]
    print(resultado)
def lista2():
    mi_lista = ['a','b','c']
    otra_lista = ['hola', 1, 61,71]
    unionlistas = mi_lista + otra_lista
    print(unionlistas)
def lista3():# cambiar contenido
    mi_lista = ['a','b','c']
    otra_lista = ['hola', 1, 61,71]
    unionlistas = mi_lista + otra_lista
    unionlistas[0] = 'primero'
    print(unionlistas)
def lista4():#añadir contenido
    mi_lista = ['a', 'b', 'c']
    otra_lista = ['hola', 1, 61, 71]
    unionlistas = mi_lista + otra_lista
    unionlistas.append('agregado')
    print(unionlistas)
def lista4():#eliminar contenido
    mi_lista = ['a', 'b', 'c']
    otra_lista = ['hola', 1, 61, 71]
    unionlistas = mi_lista + otra_lista
    eliminado = unionlistas.pop(1)
    print(unionlistas)
    print(eliminado)
def lista5():#ordenar listas alfabeticamente
    mi_lista = ['b', 'a', 'c']
    mi_lista.sort()
    print(mi_lista)

def lista6():  # ordenar listas alfabeticamente reverse
    mi_lista = ['b', 'a', 'c']
    mi_lista.reverse()
    print(mi_lista)
lista4()