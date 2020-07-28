import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from Seraph.Utilities.Colors import *
from Seraph.Core.Primitives import *

class Grid:

    def __init__(self, x_range, y_range, x_offset, y_offset, width, color, alpha=0.3):
        self.x_range = x_range
        self.y_range = y_range
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.width = width
        self.color = color
        self.alpha = alpha

    def DrawGrid(self):


        glLineWidth(self.width)
        set_color(self.color, self.alpha)


        for x in np.arange(-self.x_range, self.x_range, self.x_offset):
            points = []
            points.append(Point(x, self.y_range, 0, self.color))
            points.append(Point(x, -self.y_range, 0, self.color))
            line = Line(points)
            line.draw()


        for y in np.arange(-self.y_range, self.y_range, self.y_offset):
            points = []
            points.append(Point(self.x_range, y, 0, self.color))
            points.append(Point(-self.x_range, y, 0, self.color))
            line = Line(points)
            line.draw()

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
        
        points = []
        points.append(Point(0, self.y_lim, 0, self.color_x))
        points.append(Point(0, -self.y_lim, 0, self.color_x))
        line = Line(points)
        line.draw()
        points = []
        points.append(Point(self.x_lim, 0, 0, self.color_y))
        points.append(Point(-self.x_lim, 0, 0, self.color_y))
        line = Line(points)
        line.draw()