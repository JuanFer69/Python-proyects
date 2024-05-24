def ayuda1():
    dic = {'clave1': 100, 'calve2': 500}
    dic.items()
    print(dic.popitem())

def lstrp():
    texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
    caracteres_a_eliminar = ',:_#%'
    resultado = texto.lstrip(caracteres_a_eliminar)
    print(resultado)

def inserrt():
    frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
    frutas.insert(3, 'naranja')
    print(frutas)


def isdisjoi():
    marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
    marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
    conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
    print(conjuntos_aislados)

isdisjoi()