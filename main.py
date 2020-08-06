from OpenGL.GL import *
from OpenGL.GLUT import *
from Seraph.Graph2D.Tools import *
from Seraph.Utilities.Colors import *
from Seraph.Graph2D.Coordinates import *
from Seraph.Graph2D.Plot import *
from Seraph.Utilities.Text import *
import numpy as np

x_plot_offset = 0
animation_timer = 5
positive = True


def RenderScene():
    global x_plot_offset
    glClear(GL_COLOR_BUFFER_BIT)

    graph1 = CartSys2D(x_offset=2, y_offset=2)
    graph1.Draw()

    X = np.linspace(-100, 100, 10000)
    Y1 = np.sin(X - x_plot_offset) * 10
    Y2 = np.cos(X + x_plot_offset) * 10

    plot1 = Plot2D(X, Y1, color.RED)
    plot1.draw()
    plot2 = Plot2D(X, Y2, color.GREEN)
    plot2.draw()

    glutSwapBuffers()


def add_x_offset(value):
    global x_plot_offset, positive
    step = 0.1
    if x_plot_offset >= 100:
        positive = False
    if x_plot_offset <= -100:
        positive = True
    if positive:
        x_plot_offset += step
    else:
        x_plot_offset -= step
    glutPostRedisplay()
    glutTimerFunc(animation_timer, add_x_offset, 1)


def SetupRC():
    glClearColor(0.0, 0.0, 0.0, 1);


def ChangeSize(w, h):
    nRange = 10.0
    if h == 0:
        h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if w <= h:
        glOrtho(-nRange, nRange, -nRange * h / w, nRange * h / w, -nRange, nRange)
    else:
        glOrtho(-nRange * w / h, nRange * w / h, -nRange, nRange, -nRange, nRange)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutCreateWindow("GLRect")
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glutDisplayFunc(RenderScene)
    glutReshapeFunc(ChangeSize)
    glutTimerFunc(animation_timer, add_x_offset, 1)
    SetupRC()
    glutMainLoop()
