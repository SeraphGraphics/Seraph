from Seraph.Graph2D.Tools import *
from Seraph.Utilities.Colors import *
from Seraph.Utilities.Variables import *

class CartSys3D:
    def __init__(self, renderer, x=0, y=0, z=0, x_lim=100, y_lim=100, z_lim = 100, x_offset=20, y_offset=20, width_grid=1,
                 width_axes=3, color_x=color.BLUE, color_y=color.RED, color_z=color.GREEN, color_bg = color.BLACK,
                 color_grid = color.WHITE):
        self.grid = Grid3D(Structure3D(x_lim, y_lim, z_lim), width_grid, color_grid, 0.3)
        self.axes = None
        self.color_bg = color_bg
        self.objects = []
        self.renderer = renderer

        self.view = ViewContainer(0,0,0,0)
    def add(self, object):
        self.objects.append(object)
    def DrawScene(self):
        glClearColor(*self.color_bg, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotate(self.renderer.rotX, 1, 0, 0)
        glRotate(self.renderer.rotY, 0, 1, 0)
        set_color(color.RED, 1)
        self.grid.DrawGrid(self.renderer, self.view)
        # self.axes.DrawAxes(self.renderer, self.view)
        for plot in self.objects:
            plot.draw()
        glPopMatrix()
        self.renderer.UpdateOrtho3D()
        glutSwapBuffers()

    def Render(self):
        self.renderer.Render()
    def Draw(self):
        glutDisplayFunc(self.DrawScene)
        glutPostRedisplay()