from collections import namedtuple
from collections import Counter
from collections import defaultdict


Persona = namedtuple('Persona',['nombre','altura','peso'])

ariel = Persona('Arial',1.76,79)

print(ariel.nombre)
print(ariel.peso)
print(ariel[2])


lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)
print(contador)

# Acceder al recuento de un elemento específico
print("Número de '1':", contador[1])
print("Número de '2':", contador[2])
print("Número de '3':", contador[3])
print("Número de '4':", contador[4])
print("Número de '5':", contador[5])
print("Número de '6':", contador[6])
print("Número de '7':", contador[7])




# Creamos un defaultdict con un valor predeterminado de "Valor no hallado"
mi_diccionario = defaultdict(lambda: "Valor no hallado")

# Añadimos la palabra clave 'edad' con el valor 44
mi_diccionario['edad'] = 44

# Imprimimos el diccionario para verificar
print(mi_diccionario)


from collections import deque

# Lista inicial de ciudades
ciudades_iniciales = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

# Crear una deque a partir de la lista de ciudades iniciales
lista_ciudades = deque(ciudades_iniciales)

# Imprimir la deque original
print("Deque original:", lista_ciudades)

# Agregar un elemento por la izquierda
lista_ciudades.appendleft("Barcelona")

# Imprimir la deque después de agregar 'Barcelona' por la izquierda
print("Deque después de agregar 'Barcelona' por la izquierda:", lista_ciudades)

# Agregar un elemento por la derecha
lista_ciudades.append("Atenas")

# Imprimir la deque después de agregar 'Atenas' por la derecha
print("Deque después de agregar 'Atenas' por la derecha:", lista_ciudades)


