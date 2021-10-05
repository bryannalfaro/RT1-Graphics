from tracer import Raytracer

r = Raytracer()
r.glCreateWindow(1000,1000)
r.glClear()
r.render()
r.glFinish("./salidas/output.bmp")