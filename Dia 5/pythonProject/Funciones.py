def saludarpersona(nombre):
    '''
     Esta funcion sierve para decir el nombre
     al ejecutar la funcion con el parametro
     con la variable
    '''
    print('Hola ' +nombre)

def bienvenida(nombre_persona):
    print(f'¡Bienvenido {nombre_persona}!')

def cuadrado(un_numero):
    print(f"El cuadrado de {un_numero} es: {un_numero ** 2}")

def multiplicar(num1,num2):
    return num1 * num2

def potencia(num1,num2):
    operacion = num1 ** num2
    return operacion

def usd_a_eur(montodol):
    euros = montodol * 0.90
    return euros
dolares = 100
resulconversion = usd_a_eur(dolares)


def invertir_palabra(palabra):
    palabraresuelta = palabra[::-1].upper()
    return palabraresuelta
#palabre = 'hola'
#resultado = invertir_palabra(palabre)
#print(resultado)
def chequear3cifras(numero):
    return numero in range(100,1000)

#resultado = chequear3cifras(737)
#print(resultado)
def chequear3cifraslista(lista):
    lista3cifras = []
    lista2cifras = []
    for n in lista:
        if n in range(100,1000):
            lista3cifras.append(n)
        elif n in range(10,100):
            lista2cifras.append(n)
        else:
            pass
    return lista3cifras,lista2cifras
#lista =[1,22,333,44,555]
#resultado1 = chequear3cifraslista(lista)
#print(resultado1)

def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n < 0:
            return False
        else:
            pass
    return True
#lista = [1,2,5,7,-1]
#print(todos_positivos(lista))
def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n in range(0,1000):
            suma += n
        else:
            pass
    return suma
#lista = [1,2,3]
#print(suma_menores(lista))

def cantidad_pares(lista_numeros):
    pares = 0
    for n in lista_numeros:
        if n %2 == 0:
            pares += 1
        else:
            pass
    return pares

print(cantidad_pares([2,4,5,6]))




