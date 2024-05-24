def Busdiccionario1():# Simple
    diccionario = {'nombre':'Juan','apellido':'Falla','edad':20}
    consulta = diccionario['nombre'],diccionario['apellido']
    print(consulta)
    print(type(diccionario))
def Busdiccionario2():#con Listas
    diccionario = {'c1':55,'c2':[10,20,30],'c3': {'s1':100,'s2':200}}
    print(diccionario['c2'][2])
def Busdiccionario3():#busqieda clave-clave-cont
    diccionario = {'c1':55,'c2':[10,20,30],'c3': {'s1':100,'s2':[200,300]}}
    print(diccionario['c3']['s2'][1])
def Busdiccionario4():#
    diccionario = {'c1':55,'c2':[10,20,30],'c3': {'s1':100,'s2':[200,300]}}
    print(diccionario['c3']['s2'][1])
def ejercicio1():
    dic = {'c1':['a','b','c'],'c2':['d','e','f']}
    print(dic['c2'][1].upper())
def Añadiccionario5():# clave y contenido
    dic = {1: ['a', 'b', 'c'], 2: ['d', 'e', 'f']}
    dic[3] = 'c'
    print(dic)
def Añadiccionario6():# contenido
    dic = {1: ['a', 'b', 'c'], 2: ['d', 'e', 'f'],3 :{3.1:100,3.2:[200,300]}}
    print(dic)
def Sobrediccionario6():# Sobreescribir contenido
    dic = {1: ['a', 'b', 'c'], 2: ['d', 'e', 'f'],3 :{3.1:100,3.2:[200,300]}}
    dic[1][0] = 'z'
    print(dic)
    print(dic.keys())
    print(dic[3].keys())
    print(dic.values())
    print(dic.items())
def ejercicio1():
    mi_dict = {"valores_1": {"v1": 3, "v2": 6}, "puntos": {"points1": 9, "points2": [10, 300, 15]}}
    print(mi_dict['puntos']['points2'][1])
def ejercicio2():
    mi_dic = {"nombre": "Karen", "apellido": "Jurgens", "edad": 35, "ocupacion": "Periodista"}
    mi_dic['edad'],mi_dic['ocupacion']= 36,'Editora'
    mi_dic['pais']= 'Colombia'
    print(mi_dic)
ejercicio2()
