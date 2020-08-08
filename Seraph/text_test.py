from OpenGL.GL import *
from OpenGL.GLUT import *
from Seraph.Graph2D.Tools import *
from Seraph.Utilities.Colors import *
from Seraph.Graph2D.Coordinates import *
from Seraph.Graph2D.Plot import *
from Seraph.Utilities.Text import *
import numpy as np


def draw_string(font, text):
    for ch in text:
        glutStrokeCharacter(font, ch)

def RenderScene():
    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix()
    glTranslatef(10, 10, 0)
    glScalef(1,1,1)
    draw_string(Fonts.GLUT_STROKE_ROMAN, b"Hello!")
    glPopMatrix()
    glFinish()
    glutSwapBuffers()


def SetupRC():
    glClearColor(0.0, 0.0, 0.0, 1)


def ChangeSize(w, h):
    nRange = 100
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
    SetupRC()
    glutMainLoop()
