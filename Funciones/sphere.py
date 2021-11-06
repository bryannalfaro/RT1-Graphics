'''
Universidad del Valle de Guatemala
Graficas por computadora
Proyecto Raytracer
Bryann Alfaro 19372

Referencia general> Clases de Dennis y proyecto 1.
'''
from Funciones.math import *
from Funciones.intersect import *
from math import atan2,acos

#texture reference - http://raytracerchallenge.com/bonus/texture-mapping.html

class Sphere(object):
    def __init__(self,  center, radius,material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, origin,direction):
        L = sub(self.center, origin)
        tca = dot(L,direction)
        l = length(L)
        d2 = l**2 - tca**2

        if d2 > self.radius**2:
            return None
        thc = (self.radius**2-d2)**(1/2)

        t0 = tca-thc
        t1 = tca+thc

        if t0<0:
            t0=t1
        if t0<0:
            return None

        hit = sum(origin,mul(direction,t0))
        normal = norm(sub(hit,self.center))

        return Intersect(
            distance = t0,
            normal = normal,
            point = hit,

        )
