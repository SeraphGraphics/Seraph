from OpenGL.GL import *
from OpenGL.GLUT import *
from Seraph.Graph2D.Tools import *
from Seraph.Utilities.Colors import *
from Seraph.Graph2D.Coordinates import *

def RenderScene():
    glClear(GL_COLOR_BUFFER_BIT)

    graph1 = CartSys2D()
    graph1.Draw()
    #grid = Grid(100, 100, 5, 5, 1, WHITE, 0.4)
    #grid.DrawGrid()
    #axes = Axes(0, 0, 0, 100, 100, 5, GREEN, RED)
    #axes.DrawAxes()
    glFlush()

def SetupRC():
    glClearColor(0, 0, 0, 1)

def ChangeSize(w, h):
    print(w, h)
    if (h == 0):
        h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    aspectRatio = w / h
    if (w <= h):
        glOrtho(-100, 100, -100/aspectRatio, 100/aspectRatio, 1, -1)
    else:
        glOrtho(-100, 100 * aspectRatio, -100, 100, 1, -1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("GLRect")
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glutDisplayFunc(RenderScene)
    glutReshapeFunc(ChangeSize)
    SetupRC()

    glutMainLoop()
