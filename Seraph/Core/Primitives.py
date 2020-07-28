from OpenGL.GL import *
from OpenGL.GLUT import *
from Seraph.Utilities.Colors import *

class Primitives:

    def __init__(self, x, y, z, color, alpha=1):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.alpha = alpha

class Point(Primitives):

    def __init__(self, x, y, z, color, is_drawing = True):
        super().__init__(x, y, z, color)
        if is_drawing:
            self.draw()

    def draw(self):
        set_color(self.color, self.alpha)
        glVertex3f(self.x, self.y, self.z)

class Line:

    def __init__(self, points, width = 1):
        self.points = points
        self.width = width
    def draw(self):
        glLineWidth(self.width)
        glBegin(GL_LINE_STRIP)
        for point in self.points:
            point.draw()
        glEnd()

