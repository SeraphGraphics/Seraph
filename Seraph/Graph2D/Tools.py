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

    def DrawGrid(self, stepx_px, stepy_px):
        set_color(self.color)
        glLineWidth(self.width)
        glPushMatrix()
        stepx_px *= self.x_offset
        stepy_px *= self.y_offset

        print(stepx_px, stepy_px)

        if stepx_px < 15:
            self.x_offset *= 2
        elif stepx_px > 30 and (stepx_px * self.x_offset / 2) > 10:
            self.x_offset /= 2
        if stepy_px < 15:
            self.y_offset *= 2
        elif stepy_px > 30 and (stepy_px * self.y_offset / 2) > 10:
            self.y_offset /= 2

        for x in np.arange(-self.x_range, self.x_range, self.x_offset):
            points = []
            points.append(Point(x, self.y_range, 0, self.color, alpha=self.alpha))
            points.append(Point(x, -self.y_range, 0, self.color, alpha=self.alpha))
            line = Line(points)
            line.draw()

        for y in np.arange(-self.y_range, self.y_range, self.y_offset):
            points = []
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
        self.num_offset_x = 1
        self.num_offset_y = 1
        self.size = 1
        self.size_px = 15
        self.stroke_size = 1
        self.stroke_size_px = self.size_px / 2

    def DrawAxes(self, stepx_px, stepy_px):
        points = []
        points.append(Point(0, self.y_lim, 0, self.color_x))
        points.append(Point(0, -self.y_lim, 0, self.color_x))
        line = Line(points, self.width)
        line.draw()
        points = []
        points.append(Point(self.x_lim, 0, 0, self.color_y))
        points.append(Point(-self.x_lim, 0, 0, self.color_y))
        line = Line(points, self.width)
        line.draw()


        self.size = self.size_px / stepx_px
        self.stroke_size = self.stroke_size_px / stepx_px

        while self.num_offset_x <= 4 * glutStrokeWidth(Fonts.GLUT_STROKE_ROMAN, ord('-')) * self.size/glutStrokeHeight(Fonts.GLUT_STROKE_ROMAN):
            self.num_offset_x += 1
        while self.num_offset_x >= 6 * glutStrokeWidth(Fonts.GLUT_STROKE_ROMAN, ord('-')) * self.size/glutStrokeHeight(Fonts.GLUT_STROKE_ROMAN):
            self.num_offset_x -= 1
        while self.num_offset_y <= 1.5 * self.size:
            self.num_offset_y += 1
        while self.num_offset_y >= 3 * self.size:
            self.num_offset_y -= 1

        for x in np.concatenate((np.arange(0, self.x_lim, self.num_offset_x), np.arange(0, -self.x_lim, -self.num_offset_x))):
            num = "{:.0f}".format(x).encode('utf-8')
            putText(x + 5 / stepx_px, 0 + 5 / stepx_px, Fonts.GLUT_STROKE_ROMAN, self.size, num, rgb_picker(155, 255, 209))
            points = []
            points.append(Point(x, self.stroke_size/2, 0, self.color_x))
            points.append(Point(x, -self.stroke_size/2, 0, self.color_x))
            line = Line(points, self.width)
            line.draw()


        for y in np.concatenate((np.arange(0, self.y_lim, self.num_offset_y), np.arange(0, -self.y_lim, -self.num_offset_y))):
            num = "{:.0f}".format(y).encode('utf-8')
            putText(0 + 5 / stepx_px, y + 5 / stepx_px, Fonts.GLUT_STROKE_ROMAN, self.size, num, rgb_picker(155, 255, 209))
            points = []
            points.append(Point(self.stroke_size / 2, y, 0, self.color_y))
            points.append(Point(-self.stroke_size / 2, y, 0, self.color_y))
            line = Line(points, self.width)
            line.draw()

        #убрать различие stepx_px и stepy_px




