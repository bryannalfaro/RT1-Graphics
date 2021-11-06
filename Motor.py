'''
Universidad del Valle de Guatemala
Graficas por computadora
Proyecto Raytracer
Bryann Alfaro 19372

Referencia general> Clases de Dennis y proyecto 1.
'''

from tracer import Raytracer
from Funciones.sphere import *
from Funciones.material import *
from Funciones.utilities import *
from Funciones.cube import *
from Funciones.triangle import *
from Funciones.texture import *
from Funciones.environment import *


r = Raytracer()
r.glCreateWindow(800,600)
r.glClear()

ivory = Material(diffuse=color(100,100,80),albedo=[0.6,0.3,0.1,0],spec=50)
rubber = Material(diffuse=color(80,0,0),albedo=[0.9,0.1,0.0,0],spec=50,refractive_index=0)
mirror = Material(diffuse=color(255,255,255),albedo=[0,10,0.8,0],spec=1500)
glass = Material(diffuse=color(150,180,200),albedo=[0,0.5,0.1,0.8],spec=150,refractive_index=1.5)
water = Material(diffuse=color(48, 80, 156), albedo=[0.6, 0.3, 0.1, 0], spec=64, refractive_index=1.35)
grass = Material(texture=Texture('./salidas/Soh.bmp'))
wood = Material(texture=Texture('./salidas/6d.bmp'))
tree = Material(texture=Texture('./salidas/Grass.bmp'))
skin = Material(texture=Texture('./salidas/a.bmp'))



r.light = Light(V3(-20,-20,20),intensity=2,color=color(255,255,255))

#MODEL OBJ
r.load('./salidas/wolf.obj',(-2,2,-4),(0.02,0.02,0.02),(pi,pi/2,0))
r.draw_arrays('TRIANGLES',skin)

#Suelo
r.scene.append(Cube(V3(1, 2, -1.5), 2.5, water))
r.scene.append(Cube(V3(-1.5, 2, -1.5), 2.6, grass))
r.scene.append(Cube(V3(-1.8, 2, -4), 2.9, grass))
r.scene.append(Cube(V3(1, 2, -4), 2.8, grass))

#arbol

r.scene.append(Cube(V3(1, -0.5, -2.5), 1, wood))
r.scene.append(Cube(V3(1, -0.1, -2.5), 1, wood))
r.scene.append(Cube(V3(1, -1.5, -2.5), 1.5, tree))

#arbol par triangulo
r.scene.append(Cube(V3(-0.4, -0.5, -2.5), 0.7, wood))
r.scene.append(Cube(V3(-0.4, -0.1, -2.5), 0.7, wood))
r.scene.append(Cube(V3(-0.4, -1.5, -2.5), 1, tree))

#triangulo tree
r.scene.append(Cube(V3(-2, -0.1, -3), 1, wood))
r.scene.append(Cube(V3(-2, -1, -3), 1, wood))
r.scene.append(Triangle(V3(-5,-2,-4),V3(-3,-4,-4),V3(-1,-2,-4),tree))

r.environment = Env('./salidas/3o.bmp')
r.render()
r.glFinish("./salidas/output4.bmp")
