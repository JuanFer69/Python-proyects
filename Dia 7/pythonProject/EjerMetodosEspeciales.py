'''class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return (f'"{self.titulo}", de {self.autor}')


mi_libro = Libro('titulo1','Juan',123)
print(mi_libro)'''

'''class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas
mi_libro = Libro('titulo1','Juan',123)
print(len(mi_libro))'''

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")

mi_libro = Libro('titulo1','Juan',123)
del mi_libro