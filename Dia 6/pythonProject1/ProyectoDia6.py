from pathlib import Path
import os
from os import system
import time

# Definir la ruta base de las recetas
RUTA_BASE_RECETAS = Path('/Users/Juan Fernando/OneDrive/Documentos/Curso de python/Dia 6/pythonProject1/Recetas')

# Diccionario para mapear opciones a rutas de recetas
OPCIONES_RECETAS = {
    1: RUTA_BASE_RECETAS / 'Carnes',
    2: RUTA_BASE_RECETAS / 'Ensaladas',
    3: RUTA_BASE_RECETAS / 'Pastas',
    4: RUTA_BASE_RECETAS / 'Postres'
}

def bienvenida():
    num_carpetas = sum(1 for elemento in RUTA_BASE_RECETAS.iterdir() if elemento.is_dir())
    print("Las recetas están en:", RUTA_BASE_RECETAS)
    print(f"Tienes {num_carpetas} carpetas")
    input("Presiona Enter para continuar...")


def mostrar_menu():
    system('cls')
    print('''¡Bienvenido al Administrador de Recetas!

[1] - Leer receta
[2] - Crear receta
[3] - Crear categoría
[4] - Eliminar receta
[5] - Eliminar categoría
[6] - Finalizar programa''')


def manejar_opcion(opcion_elegida):
    while True:
        if opcion_elegida == 1:
            leer_receta()
            return True

        elif opcion_elegida == 2:
            crear_receta()
            return True

        elif opcion_elegida == 3:
            crear_categoria()
            return True

        elif opcion_elegida == 4:
            eliminar_receta()
            return True

        elif opcion_elegida == 5:
            eliminar_categoria()
            return True

        elif opcion_elegida == 6:
            print('Elegiste finalizar programa')
            return False

        else:
            opcion_elegida = int(input("Opción no válida. Por favor, elige un número del 1 al 6: "))
            if opcion_elegida.isdigit():
                opcion_elegida = int(opcion_elegida)
            else:
                print("Entrada no válida. Por favor, ingresa un número entero del 1 al 6.")
            return True


def leer_receta():
    system('cls')
    print("Carpetas en la ruta:", RUTA_BASE_RECETAS)
    for indice, nombre_carpeta in enumerate(RUTA_BASE_RECETAS.iterdir(), start=1):
        print(f"{nombre_carpeta.name} [{indice}]")
    opcion_leer = int(input('Qué categoría quieres: '))
    system('cls')
    if opcion_leer in OPCIONES_RECETAS:
        ruta_recetas = OPCIONES_RECETAS[opcion_leer]
        print(f"{ruta_recetas.name} tiene las siguientes recetas, ¿cuál quieres leer?")
        for indice, elemento in enumerate(ruta_recetas.iterdir(), start=1):
            print(f"{elemento.name} [{indice}]")
        opcion_receta = int(input('Qué receta quieres leer: '))
        if 1 <= opcion_receta <= len(list(ruta_recetas.iterdir())):
            archivo_receta = list(ruta_recetas.iterdir())[opcion_receta - 1]
            with open(archivo_receta, 'r') as archivo:
                contenido = archivo.read()
                print(contenido)
        else:
            print("Opción de receta inválida.")
    else:
        print("Opción de categoría inválida.")


def crear_receta():
    system('cls')
    print("Carpetas en la ruta:", RUTA_BASE_RECETAS)
    for indice, nombre_carpeta in enumerate(RUTA_BASE_RECETAS.iterdir(), start=1):
        print(f"{nombre_carpeta.name} [{indice}]")

    opcion_crear = int(input('En qué categoría quieres crear la receta: '))
    system('cls')

    if opcion_crear in OPCIONES_RECETAS:
        ruta_crear = OPCIONES_RECETAS[opcion_crear]
        nombre_receta = input('Ingresa el nombre de la receta: ')

        # Verificar si ya existe una receta con el mismo nombre
        if (ruta_crear / nombre_receta).exists():
            print("Ya existe una receta con ese nombre en la categoría seleccionada.")
        else:
            contenido_receta = input('Ingresa el contenido de la receta: ')

            with open(ruta_crear / nombre_receta, 'w') as archivo:
                archivo.write(contenido_receta)
            print("Receta creada exitosamente.")
    else:
        print("Opción de categoría inválida.")


