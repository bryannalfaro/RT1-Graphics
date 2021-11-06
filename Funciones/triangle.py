'''
Universidad del Valle de Guatemala
Graficas por computadora
Proyecto Raytracer
Bryann Alfaro 19372

Referencia general> Clases de Dennis y proyecto 1.
'''
from Funciones.math import *
from Funciones.intersect import *

#reference> https://www.scratchapixel.com/lessons/3d-basic-rendering/ray-tracing-rendering-a-triangle/ray-triangle-intersection-geometric-solution
#https://www.scratchapixel.com/code.php?id=9&origin=/lessons/3d-basic-rendering/ray-tracing-rendering-a-triangle
class Triangle(object):
    def __init__(self, vert0,vert1,vert2,material):
        self.vert0 = vert0
        self.vert1 = vert1
        self.vert2 = vert2
        self.material = material

    def ray_intersect(self, origin,direction):
        vert01 = sub(self.vert1,self.vert0)
        vert02 = sub(self.vert2,self.vert0)

        pvec = cross(direction,vert02)
        det = dot(vert01,pvec)

        #Culling
        if(det<epsilon):
            return None
        #else
        if(abs(det)<epsilon):
            return None
        #endif
        invDet = 1/det
        tvec = sub(origin,self.vert0)
        u = dot(tvec,pvec)*invDet
        if(u<0 or u>1):
            return None
        qvec = cross(tvec,vert01)
        v = dot(direction,qvec)* invDet
        if (v<0 or u+v>1):
            return None

        t = dot(vert02,qvec)*invDet

        #else
        vert01 = sub(self.vert1,self.vert0)
        vert02 = sub(self.vert2,self.vert0)

        N = cross(vert01,vert02)
        denom = dot(N,N)

        #S1> find P
        NDRDir = dot(N,direction)
        if(abs(NDRDir)<epsilon):
            return None

        D = dot(N,self.vert0)

        #compute t
        t = (dot(N,origin)+D)/NDRDir
        if(t<0):
            return None

        #Intersection point
        P = sum(origin,mul(direction,t))

        edge0 = sub(self.vert1,self.vert0)
        vp0 = sub(P,self.vert0)
        C = cross(edge0,vp0)
        if(dot(N,C)<0):
            return None

        edge1 = sub(self.vert2,self.vert1)
        vp1 = sub(P,self.vert1)
        C = cross(edge1,vp1)
        u = dot(N,C)

        if(u<0):
            return None

        edge2 = sub(self.vert0,self.vert2)
        vp2 = sub(P,self.vert2)
        C = cross(edge2,vp2)
        v = dot(N,C)
        if(v<0):
            return None

        u = u / denom
        v = v / denom

        return Intersect(
            distance = D,
            point = P,
            normal = N,
            texture = (u,v)
        )
