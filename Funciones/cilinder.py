from Funciones.math import *
from Funciones.intersect import *


class Cilinder(object):
    def __init__(self, altura, radio, posicion, material):
        self.altura = altura
        self.radio = radio
        self.posicion = posicion
        self.material = material

    def ray_intersect(self, origin, direction):
        # Formula a * t^2 + b * t + c = 0
        a = direction.x**2+direction.z**2
        if a == 0:
            return None

        b = 2 * (origin.x*direction.x + origin.z*direction.z)
        c = origin.x**2 + origin.z**2 - self.radio**2

        disc = b**2 - 4*a*c

        if disc < 0:
            return None
