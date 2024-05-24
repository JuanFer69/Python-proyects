def cantidad_atributos(**kwargs):
    return len(kwargs)
print(cantidad_atributos(x=1, y=3))

def lista_atributos(**kwargs):
    return list(kwargs.values())

print(lista_atributos(x=1, y=3,z=2))

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')
# Ejemplo de uso
describir_persona("Maria",color_ojos="azules", color_pelo="rubio")
