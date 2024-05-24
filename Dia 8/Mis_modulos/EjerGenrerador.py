'''def mi_generador():
    n = 7
    while True:
        yield n
        n += 7

generador = mi_generador()
print(next(generador))
print(next(generador))
print(next(generador))
'''

def perder_vida():
    vidas = 3
    while vidas > 0:
        yield f'Te quedan {vidas} vidas'
        vidas -= 1
    yield "Game Over"

perder_vida_generador = perder_vida()

# Probando el generador
print(next(perder_vida_generador))  # Imprimirá "Te quedan 3 vidas"
print(next(perder_vida_generador))  # Imprimirá "Te quedan 2 vidas"
print(next(perder_vida_generador))  # Imprimirá "Te quedan 1 vidas"
print(next(perder_vida_generador))  # Imprimirá "Game Over"

