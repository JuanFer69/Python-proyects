def tuple1():
    mi_tuple = 0,1,(10,20),3,'hola'
    print(mi_tuple[2][0])
    print(type(mi_tuple))
def tuple2():#Casting para convertit en list
    mi_tuple = 0,1,(10,20),3,'hola'
    mi_list = list(mi_tuple) #Pasamos tuple - list
    mi_list = tuple(mi_list) #Pasamos list - tuple
    print(mi_list)
    print(type(mi_list))
def tuple3():#Asignar valores a variables
    mi_tuple = 0,1,(10,20),3,'hola'
    x,y,z,a,e = mi_tuple
    print(a)
    print(type(a))

def tuple4():#Cuantas veces aparece el dato
    mi_tuple = 0,1,1,3,'hola'
    x,y,z,a,e = mi_tuple
    print(mi_tuple.count(1))
tuple4()