import numpy as np
from ezGraph import *

#initialization
dx = 1
xold, yold = 0, 2

nsteps = 10

def dydx(x=1, y=0):
    slope = 0.5
    return slope

graph = ezGraph(xmin=0, xmax=6, ymin=0, ymax=20)
graph.add(xold,yold, scatter=False)

# loop calculations
for i in range(nsteps):
    x = xold + dx 
    #dydx = xold / 5 
    dy = dydx(xold) * dx
    y = yold + dy

    graph.add(x,y, scatter=False)

    #update for next step
    xold = x
    yold = y



# post processing


graph.ax.axis("equal")
graph.ax.set_ylim(0,10)
graph.ax.set_xlim(0, 10)

x1 = [2, 4, 4]
y1 = [3, 3, 4]
graph.ax.plot(x1, y1)

x1 = [7, 9, 9]
y1 = [5.5, 5.5, 6.5]
graph.ax.plot(x1, y1)

graph.keepOpen()