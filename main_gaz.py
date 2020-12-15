from Seraph.Core.KeyEvents import *
from Seraph.Core.Renderer import *
from Seraph.Graph3D.Coordinates import *
from Seraph.Utilities.Text import *

win = Window(600, 600, "name")
renderer = Renderer(win)

# graph = CartSys3D(renderer, x_offset=1, y_offset=1, color_grid=color.BLACK, color_bg=color.WHITE)
graph = CartSys3D(renderer, x_offset=1, y_offset=1, color_grid=color.WHITE, color_bg=color.BLACK)

key = KeyEvent2D(graph)
renderer.ApplyKeyEvents(key.GraphKeyEvent2DAdvanced)
graph.Draw()
graph.Render()
