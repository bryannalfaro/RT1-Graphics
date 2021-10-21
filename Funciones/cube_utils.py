from Funciones.math import *
from Funciones.plane import *
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
    planos = []
    planos.append(Plane(sum(position, V3(sizebox[0]/2,0,0)),normals[0], material)) #face1
    planos.append(Plane(sum(position, V3(-sizebox[0]/2,0,0)),normals[1],material))#face2
    planos.append(Plane(sum(position, V3(0,sizebox[1]/2,0)),normals[2], material))#face3
    planos.append(Plane(sum(position, V3(0,-sizebox[1]/2,0)),normals[3], material))#face4
    planos.append(Plane(sum(position, V3(0,0,sizebox[2]/2)),normals[4], material))#face5
    planos.append(Plane(sum(position, V3(0,0,-sizebox[2]/2)),normals[5], material))#face6
    return planos

def get_min_bounds(position,sizebox):
    Boundmin = [0,0,0]
    epsilon =  1e-6
    Boundmin[0] = position[0] - (epsilon + sizebox[0]/2)
    Boundmin[1] = position[1] - (epsilon + sizebox[1]/2)
    Boundmin[2] = position[2] - (epsilon + sizebox[2]/2)

    return Boundmin

def get_max_bounds(position,sizebox):
    Boundmax = [0,0,0]
    epsilon =  1e-6
    Boundmax[0] = position[0] + (epsilon + sizebox[0]/2)
    Boundmax[1] = position[1] + (epsilon + sizebox[1]/2)
    Boundmax[2] = position[2] + (epsilon + sizebox[2]/2)

    return Boundmax