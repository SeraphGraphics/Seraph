from OpenGL.GL import *
from OpenGL.GLUT import *

class KeyEvent2D:
    def __init__(self, coordinate):
        self.coordinate = coordinate
    def GraphKeyEvent2D(self, key, x, y):
        if key == GLUT_KEY_RIGHT:
            self.coordinate.renderer.dx += 0.5
        if key == GLUT_KEY_LEFT:
            self.coordinate.renderer.dx -= 0.5
        if key == GLUT_KEY_UP:
            self.coordinate.renderer.dy += 0.5
        if key == GLUT_KEY_DOWN:
            self.coordinate.renderer.dy -= 0.5
        if key == b'-':
            if self.coordinate.renderer.scale_x > 1 and self.coordinate.renderer.scale_y > 1:
                self.coordinate.renderer.scale_x -= 1
                self.coordinate.renderer.scale_y -= 1
            else:
                self.coordinate.renderer.scale_x *= 0.5
                self.coordinate.renderer.scale_y *= 0.5
        if key == b'=':
            if self.coordinate.renderer.scale_x > 1 and self.coordinate.renderer.scale_y > 1:
                self.coordinate.renderer.scale_x += 1
                self.coordinate.renderer.scale_y += 1
            else:
                self.coordinate.renderer.scale_x /= 0.5
                self.coordinate.renderer.scale_y /= 0.5

        self.coordinate.renderer.UpdateOrtho()
    def GraphKeyEvent2DAdvanced(self, key, x, y):
            if key == GLUT_KEY_RIGHT:
                self.coordinate.renderer.dx += 0.5
            if key == GLUT_KEY_LEFT:
                self.coordinate.renderer.dx -= 0.5
            if key == GLUT_KEY_UP:
                self.coordinate.renderer.dy += 0.5
            if key == GLUT_KEY_DOWN:
                self.coordinate.renderer.dy -= 0.5
            if key == b'-':
                if self.coordinate.renderer.scale - 0.5 > 0:
                    self.coordinate.renderer.scale -= 0.05
            if key == b'=':
                self.coordinate.renderer.scale += 0.05
            if key == b'w':
                #print("rotX = ", self.coordinate.renderer.rotX)
                self.coordinate.renderer.rotX += 5
            if key == b's':
                #print("rotX = ", self.coordinate.renderer.rotX)
                self.coordinate.renderer.rotX -= 5
            if key == b'd':
                #print("rotY = ", self.coordinate.renderer.rotY)
                self.coordinate.renderer.rotY += 5
            if key == b'a':
                #print("rotY = ", self.coordinate.renderer.rotY)
                self.coordinate.renderer.rotY -= 5
            self.coordinate.renderer.ReDisplay()
