from OpenGL.GL import *
from OpenGL.GLUT import *

class Window:
    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.name = name

class Renderer:
    def __init__(self, window, scale_x=1, scale_y=1, perspective_x=50, perspective_y=50):
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
        if self.window.width <= self.window.height:
            self.proportion = self.window.height / self.window.width
            self.step_px = self.window.width / self.perspective_x
        else:
            self.proportion = self.window.width / self.window.height
            self.step_px = self.window.height / self.perspective_y

    def UpdateOrtho(self):
        glViewport(0, 0, self.window.width, self.window.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        if self.window.width <= self.window.height:
            glOrtho(-self.perspective_x / 2 + (self.dx * self.scale_x),
                    self.perspective_x / 2 + (self.dx * self.scale_x),
                    -self.perspective_y / 2 * self.proportion + (self.dy * self.scale_y),
                    self.perspective_y / 2 * self.proportion + (self.dy * self.scale_y),
                    -5, 5)
        else:
            glOrtho(-self.perspective_x / 2 * self.proportion + (self.dx * self.scale_x),
                    self.perspective_x / 2 * self.proportion + (self.dx * self.scale_x),
                    -self.perspective_y / 2 + (self.dy * self.scale_y),
                    self.perspective_y / 2 + (self.dy * self.scale_y),
                    -5, 5)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glutPostRedisplay()


    def ChangeSize(self, width, height):
        if height == 0:
            height = 1
        self.window.width = width
        self.window.height = height
        self.CheckProportion()
        self.UpdateOrtho()

    def ApplyKeyEvents(self, KeyEvents):
        glutSpecialFunc(KeyEvents)
        glutKeyboardFunc(KeyEvents)



    def SetupRC(self):
        glClearColor(0.0, 0.0, 0.0, 1)

    def RenderInit(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        glutInitWindowSize(self.window.width, self.window.height)
        glutCreateWindow(self.window.name)
        glEnable(GL_BLEND)
        glEnable(GL_DEPTH_TEST)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glutReshapeFunc(self.ChangeSize)
        '''glutKeyboardFunc(self.NormalKeyEvent)
        glutSpecialFunc(self.SpecialKeyEvent)
        glutMouseFunc(self.MouseEvent)
        glutMouseWheelFunc(self.MouseWheelEvent)
        glutSetKeyRepeat(GLUT_KEY_REPEAT_ON)'''
        self.SetupRC()

    def Render(self):
        glutMainLoop()