def comprelistas():
    palabra = input('dime un numero y te lo partire')
    listas = []
    for letra in palabra:
        listas.append(letra)
        print(listas)
def comprelistas1():
    palabra = 'python'
    listas = [letra for letra in palabra]
    print(listas)

def ejercicio1():
    valores = [1, 2, 3, 4, 5, 6, 9.5]
    valores_cuadrado = []
    for valor in valores:
        valores_cuadrado.append(valor ** 2)
    print(valores_cuadrado)
def ejercicio2():
    valores = [1, 2, 3, 4, 5, 6, 9.5]
    valores_pares = []
    for valor in valores:
        if valor %2 == 0:
            valores_pares.append(valor)
    print(valores_pares)

def ejercicio3():
    temperatura_fahrenheit = [32, 212, 275]
    grados_celsius = []
    for temp in temperatura_fahrenheit:
        C = (temp - 32) * (5 / 9)
        grados_celsius.append(C)
    print(grados_celsius)
