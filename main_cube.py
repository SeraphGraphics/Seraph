from random import randint

from Seraph.Core.KeyEvents import *
from Seraph.Core.Renderer import *
from Seraph.Graph3D.Coordinates import *
from Seraph.Graph3D.SimpleObjects import SimpleCube, SolidSphere
from Seraph.Utilities.Text import *

win = Window(600, 600, "name")
renderer = Renderer(win)


class Sphere:
    def __init__(self, renderer):
        self.sphere = SolidSphere(30, 0, 0, 1, color=color.RED)
        self.x = randint(-50,50)
        self.y = randint(-50,50)
        self.z = randint(-50,50)
        self.xstep = randint(1, 5)
        self.ystep = randint(1, 5)
        self.zstep = randint(1, 5)
        self.renderer = renderer
    def anim(self, value):
        if self.x >= 50:
            self.xstep *= -1
        elif self.x <= -50:
            self.xstep *= -1
        if self.y >= 50:
            self.ystep *= -1
        elif self.y <= -50:
            self.ystep *= -1
        if self.z >= 50:
            self.zstep *= -1
        elif self.z <= -50:
            self.zstep *= -1

        self.x += self.xstep
        self.y += self.ystep
        self.z += self.zstep

        self.sphere.x = self.x
        self.sphere.y = self.y
        self.sphere.z = self.z
        self.renderer.loopAnimation(self.anim, 33)

    def startAnimation(self):
        renderer.startAnimation(sphere.anim)


# graph = CartSys3D(renderer, x_offset=1, y_offset=1, color_grid=color.BLACK, color_bg=color.WHITE)
graph = CartSys3D(renderer, x_offset=1, y_offset=1, color_grid=color.WHITE, color_bg=color.BLACK)
spheres = [Sphere(renderer) for i in range(20)]
cube = SimpleCube(100, alpha=0.1, color=color.WHITE)
for sphere in spheres:
    graph.add(sphere.sphere)
graph.add(cube)
key = KeyEvent2D(graph)
renderer.ApplyKeyEvents(key.GraphKeyEvent2DAdvanced)
for sphere in spheres:
    sphere.startAnimation()
graph.Draw()
graph.Render()
