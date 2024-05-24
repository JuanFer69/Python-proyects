class TurneroFarmacia:
    def __init__(self):
        self.contador_perfumeria = 0
        self.contador_farmacia = 0
        self.contador_cosmeticos = 0

    def obtener_turno_yield(self, area):
        if area.lower() == 'perfumeria':
            while True:
                self.contador_perfumeria += 1
                yield f'P-{self.contador_perfumeria}'
        elif area.lower() == 'farmacia':
            while True:
                self.contador_farmacia += 1
                yield f'F-{self.contador_farmacia}'
        elif area.lower() == 'cosmeticos':
            while True:
                self.contador_cosmeticos += 1
                yield f'C-{self.contador_cosmeticos}'
        else:
            yield 'Área no válida'

    def agregar_mensaje_atencion(self, generator):
        def wrapper(*args, **kwargs):
            turno = next(generator(*args, **kwargs))
            return f'Su turno es: {turno}, Aguarde y será atendido'
        return wrapper


