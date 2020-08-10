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

    def DrawGrid(self, stepx_px, stepy_px, scale_x, scale_y):
        set_color(self.color)
        glLineWidth(self.width)
        glPushMatrix()

        if self.x_offset * scale_x * stepx_px < 15:
            self.x_offset *= 2
        elif self.x_offset * scale_x * stepx_px > 30:
            self.x_offset /= 2
        if self.y_offset * scale_y * stepy_px < 15:
            self.y_offset *= 2
        elif self.y_offset * scale_y * stepy_px > 30:
            self.y_offset /= 2


        for x in np.arange(-self.x_range * scale_x, self.x_range * scale_x, self.x_offset):
            points = []
            points.append(Point(x * scale_x, self.y_range * scale_y, 0, self.color, alpha=self.alpha))
            points.append(Point(x * scale_x, -self.y_range * scale_y, 0, self.color, alpha=self.alpha))
            line = Line(points)
            line.draw()

        for y in np.arange(-self.y_range, self.y_range, self.y_offset):
            points = []
            points.append(Point(self.x_range * scale_x, y * scale_y, 0, self.color, alpha=self.alpha))
            points.append(Point(-self.x_range * scale_x, y * scale_y, 0, self.color, alpha=self.alpha))
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
        self.num_offset_x = 1
        self.num_offset_y = 1
        self.size = 1
        self.size_px = 15
        self.stroke_size = 1
        self.stroke_size_px = self.size_px / 2

    def DrawAxes(self, stepx_px, stepy_px, scale_x, scale_y):
        points = []
        points.append(Point(0, self.y_lim * scale_y, 0, self.color_x))
        points.append(Point(0, -self.y_lim * scale_y, 0, self.color_x))
        line = Line(points, self.width)
        line.draw()
        points = []
        points.append(Point(self.x_lim * scale_x, 0, 0, self.color_y))
        points.append(Point(-self.x_lim * scale_x, 0, 0, self.color_y))
        line = Line(points, self.width)
        line.draw()


        self.size = self.size_px / stepx_px
        self.stroke_size = self.stroke_size_px / stepx_px


        while self.num_offset_x * scale_x <= (len(str(self.num_offset_x)) + 6) * \
                glutStrokeWidth(Fonts.GLUT_STROKE_ROMAN, ord('-')) * self.size/glutStrokeHeight(Fonts.GLUT_STROKE_ROMAN):
            self.num_offset_x = int(self.num_offset_x + 1)
        while self.num_offset_x * scale_x >= (len(str(self.num_offset_x)) + 10) * \
                glutStrokeWidth(Fonts.GLUT_STROKE_ROMAN, ord('-')) * self.size/glutStrokeHeight(Fonts.GLUT_STROKE_ROMAN):
            if self.num_offset_x > 1:
                self.num_offset_x -= 1
            else:
                self.num_offset_x *= 0.5
        while self.num_offset_y * scale_y <= (len(str(self.num_offset_y)) + 3) * self.size:
            self.num_offset_y = int(self.num_offset_y + 1)
        while self.num_offset_y * scale_y >= (len(str(self.num_offset_y)) + 5) * self.size:
            if self.num_offset_y > 1:
                self.num_offset_y -= 1
            else:
                self.num_offset_y *= 0.5

        for x in np.concatenate((np.arange(0, self.x_lim, self.num_offset_x),
                                 np.arange(0, -self.x_lim, -self.num_offset_x))):
            digits = numDot(x)
            num = "{:.{digits}f}".format(x, digits=digits).encode('utf-8')
            putText(x * scale_x + 5 / stepx_px, 0 + 5 / stepx_px,
                    Fonts.GLUT_STROKE_ROMAN, self.size, num, rgb_picker(155, 255, 209))
            points = []
            points.append(Point(x * scale_x, self.stroke_size/2, 0, self.color_x))
            points.append(Point(x * scale_x, -self.stroke_size/2, 0, self.color_x))
            line = Line(points, self.width)
            line.draw()

        for y in np.concatenate((np.arange(0, self.y_lim, self.num_offset_y),
                                 np.arange(0, -self.y_lim, -self.num_offset_y))):
            digits = numDot(y)
            num = "{:.{digits}f}".format(y, digits=digits).encode('utf-8')
            putText(0 + 5 / stepx_px, y * scale_y + 5 / stepx_px,
                    Fonts.GLUT_STROKE_ROMAN, self.size, num, rgb_picker(155, 255, 209))
            points = []
            points.append(Point(self.stroke_size / 2, y * scale_y, 0, self.color_y))
            points.append(Point(-self.stroke_size / 2, y * scale_y, 0, self.color_y))
            line = Line(points, self.width)
            line.draw()

        #убрать различие stepx_px и stepy_px




