'''
Universidad del Valle de Guatemala
Graficas por computadora
Proyecto Raytracer
Bryann Alfaro 19372

Referencia general> Clases de Dennis y proyecto 1.
'''
from Funciones.math import *
from Funciones.plane import *
from Funciones.material import *

def get_normals():
    normals = []
    normals.append(V3(1,0,0))
    normals.append(V3(-1,0,0))
    normals.append(V3(0,1,0))
    normals.append(V3(0,-1,0))
    normals.append(V3(0,0,1))
    normals.append(V3(0,0,-1))
    return normals

def get_planes(position,sizebox,normals,material):
    mid = sizebox/2

    planos = [
    Plane(sum(position, V3(mid,0,0)),normals[0], material), #face1
    Plane(sum(position, V3((-mid),0,0)),normals[1],material),#face2
    Plane(sum(position, V3(0,mid,0)),normals[2], material),#face3
    Plane(sum(position, V3(0,-(mid),0)),normals[3], material),#face4
    Plane(sum(position, V3(0,0,mid)),normals[4], material),#face5
    Plane(sum(position, V3(0,0,-(mid))),normals[5], material)#face6
    ]

    return planos

def get_Boundmin(position,sizebox):
    Boundmin = []

    Boundmin.append(position[0] - (epsilon + sizebox/2))
    Boundmin.append(position[1] - (epsilon + sizebox/2))
    Boundmin.append(position[2] - (epsilon + sizebox/2))

    return Boundmin

def get_max_bounds(position,sizebox):
    Boundmax = []
    Boundmax.append(position[0] + (epsilon + sizebox/2))
    Boundmax.append(position[1] + (epsilon + sizebox/2))
    Boundmax.append(position[2] + (epsilon + sizebox/2))

    return Boundmax

#reference https://raytracing.github.io/books/RayTracingTheNextWeek.html
def get_texture(plane,planeHit,Boundmin,Boundmax):
    divx = Boundmax[0]-Boundmin[0]
    divy = Boundmax[1]-Boundmin[1]
    divz = Boundmax[2]-Boundmin[2]

    if abs(plane.normalCoordinates[2]) > 0:
        u = (Boundmax[0] - planeHit.point[0]) / (divx)
        v = (Boundmax[1] - planeHit.point[1]) / (divy)

    elif abs(plane.normalCoordinates[1]) > 0:
        u = (Boundmax[0] - planeHit.point[0]) / (divx)
        v = (Boundmax[2] - planeHit.point[2]) / (divz)

    elif abs(plane.normalCoordinates[0]) > 0:
        u = (Boundmax[1] - planeHit.point[1]) / (divy)
        v = (Boundmax[2] - planeHit.point[2]) / (divz)

    return (u,v)