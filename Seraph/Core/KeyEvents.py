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
