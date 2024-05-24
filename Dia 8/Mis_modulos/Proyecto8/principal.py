from numeros import TurneroFarmacia

turnero = TurneroFarmacia()

while True:
    tramite = int(input("¿Qué trámite quieres hacer?\n1- Perfumeria\n2_ Farmacia\n3. Cosmeticos\n"))
    if tramite == 1:
        obtener_turno = turnero.agregar_mensaje_atencion(turnero.obtener_turno_yield)
        print(obtener_turno('perfumeria'))
    elif tramite == 2:
        obtener_turno = turnero.agregar_mensaje_atencion(turnero.obtener_turno_yield)
        print(obtener_turno('farmacia'))
    elif tramite == 3:
        obtener_turno = turnero.agregar_mensaje_atencion(turnero.obtener_turno_yield)
        print(obtener_turno('cosmeticos'))

    otro_turno = input("¿Quieres sacar otro turno? (S/N): ")
    if otro_turno.lower() == 'n':
        print('Hasta la proxima')
        break

