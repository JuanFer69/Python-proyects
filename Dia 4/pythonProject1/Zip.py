def zip1():
    nombres = ["Juan", "María", "Carlos", "Ana", "Pedro", "Luisa"]
    edades = [12,15,18,18,17,16]
    combinados = list(zip(nombres,edades))
    print(combinados)
def ejercicio1():
    capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
    paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
    combinados = list(zip(capitales,paises))
    for capital,pais in combinados:
        print(f'La capital de {pais} es {capital}')
def ejercicio2():
    numeros_espanol = ["uno", "dos", "tres", "cuatro", "cinco"]
    numeros_portugues = ["um", "dois", "três", "quatro", "cinco"]
    numeros_ingles = ["one", "two", "three", "four", "five"]
    # Crear un objeto zip
    numeros_zip = zip(numeros_espanol, numeros_portugues, numeros_ingles)

    # Convertir el objeto zip en una lista
    numeros = list(numeros_zip)

    # Mostrar la lista de traducciones
    print(numeros)
ejercicio1()