def suma_cuadrados(*args):
    suma = 0
    for num in args:
        suma += num **2
    return suma
# Ejemplo de uso
resultado = suma_cuadrados(2, 3, 4)
print(resultado)  # Output: 29 (2^2 + 3^2 + 4^2 = 4 + 9 + 16 = 29)

