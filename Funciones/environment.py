'''
Universidad del Valle de Guatemala
Graficas por computadora
Proyecto Raytracer
Bryann Alfaro 19372

Referencia general> Clases de Dennis y proyecto 1.
'''
import struct
from math import atan2,acos,pi
from Funciones.utilities import color
from Funciones.utilities import op

class Env(object):
    def __init__(self,path):
        self.path = path
        self.pixels = []
        self.read()

    #Using same structure as Texture charge
    def read(self):
        image = open(self.path,'br')
        image.seek(10)
        val = image.read(4)
        header_size = struct.unpack('=l',val)[0]
        image.seek(18)
        self.width = struct.unpack('=l',image.read(4))[0]
        self.height = struct.unpack('=l',image.read(4))[0]
        image.seek(header_size)

        for y in range(self.height):
            self.pixels.append([])
            for _ in range(self.width):
                b= ord(image.read(1))
                g= ord(image.read(1))
                r= ord(image.read(1))
                self.pixels[y].append(color(r,g,b))
        image.close()

    def get_color(self,direction):

       #Formula implemented from Github of Dennis
       x = int( (atan2( direction.z, direction.x) / op()) * self.width)
       y = int( acos(-direction.y) / pi * self.height )
       return self.pixels[y][x]