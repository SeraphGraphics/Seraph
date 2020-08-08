import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from Seraph.Utilities.Colors import *


class Plot2D:
    def __init__(self, X, Y, color, alpha=1):
        self.X = X
        self.Y = Y
        self.color = color
        self.alpha = alpha

    def draw(self, ):
        set_color(self.color, self.alpha)
        glBegin(GL_LINE_STRIP)
        for x, y in zip(self.X, self.Y):
            glVertex(x, y, 0)
        glEnd()
