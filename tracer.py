from Funciones.math import *
from Funciones.utilities import *
from Funciones.characters import *
from math import pi,tan

class Raytracer(object):
    def __init__(self):
        self.default_color = color(0,0,139)
        self.cl_color = BLACK

    def point(self, x, y):
        self.framebuffer[y][x] =self.default_color

    def glInit(self):
        pass

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.framebuffer = []

    def glClear(self):
        self.framebuffer = [
            [self.cl_color for _ in range(self.width)] for _ in range(self.height)
            ]

    def glColor(self, r,g,b):
        try:
            self.default_color = color(r,g,b)
        except:
            self.default_color = color(int(r*255),int(g*255),int(b*255))

    def point(self, x, y):
        self.framebuffer[y][x] =self.default_color


    def cast_ray(self,origin,direction):
        return color(0,0,255)

    def render(self):
        fov = pi/2
        ar = self.width/self.height

        for y in range(self.height):
            for x in range(self.width):
                i = (2 * ((x+0.5)/self.width)-1)*(ar)*tan(fov/2)
                j = 1- 2*((y+0.5)/self.height)*tan(fov/2)

                direction = norm(V3(i,j,-1))
                col= self.cast_ray(V3(0,0,0),direction)
                self.glColor(col[0],col[1],col[2])
                self.point(x,y)


    def glFinish(self,filename):
        write(filename,self.width,self.height,self.framebuffer)
