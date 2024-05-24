import os
import re
from datetime import datetime

def buscar_numeros_serie(directorio_raiz):
    numeros_serie_encontrados = []
    fecha_inicio = datetime.now()

    # Expresión regular para buscar el patrón de números de serie
    patron = r'\b[N]\w{3}-\d{5}\b'

    # Recorre el directorio raíz y sus subdirectorios
    for carpeta, _, archivos in os.walk(directorio_raiz):
        for archivo in archivos:
            with open(os.path.join(carpeta, archivo), 'r') as file:
                contenido = file.read()
                matches = re.findall(patron, contenido)
                if matches:
                    # Agrega solo el nombre del archivo junto con los números de serie encontrados
                    for match in matches:
                        numeros_serie_encontrados.append((archivo, match))

    duracion_busqueda = datetime.now() - fecha_inicio
    return numeros_serie_encontrados, duracion_busqueda

def presentar_resultados(numeros_serie, duracion):
    print("----------------------------------------------------")
    print(f"Fecha de búsqueda: {datetime.now().strftime('%d/%m/%Y')}\n")
    print("ARCHIVO\t\t    NRO. SERIE")
    print("-------\t\t    ----------")
    for archivo, serie in numeros_serie:
        print(f"{archivo}\t{serie}")
    print(f"\nNúmeros encontrados: {len(numeros_serie)}")
    print(f"Duración de la búsqueda: {duracion.seconds + 1} segundos")
    print("----------------------------------------------------")

if __name__ == "__main__":
    directorio_raiz = 'C:\\Users\\Juan Fernando\\OneDrive\\Documentos\\Curso de python\\Dia 9\\pythonProject\\Mi_Gran_Directorio'  # Reemplaza con tu directorio raíz
    numeros_serie, duracion = buscar_numeros_serie(directorio_raiz)
    presentar_resultados(numeros_serie, duracion)


