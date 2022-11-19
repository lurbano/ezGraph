import numpy as np
from ezGraph import *

#initialization
dx = 0.01
xold, yold = 0, 4

nsteps = 500

graph = ezGraph(xmin=0, xmax=6, ymin=0, ymax=20)
graph.add(xold,yold)

# loop calculations
for i in range(nsteps):
    x = xold + dx 
    dydx = xold / 5 
    dy = dydx * dx
    y = yold + dy

    graph.add(x,y)

    #update for next step
    xold = x
    yold = y



# post processing
graph.keepOpen()