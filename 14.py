#14.	Escribe un algoritmo o el respectivo diagrama de flujo que determine la energía (en Julios) de un objeto si se conoce la masa de un objeto (en kg) y la velocidad de la luz (en m/s).
import numpy as np
masa=int(input("Ingrese la masa del objeto en kg: "))
velocidad = 299792458 #m/s
Energia=float(masa*(velocidad**2))
print(format(Energia,'.1E'))
