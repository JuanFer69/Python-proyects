'''def abrir_leer(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        return "El archivo especificado no se encontró."

# Ejemplo de uso:
nombre_archivo = 'ejemplo.txt'
contenido_archivo = abrir_leer(nombre_archivo)
print(contenido_archivo)'''

def registro_error(nombre_archivo):
    with open(nombre_archivo, 'a') as archivo:
        contenido = archivo.write('"\nse ha registrado un error de ejecución"')
        return contenido
nombre_archivo = 'log_errores.txt'
contenido_archivo = registro_error(nombre_archivo)
print(contenido_archivo)


