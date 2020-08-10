from Seraph.Graph2D.Tools_old import *
from Seraph.Utilities.Colors import *
from Seraph.Graph2D.Coordinates_old import *
from Seraph.Graph2D.Plot import *
from Seraph.Utilities.Text import *
from Seraph.Core.Renderer import *
import numpy as np

win = Window(600, 600, "name")
renderer = Renderer(win, 25)

graph = CartSys2D(renderer, x_offset=1, y_offset=1)
'''X = np.linspace(-100, 100, 10000)
Y1 = np.sin(X) * 10
Y2 = X**2
plot1 = Plot2D(X, Y1, color.RED)
plot2 = Plot2D(X, Y2, color.GREEN)
#graph.addPlot(plot1)
graph.addPlot(plot2)'''
graph.Draw()

renderer.Render()
