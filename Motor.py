from tracer import Raytracer
from Funciones.sphere import *
from Funciones.material import *
from Funciones.utilities import *

r = Raytracer()
r.glCreateWindow(1000,1000)
r.glClear()

ivory = Material(diffuse=color(100,100,80),albedo=[0.6,0.3],spec=50)
rubber = Material(diffuse=color(80,0,0),albedo=[0.9,0.1],spec=10)

r.light = Light(V3(-20,-20,20),intensity=2,color=color(255,255,200))

r.scene = [
  Sphere(V3(0, -1.5, -10), 1.5, ivory),
  Sphere(V3(-2, 1, -12), 2, rubber),
  Sphere(V3(1, 1, -8), 1.7, rubber),
  Sphere(V3(0, 5, -20), 5, ivory),
]

r.render()
r.glFinish("./salidas/output.bmp")