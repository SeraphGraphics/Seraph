import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from Seraph.Utilities.Colors import *


class Plot2D:
    def __init__(self, X, Y, color, width=2, alpha=1):
        self.X = X
        self.Y = Y
        self.color = color
        self.width = width
        self.alpha = alpha

    def draw(self, scale_x, scale_y):
        glLineWidth(self.width)
        set_color(self.color, self.alpha)
        glBegin(GL_LINE_STRIP)
        for x, y in zip(self.X, self.Y):
            glVertex3f(x * scale_x, y * scale_y, 3)
        glEnd()


class PlotAnimation:
    def __init__(self, graph, plot):
        self.graph = graph
        self.plot = plot
