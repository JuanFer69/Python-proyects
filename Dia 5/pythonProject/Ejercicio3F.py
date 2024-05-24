import random
def lanzar_moneda():
    opciones = ['Cara','Cruz']
    moneda = random.choice(opciones)
    return moneda
def probar_suerte(resultadomoneda,lista_numeros):
    if resultadomoneda == 'Cara':
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista_numeros
lista_numeros = [1,2,3,4,5]
lanzaminetomoneda = lanzar_moneda()
resultadoprobarsuerte = probar_suerte(lanzaminetomoneda,lista_numeros)
print(resultadoprobarsuerte)


