import re

def verificar_saludo(frase):
    if re.match(r'\bHola', frase):
        print("Ok")
    else:
        print("No has saludado")

# Ejemplo de uso
frase = input("Ingresa una frase: ")
verificar_saludo(frase)

import re


def verificar_cp(cp):
    # Definimos el patrón para el código postal
    patron = r'^[A-Za-z]{2}\d{4}$'

    # Verificamos si el código postal coincide con el patrón
    if re.match(patron, cp):
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")


# Ejemplo de uso
codigo_postal = input("Ingrese el código postal: ")
verificar_cp(codigo_postal)
