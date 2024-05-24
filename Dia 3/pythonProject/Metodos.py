def uppermetodo():
    mitexto = 'Este es una prueba'
    print(mitexto.upper())
def lowermetodo():
    mitexto = 'Este es una PRUEBA'
    print(mitexto.lower())
def splitmetodo():
    mitexto = 'Este es una prueba'
    print(mitexto.split("u"))

def joinmetodo():
        a = "Aprendo"
        b = "python"
        c = "con"
        d = "Anuel"
        e = " ".join([a,b,c,d])
        print(e)
def findmetodo():
    mitexto = 'Este es una prueba'
    resultado = mitexto.find("x")
    print(resultado)
def replacemetodo():
    mitexto = 'Este es una prueba'
    resultado = mitexto.replace("e",'o')
    print(resultado)
    
splitmetodo()
