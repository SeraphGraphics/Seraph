from Seraph.Graph2D.Tools import *
from Seraph.Utilities.Colors import *
from Seraph.Graph2D.Coordinates import *
from Seraph.Graph2D.Plot import *
from Seraph.Utilities.Text import *
from Seraph.Core.Renderer import *
from Seraph.Core.KeyEvents import *
from OpenGL.GLUT import *
import numpy as np
from OpenGL.GLUT import *
x_step = 100
animation_timer = 5
win = Window(600, 600, "name")
renderer = Renderer(win)

def animation(value):
    global x_step, plot2, plot1
    x_step += 0.1
    plot1.Y = np.sin(x0 + x_step) + np.cos(x0 + x_step)*(X - x0)
    plot2.Y = np.sin(X+x_step)
    renderer.loopAnimation(animation, 100)



graph = CartSys2D(renderer, x_offset=1, y_offset=1, color_grid=color.BLACK, color_bg=color.WHITE)

key = KeyEvent2D(graph)
renderer.ApplyKeyEvents(key.GraphKeyEvent2D)
X = np.linspace(-100, 100, 10000)
X1 = np.linspace(-10,10,10000)
x0 = 1
Y1 = np.sin(x0 + x_step) + np.cos(x0+x_step)*(X1 - x0+x_step)

Y2 = np.sin(X+x_step)


plot1 = Plot2D(X1, Y1, color.GREEN)
plot2 = Plot2D(X, Y2, color.RED)
graph.addPlot(plot1)
graph.addPlot(plot2)

# graph.setAnimationFunction(animationEvent, animation_timer)
graph.Draw()
renderer.startAnimation(animation)
graph.Render()
