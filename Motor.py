from tracer import Raytracer
from Funciones.sphere import *
from Funciones.material import *
from Funciones.utilities import *
from Funciones.cube import *
from Funciones.triangle import *

r = Raytracer()
r.glCreateWindow(1000,1000)
r.glClear()

ivory = Material(diffuse=color(100,100,80),albedo=[0.6,0.3,0.1,0],spec=50)
rubber = Material(diffuse=color(80,0,0),albedo=[0.9,0.1,0.0,0],spec=50,refractive_index=0)
mirror = Material(diffuse=color(255,255,255),albedo=[0,10,0.8,0],spec=1500)
glass = Material(diffuse=color(150,180,200),albedo=[0,0.5,0.1,0.8],spec=150,refractive_index=1.5)
water = Material(diffuse=color(51, 83, 152), albedo=[0.6, 0.3, 0.1, 0], spec=64, refractive_index=1.35)

r.light = Light(V3(-20,10,20),intensity=8,color=color(255,255,255))

r.scene = [
    #Sphere(V3(0, -1.5, -10), 1.5, ivory),
    Sphere(V3(2, 10, -20), 4, mirror),
    #Sphere(V3(1, -4, -15), 5, rubber),
    #Sphere(V3(1, 6, -15), 7, water),
    #Cube(V3(1, 10, -18) , [10,10,10], water),
    #Cube(V3(12, 10, -18) , [10,10,10], water),
    Cube(V3(-9, 10, -30) , [10,10,10], water),
    Triangle(V3(-1,-1,-8),V3(1,-1,-8),V3(0,1,-8),ivory)
]
'''
r.scene = [
  Sphere(V3(0, -1.5, -10), 1.5, ivory),
  Sphere(V3(-2, 1, -12), 2, mirror),
  Sphere(V3(1, 1, -8), 1.7, rubber),
  Sphere(V3(-3, 3, -10), 2, mirror),
]'''

r.render()
r.glFinish("./salidas/output.bmp")