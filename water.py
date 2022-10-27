import numpy as np 
import time 
from ezGraph import *

# Model
# h = 2t - 3.22

# PARAMETERS
dt = 0.5
nsteps = 50

# linear model
m = 2 
b = -3.22

# GRAPH
graph = ezGraph(xmax=30, ymin=0, ymax=50, xLabel="Time (s)", yLabel="Height (cm)")


# TIME LOOP
for t in range(nsteps):
    modelTime = t * dt
    h = m * modelTime + b
    print(modelTime, h)
    graph.add(modelTime, h)
    graph.wait(0.1)

# DRAW GRAPH
graph.keepOpen()
    
