from Funciones.math import *
from Funciones.characters import *


def ccolor(color):
    return max(0,min(255,int(color)))

class color(object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __getitem__(self,i):
        if i == 0:
            return self.r
        elif i == 1:
            return self.g
        elif i == 2:
            return self.b

    def __repr__(self):
        b= ccolor(self.b)
        g= ccolor(self.g)
        r= ccolor(self.r)
        return 'Y(%s,%s,%s)' % (b,g,r)

    def toBytes(self):
        b= ccolor(self.b)
        g= ccolor(self.g)
        r= ccolor(self.r)
        return bytes([b,g,r])

    def __mul__(self,k):
        r= ccolor(self.r*k)
        g= ccolor(self.g*k)
        b= ccolor(self.b*k)

        return color(r,g,b)

    def __add__(self, b_color):
        r = self.r + b_color.r
        g = self.g + b_color.g
        b = self.b + b_color.b
        return color(r,g,b)

    def tolist(self):
        return color(self.r,self.g,self.b)

BLACK = color(0,0,0)
WHITE = color(255,255,255)

def reflect(I,N):
    return norm(sub(mul(I,-1),mul(N,2*dot(mul(I,-1),N))))

def refract(I,N,refractive_index):
    cosi = -max(-1,min(1,dot(I,N)))
    etai = 1
    etat = refractive_index

    if cosi< 0:
        cosi = -cosi
        etai,etat = etat,etai
        N = mul(N,-1)

    eta = etai/etat
    k = 1-eta**2*(1-cosi**2)
    if k<0:
        return None
    return norm(sum(mul(I,eta),mul(N,eta*cosi-k**0.5)))

def barycentric(A,B,C,P):
        cx,cy,cz = cross(V3(B.x-A.x,C.x-A.x,A.x-P.x),V3(B.y-A.y,C.y-A.y,A.y-P.y))
        if cz ==0:
            return -1,-1,-1

        u = cx/cz
        v = cy/cz
        w = 1-(cx+cy)/cz

        return w,v,u

def bbox(A,B,C):
    xs = [A.x, B.x, C.x,]
    xs.sort()
    ys = [A.y, B.y, C.y,]
    ys.sort()
    return round(xs[0]),round(xs[-1]),round(ys[0]),round(ys[-1])

def write(filename, width, height,framebuffer):
            #bw means binary write
            f = open(filename, 'bw')
            #file header
            f.write(char('B'))
            f.write(char('M'))
            f.write(dword(57*(width*height)))
            f.write(dword(0))
            f.write(dword(54))

            #info header
            f.write(dword(40))
            f.write(dword(width))
            f.write(dword(height))
            f.write(word(1))
            f.write(word(24))
            f.write(dword(0))
            f.write(dword(3*(width*height)))
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))

            #bitmap
            for y in range(height):
                for x in range(width):
                    f.write(framebuffer[y][x].toBytes())

            f.close()