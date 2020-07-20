from OpenGL.GL import *
from OpenGL.GLUT import *

class Primitives:

    def __init__(self, x, y, z, color, alpha=1):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.alpha = alpha

class Point(Primitives):

    def __init__(self, x, y, z, color):
        super().__init__(x, y, z, color)
        self.draw()

    def draw(self):

        glVertex3f(self.x, self.y, self.z)