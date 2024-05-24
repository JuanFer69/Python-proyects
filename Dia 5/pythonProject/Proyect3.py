def funcion2(*args):
    for n in range(1, len(args)):
        if args[n] == 0 and args[n-1] == 0:
            return True
    return False

resultado = funcion2(6,0,5,1,0,3,0,1)
print(resultado)