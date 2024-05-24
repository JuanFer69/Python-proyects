def suma():
    n1 =  int(input('Numero 1 :'))
    n2 = int(input('Numero 2 :'))
    print(n1 + n2)
    print('Gracias por sumar' + n1)


try:
    suma() #Codigo que queremos pribar
except ValueError as e:
    print('Error:', e)
    print('No puede ser una palabra, te estoy pidiendo un número')
    #Codigo a ejecutar si hay un error
except TypeError as et:
    print('Error: ',et)
    print('Estas intentando concatenar tipos de variables distintas')
else:
    print('hiciste todo bien')#Codigo si no hay error
finally:
    print('Eso fue todo')#Codigo que se va a ejecutar de todos modos

def pedirnumero():
    while True:
        try:
            numero = int(input('dame un numero: '))
        except:
            print('Eso no es un numero')
        else:
            print(f'Ingresaste el numero : {numero}')
            break
        finally:
            print('todo OK')
pedirnumero()