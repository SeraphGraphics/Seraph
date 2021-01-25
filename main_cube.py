from random import randint
import numpy as np
from Seraph.Core.KeyEvents import *
from Seraph.Core.Renderer import *
from Seraph.Graph3D.Coordinates import *
from Seraph.Graph3D.SimpleObjects import SimpleCube, SolidSphere
from Seraph.Utilities.Text import *
from Seraph.Linear.Linear_Objects import *

win = Window(600, 600, "name")
renderer = Renderer(win)


class Sphere:
    spheres = []

    def __init__(self, id, renderer, m=1):
        self.id = id
        self.sphere = SolidSphere(30, 0, 0, 5, color=color.RED)
        self.m = m
        self.x = randint(-49, 49)
        self.y = randint(-49, 49)
        self.z = randint(-49, 49)
        self.xstep = randint(1, 5)
        self.ystep = randint(1, 5)
        self.zstep = randint(1, 5)
        self.renderer = renderer
        self.spheres.append(self)

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
        self.checkCollision()
        self.x += self.xstep
        self.y += self.ystep
        self.z += self.zstep

        self.sphere.x = self.x
        self.sphere.y = self.y
        self.sphere.z = self.z
        self.renderer.loopAnimation(self.anim, 33)

    def checkCollision(self):
        for sphere in self.spheres:
            if sphere.id != self.id:
                distance = np.sqrt(
                    np.power((self.x - sphere.x), 2) + np.power((self.y - sphere.y), 2) + np.power((self.z - sphere.z),
                                                                                                   2))
                if distance < self.sphere.size + sphere.sphere.size:


    def startAnimation(self):
        renderer.startAnimation(self.anim)

    @property
    def impulse(self):
        impulse_x = self.m * self.xstep
        impulse_y = self.m * self.ystep
        impulse_z = self.m * self.zstep

        return Vector(impulse_x, impulse_y, impulse_z)

    @property
    def kinetic_energy(self):
        energy = abs(self.impulse) / (2 * self.m)
        return energy


# graph = CartSys3D(renderer, x_offset=1, y_offset=1, color_grid=color.BLACK, color_bg=color.WHITE)
graph = CartSys3D(renderer, x_offset=1, y_offset=1, color_grid=color.WHITE, color_bg=color.BLACK)
spheres = [Sphere(i, renderer) for i in range(10)]
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
