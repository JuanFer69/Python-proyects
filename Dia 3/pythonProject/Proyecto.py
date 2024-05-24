#Pasa en min el texto
textousuario = input('Dime el texto que quieres ingresar')
textousuariomin = textousuario.lower()
# Cantidad de palabras
palabras = textousuario.split()
cantidad_palabras = len(palabras)
#Primera y ulima letra del texto
primeraletra = textousuario[0]
ultimaletra = textousuario[-1]
#Texto al revez en MIn
textoinvertido = ' '.join(textousuario.split()[::-1])

resultado = bool('Python' in textousuario)
#Pasar a min letras
tresletras = input("Ingrese tres letras : ")
tresletrasmin = tresletras.lower()
lista_letras = list(tresletrasmin)
# Contar la frecuencia de cada letra en el texto original
frecuencia_letra_1 = textousuariomin.count(tresletrasmin[0])
frecuencia_letra_2 = textousuariomin.count(tresletrasmin[1])
frecuencia_letra_3 = textousuariomin.count(tresletrasmin[2])

# Imprimir los resultados
print(f"Frecuencia de {tresletrasmin[0]}: {frecuencia_letra_1}")
print(f"Frecuencia de {tresletrasmin[1]}: {frecuencia_letra_2}")
print(f"Frecuencia de {tresletrasmin[2]}: {frecuencia_letra_3}")
print(f'Numero de palabras es: {cantidad_palabras}')
print(f'Primera letra es: {primeraletra}')
print(f'Ultima letra es: {ultimaletra}')
print(f'Texto Invertido es:{textoinvertido}')
print(f"¿La palabra 'Python' se encuentra en el texto? {resultado}")