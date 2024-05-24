from pathlib import Path

ruta_base = Path.home()  # Obtiene la ruta base del usuario
ruta_relativa = "Curso Python/Día 6/practicas_path.py"  # Ruta relativa desde la ruta base

ruta = ruta_base.joinpath(ruta_relativa)  # Concatena la ruta base con la ruta relativa
print(ruta)
