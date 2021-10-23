from Funciones.utilities import *
class Material(object):
    def __init__(self, diffuse = color(255,255,255),albedo=[1,0,0,0],spec=0,refractive_index = 0,texture=None):
        self.diffuse = diffuse
        self.albedo = albedo
        self.spec = spec
        self.refractive_index = refractive_index
        self.texture = texture
