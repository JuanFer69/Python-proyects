import random

def lanzar_dados():
    opciones = [1,2,3,4,5,6]
    dado1 = random.choice(opciones)
    dado2 = random.choice(opciones)
    return dado1,dado2
def evaluar_jugada(resultado_dado1,resultado_dado2):
    suma_dados = resultado_dado1 + resultado_dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
# Lanzar los dados
resultado_dado1, resultado_dado2 = lanzar_dados()

# Evaluar la jugada
mensaje = evaluar_jugada(resultado_dado1, resultado_dado2)
print(mensaje)