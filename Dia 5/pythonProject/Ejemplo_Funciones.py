def cafemascaro(lista_precios):
    nombre_cafe_mayor = ''
    precio_mayor = 0
    for nombre, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            nombre_cafe_mayor = nombre
    return (nombre_cafe_mayor, precio_mayor)

precios_cafe = [('capuchino', 1.5), ('Éxpreso', 2.5), ('Moka', 1.9)]

nombre, precio = cafemascaro(precios_cafe)
print(f'El café más caro es {nombre} con un precio de ${precio}')
