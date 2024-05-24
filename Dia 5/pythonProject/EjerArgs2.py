def suma_absolutos(*args):
    suma = 0
    for n in args:
        num_absoluto = abs(n)
        suma += num_absoluto
    return suma

print(suma_absolutos(1,-2,3,-9))