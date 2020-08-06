from OpenGL.GLUT import glutBitmapString
import OpenGL.GLUT.fonts as ft
from OpenGL.GL import *
from Seraph.Utilities.Colors import *


class Fonts:
    GLUT_STROKE_ROMAN = ft.GLUT_STROKE_ROMAN
    GLUT_STROKE_MONO_ROMAN = ft.GLUT_STROKE_MONO_ROMAN
    GLUT_BITMAP_9_BY_15 = ft.GLUT_BITMAP_9_BY_15
    GLUT_BITMAP_8_BY_13 = ft.GLUT_BITMAP_8_BY_13
    GLUT_BITMAP_TIMES_ROMAN_10 = ft.GLUT_BITMAP_TIMES_ROMAN_10
    GLUT_BITMAP_TIMES_ROMAN_24 = ft.GLUT_BITMAP_TIMES_ROMAN_24
    GLUT_BITMAP_HELVETICA_10 = ft.GLUT_BITMAP_HELVETICA_10
    GLUT_BITMAP_HELVETICA_12 = ft.GLUT_BITMAP_HELVETICA_12
    GLUT_BITMAP_HELVETICA_18 = ft.GLUT_BITMAP_HELVETICA_18


def putText(x, y, font, string, color):
    set_color(color)
    glRasterPos2f(x, y)
    glutBitmapString(font, string)
