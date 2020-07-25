from OpenGL.GL import *
from OpenGL.GLUT import *
from Seraph.Graph2D.Tools import *
from Seraph.Utilities.Colors import *
from Seraph.Graph2D.Coordinates import *
import numpy as np
from Seraph.Graph2D.Plot import *

def RenderScene():
    glClear(GL_COLOR_BUFFER_BIT)

    graph1 = CartSys2D(x_offset = 1, y_offset = 1)
    graph1.Draw()
    X = np.linspace(-5, 5, 20)
    Y = X**2
    plot = Plot2D(X, Y, color.RED)
    plot.draw()
    #grid = Grid(100, 100, 5, 5, 1, WHITE, 0.4)
    #grid.DrawGrid()
    #axes = Axes(0, 0, 0, 100, 100, 5, GREEN, RED)
    #axes.DrawAxes()
    glFlush()

def SetupRC():
    glEnable(GL_ALPHA_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glClearColor(0, 0, 0, 1)

def ChangeSize(w, h):
    nRange = 20.0
    if h == 0:
        h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if w <= h:
        glOrtho (-nRange, nRange, -nRange*h/w, nRange*h/w, -nRange, nRange)
    else:
        glOrtho (-nRange*w/h, nRange*w/h, -nRange, nRange, -nRange, nRange)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("GLRect")
    glutDisplayFunc(RenderScene)
    glutReshapeFunc(ChangeSize)
    SetupRC()
    glutMainLoop()


