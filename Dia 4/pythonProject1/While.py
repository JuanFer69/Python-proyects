def while1():
    monedas = 5
    while monedas > 0:
        monedas -=1
        print(f'tengo {monedas} monedas')
    else:
        print('no hat mas monedas')
def while2():
    respuesta = 's'
    while respuesta == 's':
        respuesta = input('quieres seguir? (s/n)')
    else:
        print('gracias')
def while3():
    nombre = input('Tu nombre')
    for letra in nombre:
        if letra == 'r':
            break
        print(letra)
def while4():
    nombre = input('Tu nombre')
    for letra in nombre:
        if letra == 'r':
            continue
        print(letra)
def ejerwhile():
    numero = int(input("Dime numero y te dire los anteriores"))
    while numero > 0:
        print(numero)
        numero -= 1
        print(numero)
def ejerwhile2():
    numero = 50
    while numero >= 0:
        if numero % 5 == 0:
            print(numero)
        numero -= 1
ejerwhile2()