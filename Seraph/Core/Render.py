from OpenGL.GL import *
from OpenGL.GLUT import *

class Renderer:
    def __init__(self, width, heigth, name, nRange, scale_x=1, scale_y=1):
        self.width = width
        self.heigth = heigth
        self.name = name
        self.nRange = nRange
        self.RenderInit()
        self.size_updated = False
        self.proportion = heigth / width
        self.stepx_px = width / (2 * (nRange * self.proportion))
        self.stepy_px = heigth / (2 * (nRange * self.proportion))
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.dx = 0
        self.dy = 0

    def UpdateOrtho(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        if self.width <= self.heigth:
            print(-self.nRange + (self.dx * self.scale_x ), self.nRange + (self.dx * self.scale_x ),
                    -self.nRange * self.proportion + (self.dy * self.scale_y), self.nRange * self.proportion + (self.dy * self.scale_y))
            glOrtho(-self.nRange + (self.dx * self.scale_x), self.nRange + (self.dx * self.scale_x),
                    -self.nRange * self.proportion + (self.dy * self.scale_y), self.nRange * self.proportion + (self.dy * self.scale_y),
                    -self.nRange, self.nRange)
        else:
            glOrtho(-self.nRange * self.proportion + (self.dx * self.scale_x), self.nRange * self.proportion + (self.dx * self.scale_x),
                    -self.nRange + (self.dy * self.scale_y), self.nRange + (self.dy * self.scale_y),
                    -self.nRange, self.nRange)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glutPostRedisplay()

    def ChangeSize(self, width, heigth):
        self.size_updated = True
        self.width = width
        self.heigth = heigth
        if heigth == 0:
            heigth = 1
        glViewport(0, 0, width, heigth)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        if width <= heigth:
            self.proportion = heigth / width
            self.stepy_px = self.stepx_px = width / (2 * self.nRange)
        else:
            self.proportion = width / heigth
            self.stepx_px = self.stepy_px = heigth / (2 * self.nRange)

        self.UpdateOrtho()


        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def NormalKeyEvent(self, key, x, y):
        print("KEY: ", key)

    def SpecialKeyEvent(self, key, x, y):
        if key == GLUT_KEY_RIGHT:
            if glutGetModifiers() == GLUT_ACTIVE_CTRL:
                self.scale_x += 1
            else:
                self.dx += 1
        if key == GLUT_KEY_LEFT:
            if glutGetModifiers() == GLUT_ACTIVE_CTRL and self.scale_x != 1:
                self.scale_x -= 1
            else:
                self.dx -= 1
        if key == GLUT_KEY_UP:
            if glutGetModifiers() == GLUT_ACTIVE_CTRL:
                self.scale_y += 1
            else:
                self.dy += 1
        if key == GLUT_KEY_DOWN:
            if glutGetModifiers() == GLUT_ACTIVE_CTRL and self.scale_y != 1:
                self.scale_y -= 1
            else:
                self.dy -= 1

        self.UpdateOrtho()

    def MouseEvent(self, key, state, x, y):
        print("MOUSE KEY: ", key)

    def MouseWheelEvent(self, wheel, direction, x, y):
        if direction == 1 and glutGetModifiers() == GLUT_ACTIVE_CTRL:
            self.scale_x += 1
            self.scale_y += 1
        if direction == -1 and glutGetModifiers() == GLUT_ACTIVE_CTRL and self.scale_x != 1 and self.scale_y != 1:
            self.scale_x -= 1
            self.scale_y -= 1
        self.UpdateOrtho()

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
        glutKeyboardFunc(self.NormalKeyEvent)
        glutSpecialFunc(self.SpecialKeyEvent)
        glutMouseFunc(self.MouseEvent)
        glutMouseWheelFunc(self.MouseWheelEvent)
        glutSetKeyRepeat(GLUT_KEY_REPEAT_ON)
        self.SetupRC()

    def Render(self):

        glutMainLoop()
