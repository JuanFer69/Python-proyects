def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f"{nombre}, la suma de tus números es {suma_numeros}"

# Ejemplo de uso:
resultado = numeros_persona("Juan", 1, 2, 3, 4, 5)
print(resultado)

