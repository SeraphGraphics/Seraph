from Seraph.Utilities.Colors import *
from OpenGL.GL import *


class SolidSphere:
    def __init__(self, x, y, z, size, color):
        self.x = x
        self.y = y
        self.z = z
        self.size = size
        self.color = color

    def draw(self):
        set_color(self.color)
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        glutSolidSphere(self.size, 15, 15)
        glTranslatef(-50, 0, 0)
        glPopMatrix()

class SimpleCube:
    def __init__(self, size, color=color.BLACK, alpha=1):
        self.size = size
        self.color = color
        self.alpha = alpha
        self.draw()

    def draw(self):
        set_color(self.color, self.alpha)
        glBegin(GL_QUAD_STRIP)
        glVertex3f(self.size / 2, -self.size / 2, self.size / 2)
        glVertex3f(-self.size / 2, -self.size / 2, self.size / 2)
        glVertex3f(self.size / 2, -self.size / 2, -self.size / 2)
        glVertex3f(-self.size / 2, -self.size / 2, -self.size / 2)
        glEnd()
        glBegin(GL_QUAD_STRIP)
        glVertex3f(self.size / 2, self.size / 2, self.size / 2)
        glVertex3f(-self.size / 2, self.size / 2, self.size / 2)
        glVertex3f(self.size / 2, self.size / 2, -self.size / 2)
        glVertex3f(-self.size / 2, self.size / 2, -self.size / 2)
        glEnd()
        glBegin(GL_QUAD_STRIP)
        glVertex3f(-self.size / 2, self.size / 2, self.size / 2)
        glVertex3f(-self.size / 2, -self.size / 2, self.size / 2)
        glVertex3f(-self.size / 2, self.size / 2, -self.size / 2)
        glVertex3f(-self.size / 2, -self.size / 2, -self.size / 2)
        glEnd()
        glBegin(GL_QUAD_STRIP)
        glVertex3f(self.size / 2, self.size / 2, self.size / 2)
        glVertex3f(self.size / 2, -self.size / 2, self.size / 2)
        glVertex3f(self.size / 2, self.size / 2, -self.size / 2)
        glVertex3f(self.size / 2, -self.size / 2, -self.size / 2)
        glEnd()
        glBegin(GL_QUAD_STRIP)
        glVertex3f(self.size / 2, self.size / 2, -self.size / 2)
        glVertex3f(self.size / 2, -self.size / 2, -self.size / 2)
        glVertex3f(-self.size / 2, self.size / 2, -self.size / 2)
        glVertex3f(-self.size / 2, -self.size / 2, -self.size / 2)
        glEnd()
        glBegin(GL_QUAD_STRIP)
        glVertex3f(self.size / 2, self.size / 2, self.size / 2)
        glVertex3f(self.size / 2, -self.size / 2, self.size / 2)
        glVertex3f(-self.size / 2, self.size / 2, self.size / 2)
        glVertex3f(-self.size / 2, -self.size / 2, self.size / 2)
        glEnd()
