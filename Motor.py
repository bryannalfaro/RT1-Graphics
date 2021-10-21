from tracer import Raytracer
from Funciones.sphere import *
from Funciones.material import *
from Funciones.utilities import *
from Funciones.cube import *

r = Raytracer()
r.glCreateWindow(1000,1000)
r.glClear()

ivory = Material(diffuse=color(100,100,80),albedo=[0.6,0.3,0.1,0],spec=50)
rubber = Material(diffuse=color(80,0,0),albedo=[0.9,0.1,0.0,0],spec=10)
mirror = Material(diffuse=color(255,255,255),albedo=[0,10,0.8,0],spec=1500)
glass = Material(diffuse=color(255,255,255),albedo=[0,0.5,0.1,0.8],spec=1500,refractive_index=1.5)


r.light = Light(V3(-20,20,20),intensity=1,color=color(255,255,200))

r.scene = [
    #Sphere(V3(0, -1.5, -10), 1.5, ivory),
    #Sphere(V3(-2, 1, -12), 2, glass),
    #Sphere(V3(1, 1, -8), 1.7, rubber),
    #Sphere(V3(0, 5, -20), 5, mirror),
    Cube(V3(1.25, -0.5, -2) , [0.5,0.5,0.5], mirror)
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