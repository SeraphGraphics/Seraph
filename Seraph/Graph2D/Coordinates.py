from OpenGL.GL import *
from OpenGL.GLUT import *
from Seraph.Graph2D.Tools import *
from Seraph.Utilities.Colors import *

class CartSys2D:

    def __init__(self, x=0, y=0, z=0, x_lim=100, y_lim=100, x_offset=20, y_offset=20,
                 width_grid=1, width_axes=5, color_x=color.BLUE, color_y=color.BLUE,
                 color_grid=color.WHITE, color_bg=color.BLACK):
        self.axes = Axes(x, y, z, x_lim, y_lim, width_axes, color_x, color_y)
        self.grid = Grid(x_lim, y_lim, x_offset, y_offset, width_grid,color_grid,0.3)
        self.color_bg = color_bg

    def Draw(self):
        glClearColor(*self.color_bg, 1)
        glClear(GL_COLOR_BUFFER_BIT)
        self.grid.DrawGrid()
        self.axes.DrawAxes()