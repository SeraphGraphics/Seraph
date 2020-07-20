from OpenGL.GL import *
from OpenGL.GLUT import *
from Seraph.Utilities.Colors import *
from Seraph.Core.Primitives import *

class Grid:

    def __init__(self, x_range, y_range, x_offset, y_offset, width, color, alpha=1):
        self.x_range = x_range
        self.y_range = y_range
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.width = width
        self.color = color
        self.alpha = alpha

    def DrawGrid(self):

        glLineWidth(self.width)

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

class Axes:

    def __init__(self, x, y, z, x_lim, y_lim, width, color_x, color_y):
        self.x = x
        self.y = y
        self.z = z
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.width = width
        self.color_x = color_x
        self.color_y = color_y

    def DrawAxes(self):
        glLineWidth(self.width)
        glBegin(GL_LINE_STRIP)
        point = Point(0, self.y_lim, 0, self.color_x)
        point = Point(0, -self.y_lim, 0, self.color_x)
        glEnd()
        glBegin(GL_LINE_STRIP)
        point = Point(self.x_lim, 0, 0, self.color_y)
        point = Point(-self.x_lim, 0, 0, self.color_y)
        glEnd()
