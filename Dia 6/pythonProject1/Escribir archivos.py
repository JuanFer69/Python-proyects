with open('prueba2.txt', 'a') as archivo:
    archivo.write('Soy el nuevo texto')

# Ahora cerramos el archivo y lo abrimos nuevamente en modo lectura para leer el contenido
with open('prueba2.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)



registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

with open('registro.txt', 'a') as archivo:
    archivo.write('\t'.join(registro_ultima_sesion) + '\n')
with open('registro.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)