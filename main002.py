from Seraph.Graph3D.Coordinates import *
from Seraph.Graph3D.Plot import *
from Seraph.Utilities.Text import *
from Seraph.Core.Renderer import *
from Seraph.Core.KeyEvents import *
from random import randint
from random import uniform

x_step = 100
animation_timer = 5
win = Window(600, 600, "name")
renderer = Renderer(win)
points = []

def anim(value):
    global plot1,points
    point_x = randint(-100,100)
    point_y = randint(-100,100)
    point_z = randint(-100,100)

    points.append(Point(point_x, point_y, point_z, color=(uniform(0,1),uniform(0,1),uniform(0,1))))
    plot1.points = points
    renderer.loopAnimation(anim, 200)
graph = CartSys3D(renderer, x_offset=1, y_offset=1, color_grid=color.BLACK, color_bg=color.WHITE)


plot1 = Plot3DbyPoints(points, color.GREEN, type=GL_LINE_STRIP)
graph.add(plot1)
key = KeyEvent2D(graph)
renderer.ApplyKeyEvents(key.GraphKeyEvent2DAdvanced)
renderer.startAnimation(anim)
graph.Draw()
graph.Render()