def crear_categoria():
    system('cls')
    print("Carpetas en la ruta:", RUTA_BASE_RECETAS)
    for indice, nombre_carpeta in enumerate(RUTA_BASE_RECETAS.iterdir(), start=1):
        print(f"{nombre_carpeta.name} [{indice}]")
    nombre_categoria = input('qué categoría quieres crear dime el nombre:')
    ruta_nueva_categoria = RUTA_BASE_RECETAS / nombre_categoria
    system('cls')

    if ruta_nueva_categoria.exists():
        print("Ya existe una categoría con ese nombre.")
    else:
        try:
            os.mkdir(ruta_nueva_categoria)  # MAKDIRECTORY
            print("Nueva categoría creada exitosamente.")
        except OSError as e:
            print(f"No se pudo crear la categoría: {e}")


def eliminar_receta():
    system('cls')
    print("Carpetas en la ruta:", RUTA_BASE_RECETAS)
    for indice, nombre_carpeta in enumerate(RUTA_BASE_RECETAS.iterdir(), start=1):
        print(f"{nombre_carpeta.name} [{indice}]")
    opcion_categoria = int(input('Qué categoría quieres: '))
    system('cls')
    if 1 <= opcion_categoria <= len(list(RUTA_BASE_RECETAS.iterdir())):
        ruta_categoria = list(RUTA_BASE_RECETAS.iterdir())[opcion_categoria - 1]
        print(f"{ruta_categoria.name} tiene las siguientes recetas, ¿cuál quieres eliminar?")
        recetas = list(ruta_categoria.iterdir())
        for indice, receta in enumerate(recetas, start=1):
            print(f"{receta.name} [{indice}]")
        opcion_receta = int(input('Qué receta quieres eliminar: '))
        if 1 <= opcion_receta <= len(recetas):
            archivo_receta = recetas[opcion_receta - 1]
            # Verificar si el archivo existe antes de intentar eliminarlo
            if os.path.exists(archivo_receta):
                # Eliminar el archivo
                os.remove(archivo_receta)
                print(f"La receta {archivo_receta.name} ha sido eliminada.")
                # Actualizar la lista de recetas disponibles en la categoría
                recetas = list(ruta_categoria.iterdir())
            else:
                print("El archivo de receta no existe.")
        else:
            print("Opción de receta inválida.")
    else:
        print("Opción de categoría inválida.")


def eliminar_categoria():
    system('cls')
    print("Carpetas en la ruta:", RUTA_BASE_RECETAS)
    for indice, nombre_carpeta in enumerate(RUTA_BASE_RECETAS.iterdir(), start=1):
        print(f"{nombre_carpeta.name} [{indice}]")
    opcion_categoria = int(input('Qué categoría quieres eliminar? Ingresa el número: '))

    carpetas = list(RUTA_BASE_RECETAS.iterdir())

    if 1 <= opcion_categoria <= len(carpetas):
        ruta_nueva_categoria = carpetas[opcion_categoria - 1]

        if ruta_nueva_categoria.is_dir():
            try:
                os.rmdir(ruta_nueva_categoria)
                print("Categoría eliminada exitosamente.")
            except OSError as e:
                print(f"No se pudo eliminar la categoría: {e}")
        else:
            print("El elemento seleccionado no es una categoría.")
    else:
        print("Opción de categoría inválida.")

def contar_regresivamente(tiempo):
    for i in range(tiempo, 0, -1):
        print(i, end=', ', flush=True)
        time.sleep(1)
    print("Limpiando la pantalla...")
    time.sleep(1)
    system('cls')

bienvenida()
continuar_ejecucion = True
while continuar_ejecucion:
    mostrar_menu()
    opcion_elegida = int(input("Elige una opción: "))
    continuar_ejecucion = manejar_opcion(opcion_elegida)

    # Esperar 5 segundos antes de limpiar la pantalla
    print("Limpiando la pantalla en 5 segundos...")
    time.sleep(5)
    system('cls')
 # Contar regresivamente antes de limpiar la pantalla
    print("Limpiando la pantalla en 5 segundos...")
    contar_regresivamente(5)