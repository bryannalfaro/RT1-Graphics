from Funciones.math import *
from Funciones.utilities import *
from Funciones.characters import *
from Funciones.material import *
from math import pi,tan

class Raytracer(object):
    def __init__(self):
        self.default_color = color(0,0,139)
        self.cl_color = BLACK
        self.background_color = BLACK
        self.light = None
        self.scene  = []

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
        material, intersect = self.scene_intersect(origin,direction)

        if material is not None:

            light_dir = norm(sub(self.light.position,intersect.point))
            light_distance = length(sub(self.light.position,intersect.point))

            offset_normal = mul(intersect.normal,0.1)
            shadow_orig = sum(intersect.point,offset_normal) if dot(light_dir,intersect.normal)>0 else sub(intersect.point,offset_normal)
            shadow_material, shadow_intersect = self.scene_intersect(shadow_orig,light_dir)


            if shadow_material is None or length(sub(shadow_intersect.point,shadow_orig)) > light_distance:
                shadow_intensity = 0
            else:
                shadow_intensity = 0.9

            diffuse_intensity = self.light.intensity * max(0,dot(light_dir,intersect.normal)) * (1-shadow_intensity)

            if shadow_intensity > 0:
                specular_intensity = 0
            else:
                reflection = reflect(light_dir,intersect.normal)
                specular_intensity = self.light.intensity*(max(0,dot(reflection,direction))**material.spec)

            diffuse = material.diffuse*diffuse_intensity*material.albedo[0]
            specular = self.light.color * specular_intensity * material.albedo[1]
            c = diffuse + specular
            return c
        else:
            return self.background_color

    def scene_intersect(self,origin,direction):
        zbuffer = float('inf')
        material = None
        intersect = None
        for obj in self.scene:
            r_intersect = obj.ray_intersect(origin,direction)
            if r_intersect is not None:
                if r_intersect.distance  < zbuffer:
                    zbuffer = r_intersect.distance
                    material = obj.material
                    intersect = r_intersect
        return material,intersect

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
