from OpenGL.GL import *
from OpenGL.GLUT import *
from Seraph.Graph2D.Tools import *
from Seraph.Utilities.Colors import *

class CartSys2D:

    def __init__(self, renderer, x=0, y=0, z=0, x_lim=100, y_lim=100, x_offset=20, y_offset=20,
                 width_grid=1, width_axes=3, color_x=color.BLUE, color_y=color.BLUE,
                 color_grid=color.WHITE, color_bg=color.BLACK):
        self.axes = Axes(x, y, z, x_lim, y_lim, width_axes, color_x, color_y)
        self.grid = Grid(x_lim, y_lim, x_offset, y_offset, width_grid,color_grid,0.3)
        self.color_bg = color_bg
        self.plots = []
        self.renderer = renderer

    def addPlot(self, plot):
        self.plots.append(plot)

    def DrawScene(self):
        if self.renderer.size_updated:
            if self.renderer.width <= self.renderer.heigth:
                proportion = self.renderer.heigth / self.renderer.width
            else:
                proportion = self.renderer.width / self.renderer.heigth
            self.renderer.size_updated = False

        glClearColor(*self.color_bg, 1)
        glClear(GL_COLOR_BUFFER_BIT)
        self.grid.DrawGrid(self.renderer.stepx_px, self.renderer.stepy_px)
        self.axes.DrawAxes(self.renderer.stepx_px, self.renderer.stepy_px)

        for plot in self.plots:
            plot.draw()
        glutSwapBuffers()

    def Draw(self):
        glutDisplayFunc(self.DrawScene)
