'''import datetime

mi_hora = datetime.time(17,35)


print(mi_hora)
print(mi_hora.hour)
'''

from datetime import datetime

# Fecha de nacimiento
fecha_nacimiento = datetime(2003, 6, 4)  # Ejemplo: 15 de mayo de 1990

# Fecha actual
fecha_actual = datetime.now()

# Calcular la diferencia de tiempo
diferencia = fecha_actual - fecha_nacimiento

# Calcular la edad en años
edad = diferencia.days // 365  # Aproximación a años enteros

print("Edad:", edad, "años")


