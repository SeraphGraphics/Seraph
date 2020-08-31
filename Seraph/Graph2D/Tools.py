import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from Seraph.Utilities.Colors import *
from Seraph.Core.Primitives import *
from Seraph.Utilities.Text import *
from Seraph.Utilities.Variables import *

class Grid:
    def __init__(self, range, line_width, color, alpha=0.3):
        self.range = range
        self.offset = Structure2D(1, 1)
        self.line_width = line_width
        self.color = color
        self.alpha = alpha

    def DrawGrid(self, renderer, view):
        set_color(self.color)

        if self.offset.x * renderer.scale_x * renderer.step_px < 15:
            self.offset.x *= 2
        elif self.offset.x * renderer.scale_x * renderer.step_px > 30:
            self.offset.x /= 2
        if self.offset.y * renderer.scale_y * renderer.step_px < 15:
            self.offset.y *= 2
        elif self.offset.y * renderer.scale_y * renderer.step_px > 30:
            self.offset.y /= 2

        for x in np.concatenate((np.arange(0, view.left, -self.offset.x), np.arange(self.offset.x, view.right, self.offset.x))):
            points = []
            points.append(Point(x * renderer.scale_x, view.up * renderer.scale_y, 0, self.color, self.alpha))
            points.append(Point(x * renderer.scale_x, view.bottom * renderer.scale_y, 0, self.color, self.alpha))
            line = Line(points, color=self.color)
            line.draw()

        for y in np.concatenate((np.arange(0, view.bottom, -self.offset.y), np.arange(self.offset.y, view.up, self.offset.y))):
            points = []
            points.append(Point(view.left * renderer.scale_x, y * renderer.scale_y, 0, self.color, self.alpha))
            points.append(Point(view.right * renderer.scale_x, y * renderer.scale_y, 0, self.color, self.alpha))
            line = Line(points, color=self.color)
            line.draw()



class Axes:
    def __init__(self, grid, range, width, color, alpha=0.4):
        self.grid = grid
        self.range = range
        self.width = width
        self.color = color
        self.alpha = alpha
        self.num_offset = Structure2D(1, 1)
        self.num_size_px = 12
        self.num_size = 0
        self.separator_size_px = 8
        self.separator_size = 1


    def DrawAxes(self, renderer, view):

        points = []
        points.append(Point(0, view.up * renderer.scale_y, 0, self.color, alpha=self.alpha))
        points.append(Point(0, view.bottom * renderer.scale_y, 0, self.color, alpha=self.alpha))
        line = Line(points, width=self.width)
        line.draw()
        points = []
        points.append(Point(view.left * renderer.scale_x, 0, 0, self.color, alpha=self.alpha))
        points.append(Point(view.right * renderer.scale_x, 0, 0, self.color, alpha=self.alpha))
        line = Line(points, width=self.width)
        line.draw()

        self.num_size = self.num_size_px / renderer.step_px
        self.separator_size = self.separator_size_px / renderer.step_px

        num_len = len(str(int(view.left))) + numDot(self.num_offset.x)
        num_width = GetFontWidth(Fonts.GLUT_STROKE_ROMAN) * self.num_size / GetFontHeight(Fonts.GLUT_STROKE_ROMAN)
        offset_width = self.num_offset.x * renderer.scale_x
        offset_hight = self.num_offset.y * renderer.scale_y

        print(">>>>-<<<<<")
        print(self.num_size, offset_hight)

        if offset_width <= (num_len + 2) * num_width:

            tmp = (num_len + 2) * num_width / renderer.scale_x
            if tmp >= 1 and int(tmp) % 2 == 0:
                self.num_offset.x = int(tmp)
            elif tmp >= 1 and int(tmp) % 2 != 0:
                self.num_offset.x = int(tmp) + 1
            else:
                if offset_width * 2 > (num_len + 3) * num_width:
                    self.num_offset.x /= 0.5

        if offset_width > (num_len + 4) * num_width:

            tmp = (num_len + 4) * num_width / renderer.scale_x
            if int(tmp) >= 1 and int(tmp) % 2 == 0 or int(tmp) == 1:
                self.num_offset.x = int(tmp)
            elif int(tmp) >= 1 and int(tmp) % 2 != 0:
                self.num_offset.x = int(tmp) + 1
            else:
                if offset_width / 2 > (num_len + 3) * num_width:
                    self.num_offset.x *= 0.5

        if offset_hight <= 5 * self.num_size:
            tmp = 1.5 * self.num_size / renderer.scale_y
            if tmp >= 1 and int(tmp) % 2 == 0:
                self.num_offset.y = int(tmp)
            elif tmp >= 1 and int(tmp) % 2 != 0:
                self.num_offset.y = int(tmp) + 1
            else:
                if offset_hight * 2 > 4 * self.num_size / renderer.scale_y:
                    self.num_offset.y /= 0.5
        if offset_hight > 7 * self.num_size:
            tmp = 2 * self.num_size / renderer.scale_y
            print(tmp)
            if tmp >= 1 and int(tmp) % 2 == 0 or int(tmp) == 1:
                self.num_offset.y = int(tmp)
            elif tmp >= 1 and int(tmp) % 2 != 0:
                self.num_offset.y = int(tmp) + 1
            else:
                if offset_hight / 2 > 4 * self.num_size / renderer.scale_y:
                    self.num_offset.y *= 0.5


        for x in np.concatenate((np.arange(-self.num_offset.x, view.left, -self.num_offset.x), np.arange(self.num_offset.x, view.right, self.num_offset.x))):
            num_digits = numDot(x)
            number = "{:.{num_digits}f}".format(x, num_digits=num_digits).encode('utf-8')
            putText(x * renderer.scale_x + 5 / renderer.step_px, -num_width - 8 / renderer.step_px, -3, Fonts.GLUT_STROKE_ROMAN,
                    self.num_size, number, color.RED)
            points = []
            points.append(Point(x * renderer.scale_x, self.separator_size, 0, self.color, alpha=self.alpha))
            points.append(Point(x * renderer.scale_x, -self.separator_size, 0, self.color, alpha=self.alpha))
            line = Line(points, width=self.width)
            line.draw()

        for y in np.concatenate((np.arange(0, view.bottom, -self.num_offset.y), np.arange(self.num_offset.y, view.up, self.num_offset.y))):
            num_digits = numDot(y)
            number = "{:.{num_digits}f}".format(y, num_digits=num_digits).encode('utf-8')
            putText(5 / renderer.step_px, y * renderer.scale_y + 5 / renderer.step_px, -3, Fonts.GLUT_STROKE_ROMAN,
                    self.num_size, number, color.RED)
            points = []
            points.append(Point(self.separator_size, y * renderer.scale_y, 0, self.color, alpha=self.alpha))
            points.append(Point(-self.separator_size, y * renderer.scale_y, 0, self.color, alpha=self.alpha))
            line = Line(points, width=self.width)
            line.draw()