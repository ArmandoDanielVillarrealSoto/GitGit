#Calcular el volumen de una esfera a partir del radio

from math import pi

r = float(input("Si desea calcular el Volumen de una esfera inserte su radio:"))

volumen = 4/3 * pi * r ** 3

print("El volumen de la esfera es {} unidades cubicas".format(volumen))