import numpy as np 
import time 
from ezGraph import *

# Model
# h = 2t - 3.22

# PARAMETERS
dt = 0.5
nsteps = 50

# linear model
a = 0.9921
b = -3.8
c = 53.5

# GRAPH
graph = ezGraph(xmax=30,  xLabel="Time (s)", yLabel="Height (cm)")


# TIME LOOP
for t in range(nsteps):
    modelTime = t * dt
    h = c * a**modelTime + b
    print(modelTime, h)
    graph.add(modelTime, h)
    graph.wait(0.1)

# DRAW GRAPH
graph.keepOpen()
    
