from Seraph.Utilities.Colors import *


class Plot3D:
    def __init__(self, X, Y, Z, color, width=2, alpha=1, type=GL_POINTS):
        self.X = X
        self.Y = Y
        self.Z = Z
        self.color = color
        self.width = width
        self.alpha = alpha
        self.type = type

    def draw(self):
        glLineWidth(self.width)
        glPointSize(4)
        set_color(self.color, self.alpha)
        glBegin(self.type)
        for x, y, z in zip(self.X, self.Y, self.Z):
            glVertex3f(x, y, z)
        glEnd()


class Plot3DbyPoints:
    def __init__(self, points, color, width=2, alpha=1, type=GL_POINTS):
        self.points = points
        self.color = color
        self.width = width
        self.alpha = alpha
        self.type = type

    def draw(self):
        glLineWidth(self.width)
        glPointSize(10)
        glBegin(self.type)
        for point in self.points:
            set_color(point.color, self.alpha)
            glVertex3f(point.x, point.y, point.z)
        glEnd()
