class Intersect(object):
    def __init__(self,distance,point,normal):
        self.distance = distance
        self.point = point
        self.normal = normal

class Light(object):
    def __init__(self,position,intensity):
        self.position = position
        self.intensity = intensity