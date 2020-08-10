from Seraph.Graph2D.Tools import *
from Seraph.Utilities.Colors import *
from Seraph.Graph2D.Coordinates import *
from Seraph.Graph2D.Plot import *
from Seraph.Utilities.Text import *
from Seraph.Core.Render import *
import numpy as np

renderer = Renderer(600, 600, "name", 25, scale_x=1)

graph = CartSys2D(renderer, x_offset=1, y_offset=1)
X = np.linspace(-100, 100, 10000)
Y1 = np.sin(X) * 10
Y2 = np.cos(X) * 10
plot1 = Plot2D(X, Y1, color.RED)
plot2 = Plot2D(X, Y2, color.GREEN)
graph.addPlot(plot1)
#graph.addPlot(plot2)
graph.Draw()

renderer.Render()
