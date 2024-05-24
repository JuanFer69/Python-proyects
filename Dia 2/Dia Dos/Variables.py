def Casting(): #Transformacion
    num1 = 5.8
    print(num1)
    print(type(num1))

    num2 = int(num1)
    print(num2)
    print(type(num2))

def ejercicio1():
    añoactual= 2024
    edad = int((input('Dime tu edad')))
    resultado =  añoactual - edad
    print('Tu año de nacimiento es:\n',resultado)
    print(type(resultado))

def ejercicio2():
    num1 = "7.5"
    num2 = "10"
    print(float(num1) + int(num2))
def ejercicio3():
    color = 'rojo'
    matricula = 2423
    print(f'hola mi color es {color} \n y su matricula es {matricula}')
def ejercicio4():
    x = 7
    y = 2
    print(f'La suma de {x} + {y} = {x+y}')
    print(f'La resta de {x} - {y} = {x - y}')
    print(f'La multiplicacion de {x} * {y} = {x * y}')
    print(f'La division de {x} \\ {y} = {x / y}')
    print(f'La division al piso de {x} \\ {y} = {x // y}')
    print(f'El modulo de {x} % {y} = {x % y}')
    print(f'El elevado de {x} ala {y} = {x ** y}')
    print(f'El elevado de {x} ala {3} = {x **3}')
    print(f'La raiz cuadradada de {x} = {x **0.5}')

def ejercicio5():
    print('Tu número redondeado es:', round(float(input('Dime el número que quieres redondear: '))))
    valor = round(3.7,2)
    print(valor)
    print(type(valor))

def proyecto1():
    nombre = input('Dime tu nombre')
    ventas = int(input('Dime tus venta'))
    operacion = round(ventas * 13 / 100,2)
    print(f'Ok {nombre}.este mes ganaste ${operacion}')


proyecto1()