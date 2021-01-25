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

    def __init__(self, x, y, z, color=color.RED, alpha=1, is_drawing=False):
        super().__init__(x, y, z, color, alpha)
        if is_drawing:
            self.draw()

    def draw(self):
        set_color(self.color, self.alpha)
        glVertex3f(self.x, self.y, self.z)


class Line:

    def __init__(self, points, color=color.BLUE, width=1, alpha=0.2):
        self.points = points
        self.color = color
        self.width = width
        self.alpha = alpha

    def draw(self):
        glLineWidth(self.width)
        glBegin(GL_LINE_STRIP)
        for point in self.points:
            point.color = self.color
            point.alpha = self.alpha
            point.draw()
        glEnd()
