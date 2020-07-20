from OpenGL.GL import *
from OpenGL.GLUT import *
from Seraph.Utilities.Colors import *
from Seraph.Core.Primitives import *

class Grid:

    def __init__(self, x_range, y_range, x_offset, y_offset, color, alpha=1):
        self.x_range = x_range
        self.y_range = y_range
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.color = color
        self.alpha = alpha

    def DrawGrid(self):
        set_color(self.color, self.alpha)

        for x in range(-self.x_range, self.x_range, self.x_offset):
            glBegin(GL_LINE_STRIP)
            point = Point(x, self.y_range, 0, self.color)
            point = Point(x, -self.y_range, 0, self.color)
            glEnd()


        for y in range(-self.y_range, self.y_range, self.y_offset):
            glBegin(GL_LINE_STRIP)
            point = Point(self.x_range, y, 0, self.color)
            point = Point(-self.x_range, y, 0, self.color)
            glEnd()




