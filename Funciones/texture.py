'''
Universidad del Valle de Guatemala
Graficas por computadora
Proyecto Raytracer
Bryann Alfaro 19372

Referencia general> Clases de Dennis y proyecto 1.
'''
import struct
from Funciones.utilities import color

class Texture(object):
    def __init__(self,path):
        self.path = path
        self.framebuffer = []
        self.read()

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
            self.framebuffer.append([])
            for x in range(self.width):
                b= ord(image.read(1))/255
                g= ord(image.read(1))/255
                r= ord(image.read(1))/255
                self.framebuffer[y].append(color(r,g,b))
        image.close()

    def get_color(self,tx,ty):
        x = round(tx*self.width)-1
        y = round(ty*self.height)-1
        return self.framebuffer[y][x]