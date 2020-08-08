import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from Seraph.Utilities.Colors import *
from Seraph.Core.Primitives import *
from Seraph.Utilities.Text import *

class Grid:

    def __init__(self, x_range, y_range, x_offset, y_offset, width, color, alpha=0.3):
        self.x_range = x_range
        self.y_range = y_range
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.width = width
        self.color = color
        self.alpha = alpha

    def DrawGrid(self, width, heigth, nRange):
        set_color(self.color)
        glLineWidth(self.width)
        glPushMatrix()

        if width <= heigth:
            proportion = heigth/width
        else:
            proportion = width/heigth

        stepx_px = width / (2 * (nRange * proportion / self.x_offset))
        stepy_px = heigth / (2 * (nRange * proportion / self.y_offset))
        print(stepx_px, stepy_px)

        if stepx_px < 10:
            self.x_offset *= 2
        elif stepx_px > 50:
            self.x_offset /= 2
        if stepy_px < 10:
            self.y_offset *= 2
        elif stepy_px > 50:
            self.y_offset /= 2

        for x in np.arange(-self.x_range, self.x_range, self.x_offset):
            points = []
            num = "{:.0f}".format(x).encode('utf-8')
            putText(x,0,Fonts.GLUT_STROKE_ROMAN, 1, num, rgb_picker(155, 255, 209))
            points.append(Point(x, self.y_range, 0, self.color, alpha=self.alpha))
            points.append(Point(x, -self.y_range, 0, self.color, alpha=self.alpha))
            line = Line(points)
            line.draw()

        for y in np.arange(-self.y_range, self.y_range, self.y_offset):
            points = []
            num = "{:.0f}".format(y).encode('utf-8')
            putText(0,y,Fonts.GLUT_STROKE_ROMAN, 1, num, rgb_picker(155, 255, 209))
            points.append(Point(self.x_range, y, 0, self.color, alpha=self.alpha))
            points.append(Point(-self.x_range, y, 0, self.color, alpha=self.alpha))
            line = Line(points)
            line.draw()
        glPopMatrix()


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



   # def DrawUpdate(self, ):
