def por_posicion():
    mitexto = 'Este es una prueba'
    resultado = mitexto[5]
    print(resultado)
def por_letra():
    mitexto = 'Este es una prueba'
    resultado = mitexto.index('a')
    print(resultado)
def por_letra_revez():
    mitexto = 'Este es una prueba'
    resultado = mitexto.rindex('a')
    print(resultado)
por_letra()