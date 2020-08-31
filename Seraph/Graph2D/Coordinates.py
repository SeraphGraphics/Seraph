
from Seraph.Graph2D.Tools import *
from Seraph.Utilities.Colors import *
from Seraph.Utilities.Variables import *

class CartSys2D:

    def __init__(self, renderer, x=0, y=0, z=0, x_lim=100, y_lim=100, x_offset=20, y_offset=20,
                 width_grid=1, width_axes=3, color_x=color.BLUE, color_y=color.BLUE,
                 color_grid=color.WHITE, color_bg=color.BLACK):
        self.grid = Grid(Structure2D(x_lim, y_lim), width_grid, color_grid, 0.3)
        self.axes = Axes(self.grid, Structure2D(x_lim, y_lim), width_axes, color_x)
        self.color_bg = color_bg
        self.plots = []
        self.renderer = renderer

        self.view = ViewContainer(0, 0, 0, 0)

        self.UpdateViewRange()

    def UpdateViewRange(self):
        #if self.renderer.window.width / (2 * self.renderer.step_px * self.renderer.scale_x) < self.grid.range.x:
        self.view.left = - self.renderer.window.width / (2 * self.renderer.step_px * self.renderer.scale_x) + \
                         self.renderer.dx
        self.view.right = self.renderer.window.width / (2 * self.renderer.step_px * self.renderer.scale_x) + \
                         self.renderer.dx
        #if self.renderer.window.height / (2 * self.renderer.step_px * self.renderer.scale_y) < self.grid.range.y:
        self.view.bottom = - self.renderer.window.height / (2 * self.renderer.step_px * self.renderer.scale_y) + \
                           self.renderer.dy
        self.view.up = self.renderer.window.height / (2 * self.renderer.step_px * self.renderer.scale_y) + \
                           self.renderer.dy
        #print(self.view.left, self.view.right, self.view.up, self.view.bottom)


    def addPlot(self, plot):
        self.plots.append(plot)

    def DrawScene(self):
        self.UpdateViewRange()
        glClearColor(*self.color_bg, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.grid.DrawGrid(self.renderer, self.view)

        self.axes.DrawAxes(self.renderer, self.view)
        for plot in self.plots:
            plot.draw(self.renderer.scale_x, self.renderer.scale_y)
        glutSwapBuffers()

    def Draw(self):
        glutDisplayFunc(self.DrawScene)
        self.renderer.Render()