from tracer import Raytracer
from Funciones.sphere import *
from Funciones.material import *
from Funciones.utilities import *

r = Raytracer()
r.glCreateWindow(1000,1000)
r.glClear()

m= Material(diffuse=color(255,0,255))

ivory = Material(diffuse=color(100,100,80))
rubber = Material(diffuse=color(80,0,0))


r.scene = [
  Sphere(V3(0, -1.5, -10), 1.5, ivory),
  Sphere(V3(-2, 1, -12), 2, m),
  Sphere(V3(1, 1, -8), 1.7, rubber),
  Sphere(V3(0, 5, -20), 5, ivory),
]

r.render()
r.glFinish("./salidas/output.bmp")