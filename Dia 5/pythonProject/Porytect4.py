def contar_primos(maximo):
    primos = []
    for num in range(2, maximo + 1):
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
    print("Números primos del 0 al", maximo, ":", primos)
    return len(primos)

# Ejemplo de uso
cantidad_primos = contar_primos(200)
print("Cantidad de números primos encontrados:", cantidad_primos)
