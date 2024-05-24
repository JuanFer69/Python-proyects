def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(suma(1,2,2))

def suma2(*args):
    return sum(args)
print(suma2(1,2,3,3,4))