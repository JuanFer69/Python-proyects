from random import *
nombre_usuario = input('dime tu nombre')
intentos = 8
numcomputadora = randint(1,10)
print(f'Hola {nombre_usuario} He pensado en un numero tienes {intentos} intentos')
for a in range(intentos):
    numusuario = int(input('Dime un numero'))
    if numusuario == numcomputadora:
        print(f'¡Felicidades, {nombre_usuario}! Has adivinado el número en {8 - intentos + 1} intentos.')
        break
    elif numusuario < 1 or numusuario > 10:
        print('El número no está permitido. Intenta nuevamente.')
    elif numusuario < numcomputadora:
        print('Haz elegido un número menor al que pensé.')
    elif numusuario > numcomputadora:
        print('Haz elegido un número mayor al que pensé.')
    intentos -= 1
    print(f'Te quedan {intentos} intentos.')
print('programa terminado')
