from pathlib import Path

# Definir la ruta de la carpeta y el archivo
rutacarpeta = Path('/Users/Juan Fernando/OneDrive/Documentos/Curso de python/Dia 6/pythonProject1/Recetas')
rutaarchivo = rutacarpeta / 'Otroarchivo.txt'
# Comprobar si el archivo existe

if rutaarchivo.exists():
    print(f"El archivo {rutaarchivo.name} existe.")
else:
    print(f"El archivo {rutaarchivo.name} no existe.")
# Obtener el nombre de la carpeta
nombre_carpeta = rutacarpeta.name
print("Nombre de la carpeta:", nombre_carpeta)
# Obtener el nombre del archivo
nombre_carpeta = rutaarchivo.name
print("Nombre del archivo:", nombre_carpeta)

# Obtener el directorio padre de la carpeta
directorio_padre = rutacarpeta.parent
print("Directorio padre de la carpeta:", directorio_padre)


# Leer el contenido del archivo
with open(rutaarchivo, 'r') as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)
