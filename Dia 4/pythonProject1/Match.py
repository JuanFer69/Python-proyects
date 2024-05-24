def match1():
    serie = int(input('dime un numero'))
    match serie:
        case 1:
            print('samsung')
        case 2:
            print('nokia')
        case _:
            print('No hay prodcuto')
def match2():
    cliente = {'nombre':'Federico',
               'edad': 20,
               'ocupacion': 'programador'}
    pelicula = {
        'titulo': 'Inception',
        'ficha_twcnica':
            {'director': 'Christopher Nolan',
            'lanzamiento': 2010}}
    elementos = [cliente,pelicula,'libro']
    for e in elementos:
        match e:
            case {'nombre':nombre,
               'edad': edad,
               'ocupacion': ocupacion}:
                print('Es un cliente')
                print(nombre,edad,ocupacion)
            case {'titulo': titulo,
                'ficha_twcnica':
                {'director': protagonista,
                'lanzamiento': lanzamiento}}:
                print('Es una pelicula')
                print(titulo,protagonista,lanzamiento)
            case _:
                print('No se lo que es')
match2()



