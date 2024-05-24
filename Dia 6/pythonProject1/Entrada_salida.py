#Abre ARCHIVO
mi_archivo = open('prueba.txt')
#print(mi_archivo.read())
'''''''#lee todo el archivo'''

#Pone primera linea en mayusculas
'''unalinea = mi_archivo.readline()
print(unalinea.upper())'''

'''
with open('prueba.txt', 'r') as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea)'''

#Por cada linea haces :
'''for l in mi_archivo:
    print('aqui dice:' +l)'''
#Cierra archivo:
mi_archivo.close()