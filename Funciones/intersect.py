'''
Universidad del Valle de Guatemala
Graficas por computadora
Proyecto Raytracer
Bryann Alfaro 19372

Referencia general> Clases de Dennis y proyecto 1.
'''
class Intersect(object):
    def __init__(self,distance,point,normal,texture = None):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.texture = texture

class Light(object):
    def __init__(self,position,intensity,color):
        self.position = position
        self.intensity = intensity
        self.color = color