def minmax1():
    lista = [58,24,43,42,54,43]
    listamin = min(lista)
    listamax = max(lista)
    print(listamin)
    print(listamax)
def minmax2():
    lista = ['juan','carlos','alice']
    listamin = min(lista)
    listamax = max(lista)
    print(listamin)
    print(listamax)
def minmax3():
    dic = {'c1':'juan','c2':'carlos','c3':'alice'}
    dicmin = min(dic)
    dicmax = max(dic)
    print(dic.keys())
    print(dic.values())
    print(dic.items())
    print(dicmin)
    print(dicmax)

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
print(edad_minima)
