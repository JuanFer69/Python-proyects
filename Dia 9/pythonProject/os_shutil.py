import os

# Especifica la ruta completa al archivo
ruta_archivo = "ruta/al/directorio/archivo.txt"

# Intenta abrir el archivo
import shutil

# Especifica el directorio de origen y el directorio de destino
directorio_origen = 'ruta/al/directorio/de/origen'
directorio_destino = 'ruta/al/directorio/de/destino'

# Copia todos los archivos y directorios del directorio de origen al directorio de destino
shutil.copytree(directorio_origen, directorio_destino)

print("Archivos copiados correctamente.")



import send2trash

#Eliminar archivos y mandar a papelera
send2trash.send2trash()


import os

# Especifica el directorio raíz que deseas explorar
directorio_raiz = '/ruta/del/directorio'

# Itera sobre el árbol de directorios usando os.walk()
for carpeta, subcarpeta, archivo in os.walk(directorio_raiz):
    print(f'En la carpeta :: {carpeta}')
    print(f'Los subdirectorios son : ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print(f'Los archivos son : ')
    for arch in archivo:
        print(f'\t{arch}')

