from Funciones.math import *
from Funciones.intersect import *
from Funciones.plane import *
from Funciones.cube_utils import *

#https://inmensia.com/articulos/raytracing/planotrianguloycubo.html
#https://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-box-intersection
class Cube(object):
  def __init__(self, position, sizebox, material):
    self.position = position
    self.sizebox = sizebox
    self.material = material
    self.normals = get_normals()
    self.planos = get_planes(self.position,self.sizebox,self.normals,material)


  def ray_intersect(self, origin, direction):
    Boundmin = get_Boundmin(self.position,self.sizebox)
    Boundmax = get_max_bounds(self.position,self.sizebox)

    td = float('inf')
    hit = None

    for plane in self.planos:
      planeHit = plane.ray_intersect(origin, direction)

      if planeHit is not None:
        #Check corners, where hits
        if planeHit.point[0] >= Boundmin[0] and planeHit.point[0] <= Boundmax[0]:
          if planeHit.point[1] >= Boundmin[1] and planeHit.point[1] <= Boundmax[1]:
            if planeHit.point[2] >= Boundmin[2] and planeHit.point[2] <= Boundmax[2]:
              if planeHit.distance < td:
                td = planeHit.distance
                hit = planeHit
                t_cube = get_texture(plane,planeHit,Boundmin,Boundmax)


    if hit is not None:
        return Intersect(
        distance = hit.distance,
        point = hit.point,
        normal = hit.normal,
        texture=t_cube,)
    else:
      return None



