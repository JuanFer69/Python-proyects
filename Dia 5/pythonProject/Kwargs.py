def prueba(num1,num2,*args,**kwargs):
    print(f'el primer valor es {num1}')
    print(f'el segundo valor es {num2}')

    for arg in args:
        print(f'arg = {arg}')

    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')

arguments = [3,4,5,6,7]
kwarguments = {'x':1,'y':2,'z':3}
prueba(15,50,*arguments,**kwarguments)
