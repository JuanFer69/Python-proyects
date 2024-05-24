import zipfile
#comprimir archivos
""" #comprimir archivos
mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w')

mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

mi_zip.close()

"""
#Descomprimir
"""
zip_abierto = zipfile.ZipFile('archivo_comprimido.zip')

zip_abierto.extractall()"""

#comprimir archivos
"""import shutil

# Directorio que deseas comprimir
directorio_a_comprimir = '/ruta/del/directorio'

# Nombre y ubicación del archivo comprimido
nombre_archivo_comprimido = '/ruta/del/archivo_comprimido.zip'

# Comprimir el directorio en un archivo zip
shutil.make_archive(nombre_archivo_comprimido, 'zip', directorio_a_comprimir)

print("¡Directorio comprimido con éxito!")"""

#Descomprimir
import shutil

# Ruta y nombre del archivo comprimido que deseas descomprimir
archivo_comprimido = 'C:\\Users\\Juan Fernando\\OneDrive\\Documentos\\Curso de python\\Dia 9\\pythonProject\\Proyecto+Dia+9.zip'

# Directorio donde deseas extraer los archivos
directorio_destino = 'C:\\Users\\Juan Fernando\\OneDrive\\Documentos\\Curso de python\\Dia 9\\pythonProject'

# Descomprimir el archivo en el directorio destino
shutil.unpack_archive(archivo_comprimido, directorio_destino, 'zip')

print("¡Archivo descomprimido con éxito!")
