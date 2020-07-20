from OpenGL.GL import *
from OpenGL.GLUT import *
WHITE = (1, 1, 1)
BLACK = (0, 0, 0)
RED = (1, 0, 0)
GREEN = (0, 1, 0)
BLUE = (0, 0, 1)

def set_color(color, alpha=1):
    glColor4f(*color, alpha)