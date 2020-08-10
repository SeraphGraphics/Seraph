from OpenGL.GL import *
from OpenGL.GLUT import *

class Window:
    def __init__(self, width, heigth, name):
        self.width = width
        self.heigth = heigth
        self.name = name

class Renderer:
    def __init__(self, window, scale_x=1, scale_y=1, perspective_x=25, perspective_y=25):
        self.window = window
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.perspective_x = perspective_x
        self.perspective_y = perspective_y
        self.step_px = 0
        self.proportion = 0
        self.dx = 0
        self.dy = 0

        self.CheckProportion()
        self.RenderInit()

    def CheckProportion(self):
        if self.window.width <= self.window.heigth:
            self.proportion = self.window.heigth / self.window.width
            self.step_px = self.window.width / self.perspective_x
        else:
            self.proportion = self.window.width / self.window.heigt
            self.step_px = self.window.heigth / self.perspective_y

    def UpdateOrtho(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        if self.window.width <= self.window.heigth:
            glOrtho(-self.perspective_x + (self.dx * self.scale_x),
                    self.perspective_x + (self.dx * self.scale_x),
                    -self.perspective_y * self.proportion + (self.dy * self.scale_y),
                    self.perspective_y * self.proportion + (self.dy * self.scale_y),
                    -1, 1)
        else:
            glOrtho(-self.perspective_x * self.proportion + (self.dx * self.scale_x),
                    self.perspective_x * self.proportion + (self.dx * self.scale_x),
                    -self.perspective_y + (self.dy * self.scale_y),
                    self.perspective_y + (self.dy * self.scale_y),
                    -1, 1)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glutPostRedisplay()


    def ChangeSize(self, width, heigth):
        if heigth == 0:
            heigth = 1
        self.window.width = width
        self.window.heigth = heigth
        self.CheckProportion()
        self.UpdateOrtho()


    def SetupRC(self):
        glClearColor(0.0, 0.0, 0.0, 1)

    def RenderInit(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
        glutInitWindowSize(self.window.width, self.window.heigth)
        glutCreateWindow(self.window.name)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glutReshapeFunc(self.ChangeSize)
        '''glutKeyboardFunc(self.NormalKeyEvent)
        glutSpecialFunc(self.SpecialKeyEvent)
        glutMouseFunc(self.MouseEvent)
        glutMouseWheelFunc(self.MouseWheelEvent)'''
        glutSetKeyRepeat(GLUT_KEY_REPEAT_ON)
        self.SetupRC()

    def Render(self):
        glutMainLoop()