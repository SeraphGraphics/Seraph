import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from Seraph.Utilities.Colors import *
from Seraph.Core.Primitives import *
from Seraph.Utilities.Text import *
from Seraph.Utilities.Variables import *

class Grid:
    def __init__(self, range, line_width, color, alpha=0.3):
        self.range = Structure2D(*range)
        self.offset = Structure2D(1, 1)
        self.line_width = line_width
        self.color = color
        self.alpha = alpha

    def DrawGrid(self, renderer, view_left, view_rigth, view_bottom, view_up):
        set_color(self.color)

        for x in np.concatenate((np.arange(0, -view_left, -self.offset.x), np.arange(0, view_rigth, self.offset.x))):
            points = []
            points.append(Point(x * renderer.scale_x, view_up * renderer.scale_y, 0, self.color, self.alpha))
            points.append(Point(x * renderer.scale_x, view_bottom * renderer.scale_y, 0, self.color, self.alpha))
            line = Line(points)
            line.draw()

        for y in np.concatenate((np.arange(0, -view_left, -self.offset.x), np.arange(0, view_rigth, self.offset.x))):
            points = []
            points.append(Point(x * renderer.scale_x, view_up * renderer.scale_y, 0, self.color, self.alpha))
            points.append(Point(x * renderer.scale_x, view_bottom * renderer.scale_y, 0, self.color, self.alpha))
            line = Line(points)
            line.draw()

class Axes:
    def __init__(self, grid):
        self.grid = grid

    def DrawAxes(self):