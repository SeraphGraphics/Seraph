from OpenGL.GL import *
from OpenGL.GLUT import *
from Seraph.Graph2D.Tools_old import *
from Seraph.Utilities.Colors import *

class CartSys2D:

    def __init__(self, renderer, x=0, y=0, z=0, x_lim=100, y_lim=100, x_offset=20, y_offset=20,
                 width_grid=1, width_axes=3, color_x=color.BLUE, color_y=color.BLUE,
                 color_grid=color.WHITE, color_bg=color.BLACK):
        self.axes = Axes(x, y, z, x_lim, y_lim, width_axes, color_x, color_y)
        self.grid = Grid(x_lim, y_lim, x_offset, y_offset, width_grid, color_grid, 0.3)
        self.color_bg = color_bg
        self.plots = []
        self.renderer = renderer
        self.view_left = 0
        self.view_rigth = 0
        self.view_up = 0
        self.view_bottom = 0

        self.UpdateViewRange()

    def UpdateViewRange(self):
        if self.renderer.window.width / (2 * self.renderer.step_px * self.renderer.scale_x) < self.grid.x_range:
            self.view_left = self.renderer.window.width / (2 * self.renderer.step_px * self.renderer.scale_x) - \
                             self.renderer.dx
            self.view_rigth = self.renderer.window.width / (2 * self.renderer.step_px * self.renderer.scale_x) + \
                             self.renderer.dx
        if self.renderer.window.heigth / (2 * self.renderer.step_px * self.renderer.scale_y) < self.grid.y_range:
            self.view_bottom = self.renderer.window.heigth / (2 * self.renderer.step_px * self.renderer.scale_y) - \
                               self.renderer.dy
            self.view_up = self.renderer.window.heigth / (2 * self.renderer.step_px * self.renderer.scale_y) + \
                               self.renderer.dy


    def addPlot(self, plot):
        self.plots.append(plot)

    def DrawScene(self):
        glClearColor(*self.color_bg, 1)
        glClear(GL_COLOR_BUFFER_BIT)
        self.grid.DrawGrid(...)
        self.axes.DrawAxes(...)
        for plot in self.plots:
            plot.draw(self.renderer.scale_x, self.renderer.scale_y)
        glutSwapBuffers()

    def Draw(self):
        glutDisplayFunc(self.DrawScene)