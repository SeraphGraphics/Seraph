from OpenGL.GL import *
from OpenGL.GLUT import *

class Renderer:
    def __init__(self, width, heigth, name, nRange):
        self.width = width
        self.heigth = heigth
        self.name = name
        self.nRange = nRange
        self.RenderInit()
        self.size_updated = False
        self.proportion = heigth / width
        self.stepx_px = width / (2 * (nRange * self.proportion))
        self.stepy_px = heigth / (2 * (nRange * self.proportion))

    def ChangeSize(self, width, heigth):
        self.size_updated = True
        self.width = width
        self.heigth = heigth
        print("WINSIZE: ", width, heigth)
        if heigth == 0:
            heigth = 1
        glViewport(0, 0, width, heigth)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        if width <= heigth:
            self.proportion = heigth / width
            self.stepy_px = self.stepx_px = width / (2 * self.nRange)
            glOrtho(-self.nRange, self.nRange, -self.nRange * self.proportion, self.nRange * self.proportion, -self.nRange, self.nRange)
        else:
            self.proportion = width / heigth
            self.stepx_px = self.stepy_px = heigth / (2 * self.nRange)
            glOrtho(-self.nRange * self.proportion, self.nRange * self.proportion, -self.nRange, self.nRange, -self.nRange, self.nRange)


        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def SetupRC(self):
        glClearColor(0.0, 0.0, 0.0, 1)

    def RenderInit(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
        glutInitWindowSize(self.width, self.heigth)
        glutCreateWindow(self.name)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glutReshapeFunc(self.ChangeSize)
        self.SetupRC()

    def Render(self):

        glutMainLoop()
