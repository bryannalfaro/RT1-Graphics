'''
Universidad del Valle de Guatemala
Graficas por computadora
Proyecto Raytracer
Bryann Alfaro 19372

Referencia general> Clases de Dennis y proyecto 1.
'''
from Funciones.math import *
from Funciones.intersect import *

#Reference>
#https://stackoverflow.com/questions/23975555/how-to-do-ray-plane-intersection
#https://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-plane-and-ray-disk-intersection
class Plane(object):
    def __init__(self,  pos, normalCoordinates,material):
        self.pos = pos
        self.normalCoordinates = norm(normalCoordinates)
        self.material = material


    def ray_intersect(self, origin,direction):

        if(abs(dot(direction, self.normalCoordinates)))>epsilon:
            t = dot(self.normalCoordinates,sub(self.pos,origin))/dot(direction,self.normalCoordinates)
            if t > 0:
                # p + t * v
                hit = sum(origin,mul(direction,t))

                return Intersect(
                    distance = t,
                    normal = self.normalCoordinates,
                    point = hit
                )
        return None
