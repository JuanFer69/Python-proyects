def reducir_lista(lista):
    # Convertir la lista en un conjunto para eliminar duplicados
    lista_sin_duplicados = set(lista)
    # Si hay más de un elemento en el conjunto, eliminar el valor más alto
    if len(lista_sin_duplicados) > 1:
        lista_sin_duplicados.remove(max(lista_sin_duplicados))
    # Convertir el conjunto de nuevo en lista y devolverlo
    return list(lista_sin_duplicados)
def promedio(lista):
    # Calcula la suma de los valores en la lista
    suma = sum(lista)
    # Calcula la cantidad de elementos en la lista
    cantidad_elementos = len(lista)
    # Calcula el promedio
    promedio = suma / cantidad_elementos
    return promedio

# Ejemplo de uso:
lista_numeros = [1, 2, 3, 3, 4]
lista_reducida = reducir_lista(lista_numeros)
resultado_promedio = promedio(lista_reducida)
print(resultado_promedio)
